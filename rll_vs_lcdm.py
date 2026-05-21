#!/usr/bin/env python3
"""RLL vs ΛCDM baseline comparator.

Purpose
-------
Compute a reproducible, falsifiable first-pass comparison using local public-like
artifacts already committed in this repository.

Inputs (default)
----------------
- data/real/Hz_data_real.csv
- data/real/BAO_data_real.csv

Outputs
-------
- results/rll_vs_lcdm_predictions.csv
- results/rll_vs_lcdm_summary.json

Notes
-----
This script is intentionally conservative: it does not claim discovery and treats
RLL as an extension that must beat ΛCDM under AIC/BIC penalties.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

C_KM_S = 299792.458


@dataclass
class DataPoint:
    z: float
    value: float
    sigma: float


def _safe_float(text: str, default: float | None = None) -> float:
    try:
        return float(text)
    except Exception:
        if default is None:
            raise
        return default


def load_hz(path: Path) -> list[DataPoint]:
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cols = {c.lower(): c for c in (reader.fieldnames or [])}
        zc = cols.get("z", list(cols.values())[0])
        hc = cols.get("h", cols.get("hz", list(cols.values())[1]))
        sc = cols.get("sigma_h", cols.get("sigma", cols.get("err", list(cols.values())[-1])))
        out = []
        for row in reader:
            out.append(DataPoint(_safe_float(row[zc]), _safe_float(row[hc]), _safe_float(row[sc], 10.0)))
        return out


def e_lcdm(z: float, om: float) -> float:
    return math.sqrt(om * (1 + z) ** 3 + (1 - om))


def e_rll(z: float, om: float, w0: float, wa: float) -> float:
    # CPL-like effective EOS mapping for a first falsifiability pass.
    a = 1.0 / (1.0 + z)
    de = (1 + z) ** (3 * (1 + w0 + wa)) * math.exp(-3 * wa * z / (1 + z))
    return math.sqrt(om * (1 + z) ** 3 + (1 - om) * de)


def h_model(z: float, h0: float, model: str, om: float, w0: float, wa: float) -> float:
    if model == "lcdm":
        return h0 * e_lcdm(z, om)
    return h0 * e_rll(z, om, w0, wa)


def chi2(data: Iterable[DataPoint], *, h0: float, model: str, om: float, w0: float, wa: float) -> float:
    total = 0.0
    for p in data:
        pred = h_model(p.z, h0, model, om, w0, wa)
        total += ((p.value - pred) / p.sigma) ** 2
    return total


def aic(k: int, chisq: float) -> float:
    return 2 * k + chisq


def bic(k: int, n: int, chisq: float) -> float:
    return math.log(max(n, 1)) * k + chisq


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hz", default="data/real/Hz_data_real.csv")
    ap.add_argument("--out-csv", default="results/rll_vs_lcdm_predictions.csv")
    ap.add_argument("--out-json", default="results/rll_vs_lcdm_summary.json")
    ap.add_argument("--h0", type=float, default=67.4)
    ap.add_argument("--omega-m", type=float, default=0.315)
    ap.add_argument("--w0", type=float, default=-0.95)
    ap.add_argument("--wa", type=float, default=-0.2)
    args = ap.parse_args()

    hz_data = load_hz(Path(args.hz))

    c_lcdm = chi2(hz_data, h0=args.h0, model="lcdm", om=args.omega_m, w0=-1.0, wa=0.0)
    c_rll = chi2(hz_data, h0=args.h0, model="rll", om=args.omega_m, w0=args.w0, wa=args.wa)

    n = len(hz_data)
    k_lcdm = 2  # H0, Omega_m
    k_rll = 4  # H0, Omega_m, w0, wa

    summary = {
        "input": {"hz": args.hz, "n_hz": n},
        "params": {
            "lcdm": {"H0": args.h0, "Omega_m": args.omega_m, "w0": -1.0, "wa": 0.0},
            "rll": {"H0": args.h0, "Omega_m": args.omega_m, "w0": args.w0, "wa": args.wa},
        },
        "metrics": {
            "chi2_lcdm": c_lcdm,
            "chi2_rll": c_rll,
            "delta_chi2": c_rll - c_lcdm,
            "aic_lcdm": aic(k_lcdm, c_lcdm),
            "aic_rll": aic(k_rll, c_rll),
            "bic_lcdm": bic(k_lcdm, n, c_lcdm),
            "bic_rll": bic(k_rll, n, c_rll),
        },
    }

    out_csv = Path(args.out_csv)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["z", "H_obs", "sigma_H", "H_lcdm", "H_rll", "eps_lcdm", "eps_rll"])
        for p in hz_data:
            hl = h_model(p.z, args.h0, "lcdm", args.omega_m, -1.0, 0.0)
            hr = h_model(p.z, args.h0, "rll", args.omega_m, args.w0, args.wa)
            w.writerow([p.z, p.value, p.sigma, hl, hr, p.value - hl, p.value - hr])

    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(json.dumps(summary["metrics"], indent=2))


if __name__ == "__main__":
    main()
