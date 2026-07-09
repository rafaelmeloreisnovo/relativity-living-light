#!/usr/bin/env python3
"""Materialize the C01 z_t falsification scan for the RLL logistic sector.

The script keeps the protocol epistemically conservative: it writes point-scan
artifacts and PASS/FAIL/TOKEN_VAZIO statuses, but it does not claim discovery.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
from typing import Any, Sequence

import yaml
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import rll_vs_lcdm


def _repo_root() -> Path:
    return REPO_ROOT


def _load_protocol(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        payload = yaml.safe_load(fh)
    if not isinstance(payload, dict):
        raise ValueError(f"Protocol must be a YAML mapping: {path}")
    return payload


def _args_for(base: argparse.Namespace, zt: float) -> argparse.Namespace:
    copied = argparse.Namespace(**vars(base))
    copied.zt = float(zt)
    return copied


def _base_model_args(protocol: dict[str, Any], cli: argparse.Namespace) -> argparse.Namespace:
    scan = protocol.get("scan_zt", {})
    parser = rll_vs_lcdm.build_arg_parser()
    args = parser.parse_args([])
    args.bao = cli.bao or protocol.get("test_C01_background", {}).get("desi_data", args.bao)
    args.hz = cli.hz or protocol.get("test_C01_background", {}).get("hz_data", args.hz)
    args.h0 = float(cli.h0 if cli.h0 is not None else scan.get("H0", args.h0))
    args.omega_m = float(cli.omega_m if cli.omega_m is not None else scan.get("Om", args.omega_m))
    args.omega_s0 = float(cli.omega_s0 if cli.omega_s0 is not None else scan.get("Os0", args.omega_s0))
    args.wt = float(cli.wt if cli.wt is not None else scan.get("wt", args.wt))
    args.adversary = "lcdm"
    return args


def _curvature(rows: list[dict[str, float]], key: str, idx: int) -> float | None:
    if idx <= 0 or idx >= len(rows) - 1:
        return None
    x0, x1, x2 = rows[idx - 1]["zt"], rows[idx]["zt"], rows[idx + 1]["zt"]
    y0, y1, y2 = rows[idx - 1][key], rows[idx][key], rows[idx + 1][key]
    if not math.isclose(x1 - x0, x2 - x1, rel_tol=1e-9, abs_tol=1e-9):
        left = (y1 - y0) / (x1 - x0)
        right = (y2 - y1) / (x2 - x1)
        return 2.0 * (right - left) / (x2 - x0)
    h = x1 - x0
    return (y0 - 2.0 * y1 + y2) / (h * h)


def _weff_present(zt: float, wt: float) -> float:
    # For rho_s(z)=Omega_s0[f(z)+(1-f(z))(1+z)^3], w_eff=-1+(1/3)dlnrho/dln(1+z).
    f0 = rll_vs_lcdm.rll_transition_f(0.0, zt, wt)
    df_dz0 = -f0 * (1.0 - f0) / wt
    drho_dz0 = df_dz0 + (-df_dz0) + 3.0 * (1.0 - f0)
    rho0_shape = 1.0
    return -1.0 + drho_dz0 / (3.0 * rho0_shape)


def _status(rows: list[dict[str, float]], wt: float) -> dict[str, Any]:
    bao_min_idx = min(range(len(rows)), key=lambda i: rows[i]["chi2_bao"])
    hz_min_idx = min(range(len(rows)), key=lambda i: rows[i]["chi2_hz"])
    bao_min = rows[bao_min_idx]
    hz_min = rows[hz_min_idx]
    nearest = [row for row in rows if abs(row["zt"] - bao_min["zt"]) >= 0.29]
    delta_neighbor = min((row["chi2_bao"] - bao_min["chi2_bao"] for row in nearest), default=0.0)
    curvature = _curvature(rows, "chi2_bao", bao_min_idx)
    weff_z05 = _weff_present(0.5, wt)
    return {
        "claim_allowed": False,
        "best": {"zt_bao": bao_min["zt"], "zt_hz": hz_min["zt"], "zt_total": min(rows, key=lambda r: r["chi2_total"])["zt"]},
        "falsifiers": {
            "F_ZT_01": {
                "status": "PASS" if (curvature is not None and curvature > 0.0 and delta_neighbor > 1.0) else "FAIL",
                "delta_chi2_bao_nearest_pm_0p3": delta_neighbor,
                "curvature_bao_grid": curvature,
            },
            "F_ZT_02": {
                "status": "PASS" if abs(bao_min["zt"] - hz_min["zt"]) < 0.2 else "FAIL",
                "abs_zt_bao_minus_hz": abs(bao_min["zt"] - hz_min["zt"]),
            },
            "F_ZT_03": {
                "status": "PASS" if weff_z05 < -0.85 else "FAIL",
                "w_eff_z0_at_zt_0p5": weff_z05,
            },
        },
    }


def run_scan(protocol_path: Path, out_dir: Path, cli: argparse.Namespace) -> dict[str, Any]:
    protocol = _load_protocol(protocol_path)
    base = _base_model_args(protocol, cli)
    zt_values = [float(z) for z in protocol.get("scan_zt", {}).get("zt_range", [])]
    if not zt_values:
        raise ValueError("scan_zt.zt_range is required")
    hz = rll_vs_lcdm.load_hz(_repo_root() / base.hz)
    bao = rll_vs_lcdm.load_bao(_repo_root() / base.bao, bao_format=base.bao_format)
    cov = rll_vs_lcdm.load_bao_covariance_summary(_repo_root() / base.bao_covariance)
    out_dir.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, float]] = []
    for zt in zt_values:
        args = _args_for(base, zt)
        metrics = rll_vs_lcdm.evaluate("rll", hz, bao, args, cov)
        row = {"zt": zt, "chi2_hz": float(metrics["chi2_hz"]), "chi2_bao": float(metrics["chi2_bao"]), "chi2_total": float(metrics["chi2_total"])}
        rows.append(row)
        (out_dir / f"zt_{zt:g}.json").write_text(json.dumps({"params": rll_vs_lcdm.parameter_payload("rll", args), "metrics": row}, indent=2), encoding="utf-8")
    rows.sort(key=lambda r: r["zt"])
    with (out_dir / "zt_scan.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["zt", "chi2_hz", "chi2_bao", "chi2_total"])
        writer.writeheader(); writer.writerows(rows)
    summary = {"protocol": str(protocol_path), "scan": rows, "assessment": _status(rows, base.wt)}
    (out_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


def main(argv: Sequence[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Run RLL z_t falsification scan C01")
    parser.add_argument("--protocol", default="protocols/05_slingshot_zt_falsification.yml")
    parser.add_argument("--out-dir", default="results/zt_scan")
    parser.add_argument("--bao")
    parser.add_argument("--hz")
    parser.add_argument("--h0", type=float)
    parser.add_argument("--omega-m", type=float)
    parser.add_argument("--omega-s0", type=float)
    parser.add_argument("--wt", type=float)
    args = parser.parse_args(argv)
    summary = run_scan(_repo_root() / args.protocol, _repo_root() / args.out_dir, args)
    print(json.dumps(summary["assessment"], indent=2))


if __name__ == "__main__":
    main()
