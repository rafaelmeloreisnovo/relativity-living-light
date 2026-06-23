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


def e2_lcdm(a: float, om: float) -> float:
    return om * a ** -3 + (1.0 - om)


def e2_w0wa(a: float, om: float, w0: float, wa: float) -> float:
    z = 1.0 / a - 1.0
    ode = (1.0 - om) * a ** (-3.0 * (1.0 + w0 + wa)) * exp_clip(-3.0 * wa * z / (1.0 + z))
    return om * a ** -3 + ode


def e2_rll(a: float, om: float, os0: float, zt: float, wt: float) -> float:
    z = 1.0 / a - 1.0
    f = f_transition(z, zt, wt)
    ol = 1.0 - om - os0
    return om * a ** -3 + ol + os0 * (f + (1.0 - f) * a ** -3)


def e2_model(a: float, model: str, p: argparse.Namespace) -> float:
    if model == "lcdm":
        return e2_lcdm(a, p.omega_m)
    if model == "w0wa":
        return e2_w0wa(a, p.omega_m, p.w0, p.wa)
    if model == "rll":
        return e2_rll(a, p.omega_m, p.omega_s0, p.zt, p.wt)
    raise ValueError(f"unknown model: {model}")


def omega_m_a(a: float, model: str, p: argparse.Namespace) -> float:
    return p.omega_m * a ** -3 / e2_model(a, model, p)


def dlnh_dlna(a: float, model: str, p: argparse.Namespace) -> float:
    x = math.log(a)
    h = 1.0e-4
    ap = math.exp(x + h)
    am = math.exp(x - h)
    return 0.25 * (math.log(e2_model(ap, model, p)) - math.log(e2_model(am, model, p))) / h


def rhs(x: float, y: tuple[float, float], model: str, p: argparse.Namespace) -> tuple[float, float]:
    a = math.exp(x)
    d, u = y
    drag = 2.0 + dlnh_dlna(a, model, p)
    source = 1.5 * omega_m_a(a, model, p) * d
    return u, -drag * u + source


def rk4_step(x: float, y: tuple[float, float], h: float, model: str, p: argparse.Namespace) -> tuple[float, float]:
    k1 = rhs(x, y, model, p)
    y2 = (y[0] + 0.5 * h * k1[0], y[1] + 0.5 * h * k1[1])
    k2 = rhs(x + 0.5 * h, y2, model, p)
    y3 = (y[0] + 0.5 * h * k2[0], y[1] + 0.5 * h * k2[1])
    k3 = rhs(x + 0.5 * h, y3, model, p)
    y4 = (y[0] + h * k3[0], y[1] + h * k3[1])
    k4 = rhs(x + h, y4, model, p)
    return (
        y[0] + h * (k1[0] + 2.0 * k2[0] + 2.0 * k3[0] + k4[0]) / 6.0,
        y[1] + h * (k1[1] + 2.0 * k2[1] + 2.0 * k3[1] + k4[1]) / 6.0,
    )


def integrate_growth(model: str, p: argparse.Namespace) -> list[dict[str, float]]:
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
        rows.append({"a": a, "z": 1.0 / a - 1.0, "D_raw": y[0], "dD_dlna_raw": y[1]})
        if x < x1:
            y = rk4_step(x, y, h, model, p)
            x += h
    d0 = rows[-1]["D_raw"]
    for r in rows:
        r["D"] = r["D_raw"] / d0
        r["dD_dlna"] = r["dD_dlna_raw"] / d0
        r["f_growth"] = r["dD_dlna"] / r["D"]
        r["fsigma8"] = r["f_growth"] * p.sigma8_0 * r["D"]
    return rows


def interp(rows: list[dict[str, float]], z: float, key: str) -> float:
    target_a = 1.0 / (1.0 + z)
    ordered = sorted(rows, key=lambda r: r["a"])
    if target_a <= ordered[0]["a"]:
        return ordered[0][key]
    if target_a >= ordered[-1]["a"]:
        return ordered[-1][key]
    lo = ordered[0]
    for hi in ordered[1:]:
        if lo["a"] <= target_a <= hi["a"]:
            t = (target_a - lo["a"]) / (hi["a"] - lo["a"])
            return lo[key] + t * (hi[key] - lo[key])
        lo = hi
    return ordered[-1][key]


