#!/usr/bin/env python3
"""Deterministic H0 grid expansion around the RLL/LCDM/w0wa comparator.

This script mitigates H0 lower-bound artifacts by scanning a corrected interval
and writing auditable CSV/JSON artifacts. It is a point-grid scan, not MCMC,
not nested sampling, and not a scientific superiority claim.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from argparse import Namespace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import rll_vs_lcdm as cmp


def frange(start: float, stop: float, step: float) -> list[float]:
    if step <= 0:
        raise ValueError("step must be positive")
    if start >= stop:
        raise ValueError("start must be smaller than stop")
    n = int(round((stop - start) / step)) + 1
    return [round(start + i * step, 10) for i in range(n)]


def args_for(base: argparse.Namespace, h0: float, model: str) -> Namespace:
    return Namespace(
        h0=h0,
        omega_m=base.omega_m,
        omega_s0=base.omega_s0 if model == "rll" else 0.0,
        zt=base.zt,
        wt=base.wt,
        w0=base.w0 if model == "w0wa" else -1.0,
        wa=base.wa if model == "w0wa" else 0.0,
        rs_drag=base.rs_drag,
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hz", default="data/real/Hz_data_real.csv")
    parser.add_argument("--bao", default="data/real/cosmology/desi_dr2_bao_primary_points.csv")
    parser.add_argument("--bao-covariance", default="data/real/cosmology/desi_dr2_bao_covariance_summary.csv")
    parser.add_argument("--bao-format", default="auto")
    parser.add_argument("--out-json", default="results/h0_grid_expansion_summary.json")
    parser.add_argument("--out-csv", default="results/h0_grid_expansion_scan.csv")
    parser.add_argument("--h0-min", type=float, default=64.0)
    parser.add_argument("--h0-max", type=float, default=74.0)
    parser.add_argument("--h0-step", type=float, default=0.5)
    parser.add_argument("--omega-m", type=float, default=0.315)
    parser.add_argument("--omega-s0", type=float, default=0.05)
    parser.add_argument("--zt", type=float, default=1.2)
    parser.add_argument("--wt", type=float, default=0.35)
    parser.add_argument("--w0", type=float, default=-0.3)
    parser.add_argument("--wa", type=float, default=-1.84)
    parser.add_argument("--rs-drag", type=float, default=147.0)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    hz = cmp.load_hz(Path(args.hz))
    bao = cmp.load_bao(Path(args.bao), bao_format=args.bao_format)
    cov = cmp.load_bao_covariance_summary(Path(args.bao_covariance))

    rows: list[dict[str, float | str | int]] = []
    best: dict[str, dict[str, float | str | int]] = {}
    for model in ("lcdm", "w0wa", "rll"):
        for h0 in frange(args.h0_min, args.h0_max, args.h0_step):
            point_args = args_for(args, h0, model)
            metrics = cmp.evaluate(model, hz, bao, point_args, cov)
            row: dict[str, float | str | int] = {
                "model": model,
                "H0": h0,
                "omega_m": args.omega_m,
                "omega_s0": args.omega_s0 if model == "rll" else "",
                "zt": args.zt if model == "rll" else "",
                "wt": args.wt if model == "rll" else "",
                "w0": args.w0 if model == "w0wa" else "",
                "wa": args.wa if model == "w0wa" else "",
                **metrics,
            }
            rows.append(row)
            current = best.get(model)
            if current is None or float(row["chi2_total"]) < float(current["chi2_total"]):
                best[model] = row

    out_csv = Path(args.out_csv)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "model",
        "H0",
        "omega_m",
        "omega_s0",
        "zt",
        "wt",
        "w0",
        "wa",
        "chi2_hz",
        "chi2_bao",
        "chi2_total",
        "n_params",
        "aic",
        "bic",
    ]
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    h0_lcdm = float(best["lcdm"]["H0"])
    h0_rll = float(best["rll"]["H0"])
    delta_aic_lcdm = float(best["rll"]["aic"]) - float(best["lcdm"]["aic"])
    delta_aic_w0wa = float(best["rll"]["aic"]) - float(best["w0wa"]["aic"])
    quality_gates = {
        "gate_1_grid_lcdm_internal": args.h0_min < h0_lcdm < args.h0_max,
        "gate_1_grid_rll_internal": args.h0_min < h0_rll < args.h0_max,
        "gate_2_h0_degeneracy_lcdm_rll": abs(h0_rll - h0_lcdm) < 1.0,
        "gate_3_delta_aic_rll_minus_lcdm_lt_4": delta_aic_lcdm < 4.0,
        "gate_4_w0wa_adversary_present": "w0wa" in best,
    }
    summary = {
        "schema_version": "1.1",
        "module": "h0_grid_expansion",
        "claim_allowed": False,
        "mode": "point_grid_scan_not_optimizer",
        "inputs": {
            "hz": args.hz,
            "bao": args.bao,
            "bao_covariance": args.bao_covariance,
            "h0_grid": [args.h0_min, args.h0_max, args.h0_step],
        },
        "fixed_parameters": {
            "omega_m": args.omega_m,
            "omega_s0": args.omega_s0,
            "zt": args.zt,
            "wt": args.wt,
            "w0": args.w0,
            "wa": args.wa,
            "rs_drag": args.rs_drag,
        },
        "best_by_model": best,
        "comparisons": {
            "delta_H0_rll_minus_lcdm": h0_rll - h0_lcdm,
            "delta_aic_rll_minus_lcdm": delta_aic_lcdm,
            "delta_aic_rll_minus_w0wa": delta_aic_w0wa,
        },
        "quality_gates": quality_gates,
        "status": "grid_passed" if all(quality_gates.values()) else "claim_blocked_quality_gate_failed",
        "safe_conclusion": "Use this artifact to detect H0 boundary behavior; do not use it as model-superiority evidence.",
        "rollback": "Remove generated CSV/JSON or git revert; no raw data is changed.",
    }
    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(summary, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps({"best_by_model": best, "quality_gates": quality_gates, "status": summary["status"]}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
