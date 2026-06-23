#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def exp_clip(x: float) -> float:
    return math.exp(max(-700.0, min(700.0, x)))


def f_transition(z: float, zt: float, wt: float) -> float:
    if wt <= 0:
        raise ValueError("wt must be positive")
    return 1.0 / (1.0 + exp_clip((z - zt) / wt))


def rho_factor(z: float, zt: float, wt: float) -> float:
    f = f_transition(z, zt, wt)
    return f + (1.0 - f) * (1.0 + z) ** 3


def e2(z: float, om: float, os0: float, zt: float, wt: float) -> float:
    ol = 1.0 - om - os0
    return om * (1.0 + z) ** 3 + ol + os0 * rho_factor(z, zt, wt)


def w_eff(z: float, zt: float, wt: float) -> float:
    return -f_transition(z, zt, wt) / rho_factor(z, zt, wt)


def omega_s(z: float, om: float, os0: float, zt: float, wt: float) -> float:
    return os0 * rho_factor(z, zt, wt) / e2(z, om, os0, zt, wt)


def kinetic_gate(z: float, om: float, os0: float, zt: float, wt: float) -> float:
    return (1.0 + w_eff(z, zt, wt)) * omega_s(z, om, os0, zt, wt)


def grid(a: float, b: float, n: int) -> list[float]:
    if n < 2:
        return [a]
    h = (b - a) / (n - 1)
    return [a + i * h for i in range(n)]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--omega-m", type=float, default=0.315)
    ap.add_argument("--omega-s0", type=float, default=0.059)
    ap.add_argument("--zt", type=float, default=1.164)
    ap.add_argument("--wt", type=float, default=0.405)
    ap.add_argument("--z-max", type=float, default=5.0)
    ap.add_argument("--n", type=int, default=501)
    ap.add_argument("--out-json", default="results/rll_background_check.json")
    args = ap.parse_args()
    zs = grid(0.0, args.z_max, args.n)
    rows = [
        {
            "z": z,
            "f": f_transition(z, args.zt, args.wt),
            "w_eff": w_eff(z, args.zt, args.wt),
            "omega_s": omega_s(z, args.omega_m, args.omega_s0, args.zt, args.wt),
            "kinetic_gate": kinetic_gate(z, args.omega_m, args.omega_s0, args.zt, args.wt),
            "cs2_proxy": f_transition(z, args.zt, args.wt),
        }
        for z in zs
    ]
    summary = {
        "params": vars(args),
        "ranges": {
            "f": [min(r["f"] for r in rows), max(r["f"] for r in rows)],
            "w_eff": [min(r["w_eff"] for r in rows), max(r["w_eff"] for r in rows)],
            "kinetic_gate": [min(r["kinetic_gate"] for r in rows), max(r["kinetic_gate"] for r in rows)],
            "cs2_proxy": [min(r["cs2_proxy"] for r in rows), max(r["cs2_proxy"] for r in rows)],
        },
        "checks": {
            "kinetic_gate_non_negative": all(r["kinetic_gate"] >= -1e-10 for r in rows),
            "w_eff_above_minus_one": all(r["w_eff"] >= -1.0 - 1e-10 for r in rows),
            "cs2_proxy_bounded": all(-1e-10 <= r["cs2_proxy"] <= 1.0 + 1e-10 for r in rows),
            "growth_solver": "TOKEN_VAZIO",
        },
    }
    out = Path(args.out_json)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary["checks"], indent=2))


if __name__ == "__main__":
    main()
