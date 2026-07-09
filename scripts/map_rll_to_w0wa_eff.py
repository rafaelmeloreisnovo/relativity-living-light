#!/usr/bin/env python3
"""Map RLL logistic background parameters to local effective CPL coordinates.

The mapper computes w0_eff = w(a=1) and wa_eff = -dw/da|a=1 for the RLL
dark-sector effective equation of state. This is a diagnostic bridge to compare
RLL trajectories with CPL/w0waCDM; it is not a fit and not a claim.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path


def transition_f(z: float, zt: float, wt: float) -> float:
    return 1.0 / (1.0 + math.exp(max(-700.0, min(700.0, (z - zt) / wt))))


def rll_sector_w(z: float, zt: float, wt: float) -> float:
    a = 1.0 / (1.0 + z)
    f = transition_f(z, zt, wt)
    denom = f + (1.0 - f) * a ** -3
    return -f / denom


def rll_dark_w(a: float, omega_m: float, omega_s0: float, zt: float, wt: float) -> float:
    z = 1.0 / a - 1.0
    f = transition_f(z, zt, wt)
    omega_lambda = 1.0 - omega_m - omega_s0
    rho_dark = omega_lambda + omega_s0 * (f + (1.0 - f) * a ** -3)
    pressure_dark = -(omega_lambda + omega_s0 * f)
    if rho_dark == 0.0:
        raise ZeroDivisionError("dark-sector density is zero")
    return pressure_dark / rho_dark


def derivative_dw_da(func, a: float = 1.0, h: float = 1.0e-4) -> float:
    return (func(a + h) - func(a - h)) / (2.0 * h)


def frange(start: float, stop: float, step: float) -> list[float]:
    if step <= 0:
        raise ValueError("step must be positive")
    n = int(round((stop - start) / step)) + 1
    return [round(start + i * step, 10) for i in range(n)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--omega-m", type=float, default=0.315)
    parser.add_argument("--omega-s0-min", type=float, default=0.0)
    parser.add_argument("--omega-s0-max", type=float, default=0.12)
    parser.add_argument("--omega-s0-step", type=float, default=0.01)
    parser.add_argument("--zt", type=float, default=1.2)
    parser.add_argument("--wt", type=float, default=0.35)
    parser.add_argument("--cpl-w0", type=float, default=-0.3)
    parser.add_argument("--cpl-wa", type=float, default=-1.84)
    parser.add_argument("--out-json", default="results/rll_w0wa_eff_map.json")
    parser.add_argument("--out-csv", default="results/rll_w0wa_eff_map.csv")
    args = parser.parse_args()

    rows = []
    for omega_s0 in frange(args.omega_s0_min, args.omega_s0_max, args.omega_s0_step):
        if args.omega_m + omega_s0 >= 1.0:
            status = "invalid_omega_lambda_negative"
            w0_eff = None
            wa_eff = None
            distance = None
        else:
            def local_dark_w(a: float) -> float:
                return rll_dark_w(a, args.omega_m, omega_s0, args.zt, args.wt)

            w0_eff = local_dark_w(1.0)
            wa_eff = -derivative_dw_da(local_dark_w)
            distance = math.sqrt((w0_eff - args.cpl_w0) ** 2 + (wa_eff - args.cpl_wa) ** 2)
            status = "mapped_claim_blocked"
        rows.append({
            "omega_m": args.omega_m,
            "omega_s0": omega_s0,
            "omega_lambda": 1.0 - args.omega_m - omega_s0,
            "zt": args.zt,
            "wt": args.wt,
            "w0_eff_dark": w0_eff,
            "wa_eff_dark": wa_eff,
            "cpl_w0_reference": args.cpl_w0,
            "cpl_wa_reference": args.cpl_wa,
            "distance_to_cpl_reference": distance,
            "sector_w_z0": rll_sector_w(0.0, args.zt, args.wt),
            "status": status,
            "claim_allowed": False,
        })

    best = min(
        [row for row in rows if row["distance_to_cpl_reference"] is not None],
        key=lambda row: float(row["distance_to_cpl_reference"]),
        default=None,
    )

    out_csv = Path(args.out_csv)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    summary = {
        "schema": "rll.w0wa_eff_mapper.v1",
        "claim_allowed": False,
        "mode": "diagnostic_mapping_not_fit",
        "definition": "w0_eff=w_dark(a=1), wa_eff=-dw_dark/da at a=1",
        "inputs": vars(args),
        "rows": len(rows),
        "best_distance_to_cpl_reference": best,
        "safe_conclusion": "This mapper locates RLL in CPL coordinates for diagnostics only; real-data preference requires likelihood artifacts and baselines.",
    }
    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"best_distance_to_cpl_reference": best, "claim_allowed": False}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
