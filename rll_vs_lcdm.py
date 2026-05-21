#!/usr/bin/env python3
"""RLL vs ΛCDM comparator with H(z) + BAO D_V/r_s.

References (baseline context)
- DESI BAO program (DR2-era constraints)
- Planck 2018 cosmological parameters (A&A 641, A6, 2020)
- Pantheon+ (SNe Ia; integration planned in next pipeline step)

This script keeps GR/ΛCDM as null hypothesis and compares a CPL-like
RLL effective extension using chi2/AIC/BIC with explicit parameter penalty.
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


def _first_present(cols: dict[str, str], options: list[str], fallback_index: int) -> str:
    for o in options:
        if o in cols:
            return cols[o]
    return list(cols.values())[fallback_index]


def load_hz(path: Path) -> list[DataPoint]:
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cols = {c.lower(): c for c in (reader.fieldnames or [])}
        zc = _first_present(cols, ["z", "z_eff"], 0)
        hc = _first_present(cols, ["h", "hz", "h_obs"], 1)
        sc = _first_present(cols, ["sigma_h", "sigma", "err"], 2)
        return [DataPoint(_safe_float(r[zc]), _safe_float(r[hc]), _safe_float(r[sc], 10.0)) for r in reader]


def load_bao(path: Path) -> list[DataPoint]:
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cols = {c.lower(): c for c in (reader.fieldnames or [])}
        zc = _first_present(cols, ["z", "z_eff"], 0)
        vc = _first_present(cols, ["dv_over_rs", "dvrs", "value"], 1)
        sc = _first_present(cols, ["sigma", "err"], 2)
        return [DataPoint(_safe_float(r[zc]), _safe_float(r[vc]), _safe_float(r[sc], 0.1)) for r in reader]


def e_lcdm(z: float, om: float) -> float:
    return math.sqrt(om * (1 + z) ** 3 + (1 - om))


def e_rll(z: float, om: float, w0: float, wa: float) -> float:
    de = (1 + z) ** (3 * (1 + w0 + wa)) * math.exp(-3 * wa * z / (1 + z))
    return math.sqrt(om * (1 + z) ** 3 + (1 - om) * de)


def h_model(z: float, h0: float, model: str, om: float, w0: float, wa: float) -> float:
    return h0 * (e_lcdm(z, om) if model == "lcdm" else e_rll(z, om, w0, wa))


def _simpson_integral(func, a: float, b: float, n: int = 600) -> float:
    if b <= a:
        return 0.0
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    s = func(a) + func(b)
    for i in range(1, n):
        x = a + i * h
        s += (4 if i % 2 else 2) * func(x)
    return s * h / 3.0


def d_c(z: float, h0: float, model: str, om: float, w0: float, wa: float) -> float:
    integ = _simpson_integral(lambda zp: 1.0 / h_model(zp, h0, model, om, w0, wa), 0.0, z)
    return C_KM_S * integ


def dv_over_rs_model(z: float, h0: float, model: str, om: float, w0: float, wa: float, rs_drag: float) -> float:
    dc = d_c(z, h0, model, om, w0, wa)
    da = dc / (1 + z)
    hz = h_model(z, h0, model, om, w0, wa)
    dv = ((1 + z) ** 2 * da * da * C_KM_S * z / hz) ** (1 / 3)
    return dv / rs_drag


def chi2_hz(data: Iterable[DataPoint], *, h0: float, model: str, om: float, w0: float, wa: float) -> float:
    return sum(((p.value - h_model(p.z, h0, model, om, w0, wa)) / p.sigma) ** 2 for p in data)


def chi2_bao(data: Iterable[DataPoint], *, h0: float, model: str, om: float, w0: float, wa: float, rs_drag: float) -> float:
    return sum(((p.value - dv_over_rs_model(p.z, h0, model, om, w0, wa, rs_drag)) / p.sigma) ** 2 for p in data)


def aic(k: int, chisq: float) -> float:
    return 2 * k + chisq


def bic(k: int, n: int, chisq: float) -> float:
    return math.log(max(n, 1)) * k + chisq


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hz", default="data/real/Hz_data_real.csv")
    ap.add_argument("--bao", default="data/real/BAO_data_real.csv")
    ap.add_argument("--out-csv", default="results/rll_vs_lcdm_predictions.csv")
    ap.add_argument("--out-json", default="results/rll_vs_lcdm_summary.json")
    ap.add_argument("--h0", type=float, default=67.4)
    ap.add_argument("--omega-m", type=float, default=0.315)
    ap.add_argument("--w0", type=float, default=-0.95)
    ap.add_argument("--wa", type=float, default=-0.2)
    ap.add_argument("--rs-drag", type=float, default=147.0)
    args = ap.parse_args()

    hz_data = load_hz(Path(args.hz))
    bao_data = load_bao(Path(args.bao))

    c_h_l = chi2_hz(hz_data, h0=args.h0, model="lcdm", om=args.omega_m, w0=-1.0, wa=0.0)
    c_h_r = chi2_hz(hz_data, h0=args.h0, model="rll", om=args.omega_m, w0=args.w0, wa=args.wa)
    c_b_l = chi2_bao(bao_data, h0=args.h0, model="lcdm", om=args.omega_m, w0=-1.0, wa=0.0, rs_drag=args.rs_drag)
    c_b_r = chi2_bao(bao_data, h0=args.h0, model="rll", om=args.omega_m, w0=args.w0, wa=args.wa, rs_drag=args.rs_drag)
    c_lcdm, c_rll = c_h_l + c_b_l, c_h_r + c_b_r

    n = len(hz_data) + len(bao_data)
    k_lcdm, k_rll = 3, 5  # + r_s for BAO block

    summary = {
        "input": {"hz": args.hz, "bao": args.bao, "n_hz": len(hz_data), "n_bao": len(bao_data), "n_total": n},
        "params": {
            "lcdm": {"H0": args.h0, "Omega_m": args.omega_m, "w0": -1.0, "wa": 0.0, "r_s": args.rs_drag},
            "rll": {"H0": args.h0, "Omega_m": args.omega_m, "w0": args.w0, "wa": args.wa, "r_s": args.rs_drag},
        },
        "metrics": {
            "chi2_hz_lcdm": c_h_l,
            "chi2_hz_rll": c_h_r,
            "chi2_bao_lcdm": c_b_l,
            "chi2_bao_rll": c_b_r,
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
        w.writerow(["dataset", "z", "obs", "sigma", "lcdm_pred", "rll_pred", "eps_lcdm", "eps_rll"])
        for p in hz_data:
            hl = h_model(p.z, args.h0, "lcdm", args.omega_m, -1.0, 0.0)
            hr = h_model(p.z, args.h0, "rll", args.omega_m, args.w0, args.wa)
            w.writerow(["Hz", p.z, p.value, p.sigma, hl, hr, p.value - hl, p.value - hr])
        for p in bao_data:
            bl = dv_over_rs_model(p.z, args.h0, "lcdm", args.omega_m, -1.0, 0.0, args.rs_drag)
            br = dv_over_rs_model(p.z, args.h0, "rll", args.omega_m, args.w0, args.wa, args.rs_drag)
            w.writerow(["BAO_DVrs", p.z, p.value, p.sigma, bl, br, p.value - bl, p.value - br])

    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary["metrics"], indent=2))


if __name__ == "__main__":
    main()
