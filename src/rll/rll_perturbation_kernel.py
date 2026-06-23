#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path


def exp_clip(x: float) -> float:
    return math.exp(max(-700.0, min(700.0, x)))


def f_transition(z: float, zt: float, wt: float) -> float:
    if wt <= 0.0:
        raise ValueError("wt must be positive")
    return 1.0 / (1.0 + exp_clip((z - zt) / wt))


def rho_factor(a: float, zt: float, wt: float) -> float:
    z = 1.0 / a - 1.0
    f = f_transition(z, zt, wt)
    return f + (1.0 - f) * a ** -3


def e2_rll(a: float, omega_m: float, omega_s0: float, zt: float, wt: float) -> float:
    return omega_m * a ** -3 + (1.0 - omega_m - omega_s0) + omega_s0 * rho_factor(a, zt, wt)


def omega_m_a(a: float, omega_m: float, omega_s0: float, zt: float, wt: float) -> float:
    return omega_m * a ** -3 / e2_rll(a, omega_m, omega_s0, zt, wt)


def dlnh_dlna(a: float, omega_m: float, omega_s0: float, zt: float, wt: float) -> float:
    x = math.log(a)
    h = 1.0e-4
    ep = e2_rll(math.exp(x + h), omega_m, omega_s0, zt, wt)
    em = e2_rll(math.exp(x - h), omega_m, omega_s0, zt, wt)
    return 0.25 * (math.log(ep) - math.log(em)) / h


def rhs(x: float, y: tuple[float, float], p: argparse.Namespace) -> tuple[float, float]:
    a = math.exp(x)
    delta, velocity = y
    drag = 2.0 + dlnh_dlna(a, p.omega_m, p.omega_s0, p.zt, p.wt)
    source = 1.5 * omega_m_a(a, p.omega_m, p.omega_s0, p.zt, p.wt) * delta
    return velocity, -drag * velocity + source


def rk4(x: float, y: tuple[float, float], h: float, p: argparse.Namespace) -> tuple[float, float]:
    k1 = rhs(x, y, p)
    k2 = rhs(x + 0.5 * h, (y[0] + 0.5 * h * k1[0], y[1] + 0.5 * h * k1[1]), p)
    k3 = rhs(x + 0.5 * h, (y[0] + 0.5 * h * k2[0], y[1] + 0.5 * h * k2[1]), p)
    k4 = rhs(x + h, (y[0] + h * k3[0], y[1] + h * k3[1]), p)
    return (
        y[0] + h * (k1[0] + 2.0 * k2[0] + 2.0 * k3[0] + k4[0]) / 6.0,
        y[1] + h * (k1[1] + 2.0 * k2[1] + 2.0 * k3[1] + k4[1]) / 6.0,
    )


def solve_kernel(p: argparse.Namespace) -> list[dict[str, float]]:
    x0 = math.log(p.a_min)
    x1 = 0.0
    n = max(8, p.steps)
    h = (x1 - x0) / n
    a0 = math.exp(x0)
    y = (a0, a0)
    rows = []
    x = x0
    for _ in range(n + 1):
        a = math.exp(x)
        rows.append({"a": a, "z": 1.0 / a - 1.0, "delta_raw": y[0], "theta_raw": y[1]})
        if x < x1:
            y = rk4(x, y, h, p)
            x += h
    norm = rows[-1]["delta_raw"]
    for row in rows:
        row["delta"] = row["delta_raw"] / norm
        row["theta"] = row["theta_raw"] / norm
        row["growth_rate"] = row["theta"] / row["delta"]
    return rows


def write_csv(path: str, rows: list[dict[str, float]]) -> None:
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    fields = ["a", "z", "delta", "theta", "growth_rate"]
    with out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row[k] for k in fields})


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser()
    p.add_argument("--omega-m", type=float, default=0.315)
    p.add_argument("--omega-s0", type=float, default=0.059)
    p.add_argument("--zt", type=float, default=1.164)
    p.add_argument("--wt", type=float, default=0.405)
    p.add_argument("--a-min", type=float, default=1.0e-3)
    p.add_argument("--steps", type=int, default=4000)
    p.add_argument("--out-csv", default="results/rll_perturbation_kernel.csv")
    p.add_argument("--out-json", default="results/rll_perturbation_kernel_summary.json")
    return p


def main() -> None:
    p = parser().parse_args()
    rows = solve_kernel(p)
    write_csv(p.out_csv, rows)
    summary = {
        "status": "linear_perturbation_kernel_available",
        "background": "src/rll/class_rll_background.c",
        "regime": "GR matter perturbation on exact RLL background",
        "delta_z0": rows[-1]["delta"],
        "growth_rate_z0": rows[-1]["growth_rate"],
        "cmb_cl_exact": "TOKEN_VAZIO",
        "nonlinear_pk_exact": "TOKEN_VAZIO",
    }
    out = Path(p.out_json)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
