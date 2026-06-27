#!/usr/bin/env python3
"""Small deterministic H₀ grid expansion around the RLL/LCDM comparator."""

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
    n = int(round((stop - start) / step)) + 1
    return [round(start + i * step, 10) for i in range(n)]


def args_for(base: argparse.Namespace, h0: float, model: str) -> Namespace:
    return Namespace(
        h0=h0,
        omega_m=base.omega_m,
        omega_s0=0.0 if model == "lcdm" else base.omega_s0,
        zt=base.zt,
        wt=base.wt,
        w0=-1.0,
        wa=0.0,
        rs_drag=base.rs_drag,
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--hz", default="data/real/Hz_data_real.csv")
    parser.add_argument("--bao", default="data/real/cosmology/desi_dr2_bao_primary_points.csv")
    parser.add_argument("--bao-covariance", default="data/real/cosmology/desi_dr2_bao_covariance_summary.csv")
    parser.add_argument("--out-json", default="results/h0_grid_expansion_summary.json")
    parser.add_argument("--out-csv", default="results/h0_grid_expansion_scan.csv")
    parser.add_argument("--h0-min", type=float, default=64.0)
    parser.add_argument("--h0-max", type=float, default=74.0)
    parser.add_argument("--h0-step", type=float, default=0.5)
    parser.add_argument("--omega-m", type=float, default=0.315)
    parser.add_argument("--omega-s0", type=float, default=0.05)
    parser.add_argument("--zt", type=float, default=1.2)
    parser.add_argument("--wt", type=float, default=0.35)
    parser.add_argument("--rs-drag", type=float, default=147.0)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    hz = cmp.load_hz(Path(args.hz))
    bao = cmp.load_bao(Path(args.bao), bao_format="auto")
    cov = cmp.load_bao_covariance_summary(Path(args.bao_covariance))
    rows: list[dict[str, float | str]] = []
    best: dict[str, dict[str, float | str]] = {}
    for model in ("lcdm", "rll"):
        for h0 in frange(args.h0_min, args.h0_max, args.h0_step):
            point_args = args_for(args, h0, model)
            metrics = cmp.evaluate(model, hz, bao, point_args, cov)
            row = {"model": model, "H0": h0, **metrics}
            rows.append(row)
            current = best.get(model)
            if current is None or float(row["chi2_total"]) < float(current["chi2_total"]):
                best[model] = row
    out_csv = Path(args.out_csv)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["model", "H0", "chi2_hz", "chi2_bao", "chi2_total", "n_params", "aic", "bic"])
        writer.writeheader()
        writer.writerows(rows)
    h0_lcdm = float(best["lcdm"]["H0"])
    h0_rll = float(best["rll"]["H0"])
    delta_aic = float(best["rll"]["aic"]) - float(best["lcdm"]["aic"])
    quality_gates = {
        "gate_1_grid_lcdm_internal": args.h0_min < h0_lcdm < args.h0_max,
        "gate_1_grid_rll_internal": args.h0_min < h0_rll < args.h0_max,
        "gate_2_h0_degeneracy": abs(h0_rll - h0_lcdm) < 1.0,
        "gate_3_delta_aic": delta_aic < 4.0,
    }
    summary = {
        "schema_version": "1.0",
        "module": "h0_grid_expansion",
        "claim_allowed": False,
        "inputs": {"hz": args.hz, "bao": args.bao, "h0_grid": [args.h0_min, args.h0_max, args.h0_step]},
        "best_by_model": best,
        "comparisons": {"delta_H0_rll_minus_lcdm": h0_rll - h0_lcdm, "delta_aic_rll_minus_lcdm": delta_aic},
        "quality_gates": quality_gates,
        "status": "grid_passed" if all(quality_gates.values()) else "claim_blocked_quality_gate_failed",
        "rollback": "Remove generated CSV/JSON or git revert; no raw data is changed.",
    }
    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(summary, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps({"best_by_model": best, "quality_gates": quality_gates, "status": summary["status"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
