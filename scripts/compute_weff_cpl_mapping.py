#!/usr/bin/env python3
"""Compute a claim-blocked RLL w_eff(z) to CPL target mapping.

The script is deterministic, dependency-light, and fail-closed: it produces a
mapping artifact and falsifier gates, not a scientific claim.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
from typing import Iterable

Z_TARGET = (0.295, 0.510, 0.706, 0.934, 1.321, 1.484)
W_TARGET = (-0.671, -0.558, -0.459, -0.354, -0.210, -0.156)
Z_TABLE = (0.000, 0.100, 0.295, 0.510, 0.706, 0.934, 1.000, 1.321, 1.484, 2.330)
W_TABLE = (-0.838, -0.776, -0.671, -0.558, -0.459, -0.354, -0.328, -0.210, -0.156, 0.055)


def transition_f(z: float, zt: float, wt: float) -> float:
    return 1.0 / (1.0 + math.exp(max(-700.0, min(700.0, (z - zt) / wt))))


def rho_sector(z: float, zt: float, wt: float) -> float:
    a = 1.0 / (1.0 + z)
    fz = transition_f(z, zt, wt)
    return fz + (1.0 - fz) * a ** -3


def d_rho_d_lna(z: float, zt: float, wt: float, h: float = 1e-5) -> float:
    a = 1.0 / (1.0 + z)
    x = math.log(a)

    def at_log_scale(log_a: float) -> float:
        aa = math.exp(log_a)
        zz = 1.0 / aa - 1.0
        ff = transition_f(zz, zt, wt)
        return ff + (1.0 - ff) * aa ** -3

    return (at_log_scale(x + h) - at_log_scale(x - h)) / (2.0 * h)


def weff(z: float, zt: float, wt: float) -> float:
    density = rho_sector(z, zt, wt)
    return -1.0 - d_rho_d_lna(z, zt, wt) / (3.0 * density)


def cpl_w(z: float, w0: float, wa: float) -> float:
    """User-seeded target convention: w(z)=w0-wa*z/(1+z).

    The sign is intentionally kept to reproduce the supplied mapping table;
    official DESI convention/table values remain claim-blocked until ingested.
    """
    return w0 - wa * z / (1.0 + z)


def chi2_vs_cpl(zt: float, wt: float, sigma: float, w0: float, wa: float) -> float:
    return sum(((weff(z, zt, wt) - wc) / sigma) ** 2 for z, wc in zip(Z_TARGET, W_TARGET))


def monotonic_nonincreasing(values: Iterable[float]) -> bool:
    seq = list(values)
    return all(left >= right for left, right in zip(seq, seq[1:]))


def scan(args: argparse.Namespace) -> tuple[dict[str, float], list[dict[str, float]]]:
    rows: list[dict[str, float]] = []
    best: dict[str, float] | None = None
    zt_steps = int(round((args.zt_max - args.zt_min) / args.zt_step)) + 1
    wt_steps = int(round((args.wt_max - args.wt_min) / args.wt_step)) + 1
    for zt_i in range(zt_steps):
        zt = round(args.zt_min + zt_i * args.zt_step, 10)
        for wt_i in range(wt_steps):
            wt = round(args.wt_min + wt_i * args.wt_step, 10)
            chi2 = chi2_vs_cpl(zt, wt, args.sigma, args.w0, args.wa)
            row = {"zt": zt, "wt": wt, "chi2_weff_vs_cpl": chi2, "w_eff_z0": weff(0.0, zt, wt)}
            rows.append(row)
            if best is None or chi2 < best["chi2_weff_vs_cpl"]:
                best = row
    assert best is not None
    return best, rows


def write_csv(path: Path, rows: list[dict[str, float]], args: argparse.Namespace) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["z", "w_eff_seed", "f_z_seed", "w_cpl_target"])
        for z, wc in zip(Z_TABLE, W_TABLE):
            writer.writerow([z, weff(z, args.seed_zt, args.seed_wt), transition_f(z, args.seed_zt, args.seed_wt), wc])


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-csv", default="results/weff_cpl_plane_rll.csv")
    parser.add_argument("--out-json", default="results/weff_cpl_plane_rll_summary.json")
    parser.add_argument("--w0", type=float, default=-0.838)
    parser.add_argument("--wa", type=float, default=-0.62)
    parser.add_argument("--sigma", type=float, default=0.05)
    parser.add_argument("--seed-zt", type=float, default=1.0)
    parser.add_argument("--seed-wt", type=float, default=0.3)
    parser.add_argument("--zt-min", type=float, default=0.3)
    parser.add_argument("--zt-max", type=float, default=1.4)
    parser.add_argument("--zt-step", type=float, default=0.1)
    parser.add_argument("--wt-min", type=float, default=0.1)
    parser.add_argument("--wt-max", type=float, default=0.55)
    parser.add_argument("--wt-step", type=float, default=0.05)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    best, scan_rows = scan(args)
    write_csv(Path(args.out_csv), scan_rows, args)
    seed_values = [weff(z, args.seed_zt, args.seed_wt) for z in Z_TARGET if z <= args.seed_zt]
    best_values = [weff(z, best["zt"], best["wt"]) for z in Z_TARGET if z <= best["zt"]]
    falsifiers = {
        "F_WEFF_01": best["chi2_weff_vs_cpl"] < 10.0,
        "F_WEFF_02": best["w_eff_z0"] < -0.7,
        "F_WEFF_03": monotonic_nonincreasing(best_values),
    }
    summary = {
        "schema_version": "1.0",
        "module": "weff_cpl_plane_mapping",
        "claim_allowed": False,
        "target_boundary": "User-provided CPL target; exact official DESI table row remains TOKEN_VAZIO until ingested.",
        "target": {"w0_seed": args.w0, "wa_seed": args.wa, "sigma_assumed": args.sigma, "values": dict(zip(map(str, Z_TARGET), W_TARGET)), "convention": "user-provided table values; official DESI table remains TOKEN_VAZIO"},
        "seed": {"zt": args.seed_zt, "wt": args.seed_wt, "monotonic_z0_to_zt": monotonic_nonincreasing(seed_values)},
        "best_scan": best,
        "n_scan_points": len(scan_rows),
        "falsifiers": falsifiers,
        "status": "candidate_mapping_passed" if all(falsifiers.values()) else "claim_blocked_falsifier_failed",
        "rollback": "Remove generated CSV/JSON or git revert; no raw data is changed.",
    }
    out = Path(args.out_json)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps({"best_scan": best, "falsifiers": falsifiers, "status": summary["status"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