def prediction_grid(p: argparse.Namespace) -> list[float]:
    return [round(i * p.z_step, 10) for i in range(int(p.z_max / p.z_step) + 1)]


def read_data(path: str | None) -> list[dict[str, float]]:
    if not path:
        return []
    out = []
    with Path(path).open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            z = float(row.get("z") or row.get("redshift"))
            obs = float(row.get("fsigma8") or row.get("f_sigma8") or row.get("value"))
            err = float(row.get("sigma") or row.get("error") or row.get("err"))
            out.append({"z": z, "obs": obs, "sigma": err})
    return out


def evaluate_models(p: argparse.Namespace) -> tuple[dict, list[dict[str, float]]]:
    models = ["lcdm", "w0wa", "rll"] if p.model == "all" else [p.model]
    data = read_data(p.data)
    all_predictions: list[dict[str, float]] = []
    summary: dict[str, object] = {
        "params": {
            "omega_m": p.omega_m,
            "omega_s0": p.omega_s0,
            "zt": p.zt,
            "wt": p.wt,
            "w0": p.w0,
            "wa": p.wa,
            "sigma8_0": p.sigma8_0,
            "a_min": p.a_min,
            "steps": p.steps,
        },
        "assumptions": {
            "equation": "D_xx + (2 + dlnH_dlna) D_x - 1.5 Omega_m(a) D = 0",
            "normalization": "D(a=1)=1",
            "regime": "linear_growth_smooth_dark_sector_GR_background",
            "nonlinear_power": "TOKEN_VAZIO",
            "boltzmann_cmb": "TOKEN_VAZIO",
            "baryonic_feedback": "TOKEN_VAZIO",
        },
        "models": {},
    }
    z_grid = prediction_grid(p)
    for model in models:
        rows = integrate_growth(model, p)
        for z in z_grid:
            pred = {
                "model": model,
                "z": z,
                "D": interp(rows, z, "D"),
                "f_growth": interp(rows, z, "f_growth"),
                "fsigma8": interp(rows, z, "fsigma8"),
            }
            all_predictions.append(pred)
        chi2 = None
        if data:
            chi2 = 0.0
            for item in data:
                theory = interp(rows, item["z"], "fsigma8")
                chi2 += ((theory - item["obs"]) / item["sigma"]) ** 2
        summary["models"][model] = {
            "D_z0": interp(rows, 0.0, "D"),
            "f_z0": interp(rows, 0.0, "f_growth"),
            "fsigma8_z0": interp(rows, 0.0, "fsigma8"),
            "D_z1": interp(rows, 1.0, "D"),
            "fsigma8_z1": interp(rows, 1.0, "fsigma8"),
            "chi2_fsigma8": chi2,
            "n_data": len(data),
        }
    return summary, all_predictions


def write_predictions(path: str, rows: list[dict[str, float]]) -> None:
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as f:
        fields = ["model", "z", "D", "f_growth", "fsigma8"]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", choices=["lcdm", "w0wa", "rll", "all"], default="all")
    ap.add_argument("--omega-m", type=float, default=0.315)
    ap.add_argument("--omega-s0", type=float, default=0.059)
    ap.add_argument("--zt", type=float, default=1.164)
    ap.add_argument("--wt", type=float, default=0.405)
    ap.add_argument("--w0", type=float, default=-1.0)
    ap.add_argument("--wa", type=float, default=0.0)
    ap.add_argument("--sigma8-0", type=float, default=0.811)
    ap.add_argument("--a-min", type=float, default=1.0e-3)
    ap.add_argument("--steps", type=int, default=4000)
    ap.add_argument("--z-max", type=float, default=2.0)
    ap.add_argument("--z-step", type=float, default=0.1)
    ap.add_argument("--data", default=None)
    ap.add_argument("--out-json", default="results/rll_growth_fsigma8_summary.json")
    ap.add_argument("--out-csv", default="results/rll_growth_fsigma8_predictions.csv")
    return ap


def main() -> None:
    p = build_parser().parse_args()
    summary, predictions = evaluate_models(p)
    out_json = Path(p.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    write_predictions(p.out_csv, predictions)
    print(json.dumps(summary["models"], indent=2))


if __name__ == "__main__":
    main()
