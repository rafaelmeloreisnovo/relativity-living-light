#!/usr/bin/env python3
"""RLL vs ΛCDM comparator with H(z) + BAO distance observables.

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
from typing import Iterable, Sequence

C_KM_S = 299792.458
DEFAULT_BAO_PATH = "data/real/cosmology/desi_dr2_bao_primary_points.csv"
DEFAULT_BAO_COVARIANCE_PATH = "data/real/cosmology/desi_dr2_bao_covariance_summary.csv"
LEGACY_BAO_PATH = "data/real/BAO_data_real.csv"
BAO_FORMATS = ("auto", "legacy_dv", "desi_dr2_primary")
BAO_DV_OBSERVABLES = {"DV_over_rd", "DV_over_rs"}
BAO_DM_OBSERVABLE = "DM_over_rd"
BAO_DH_OBSERVABLE = "DH_over_rd"


@dataclass
class DataPoint:
    z: float
    value: float
    sigma: float


@dataclass
class BaoPoint(DataPoint):
    observable: str = "DV_over_rd"
    tracer: str = ""
    release: str = ""
    covariance_block: str = ""


@dataclass(frozen=True)
class BaoCovarianceBlock:
    covariance_block: str
    tracer: str
    z: float
    observable_a: str
    sigma_a: float
    observable_b: str
    sigma_b: float
    correlation_coefficient: float
    covariance: float


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


def _normalise_observable(observable: str) -> str:
    aliases = {
        "dv_over_rs": "DV_over_rd",
        "dvrs": "DV_over_rd",
        "dv_over_rd": "DV_over_rd",
        "dm_over_rd": "DM_over_rd",
        "dh_over_rd": "DH_over_rd",
    }
    key = observable.strip().lower()
    return aliases.get(key, observable.strip())


def load_hz(path: Path) -> list[DataPoint]:
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cols = {c.lower(): c for c in (reader.fieldnames or [])}
        zc = _first_present(cols, ["z", "z_eff"], 0)
        hc = _first_present(cols, ["h", "hz", "h_obs"], 1)
        sc = _first_present(cols, ["sigma_h", "sigma", "err"], 2)
        return [DataPoint(_safe_float(r[zc]), _safe_float(r[hc]), _safe_float(r[sc], 10.0)) for r in reader]


def _detect_bao_format(cols: dict[str, str]) -> str:
    required = {"z_eff", "observable", "value", "sigma", "tracer", "release"}
    if required.issubset(cols):
        return "desi_dr2_primary"
    return "legacy_dv"


def load_bao(path: Path, *, bao_format: str = "auto") -> list[BaoPoint]:
    """Load BAO observations from either DESI DR2 primary or legacy DV tables."""
    if bao_format not in BAO_FORMATS:
        raise ValueError(f"Unsupported BAO format {bao_format!r}; expected one of {BAO_FORMATS}")

    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cols = {c.lower(): c for c in (reader.fieldnames or [])}
        resolved_format = _detect_bao_format(cols) if bao_format == "auto" else bao_format

        if resolved_format == "desi_dr2_primary":
            zc = _first_present(cols, ["z_eff", "z"], 2)
            oc = _first_present(cols, ["observable"], 3)
            vc = _first_present(cols, ["value"], 4)
            sc = _first_present(cols, ["sigma", "err"], 5)
            tc = _first_present(cols, ["tracer", "survey"], 1)
            rc = _first_present(cols, ["release"], 0)
            bc = cols.get("covariance_block")
            return [
                BaoPoint(
                    z=_safe_float(r[zc]),
                    value=_safe_float(r[vc]),
                    sigma=_safe_float(r[sc], 0.1),
                    observable=_normalise_observable(r[oc]),
                    tracer=r.get(tc, ""),
                    release=r.get(rc, ""),
                    covariance_block=r.get(bc, "") if bc else "",
                )
                for r in reader
            ]

        zc = _first_present(cols, ["z", "z_eff"], 0)
        vc = _first_present(cols, ["dv_over_rs", "dvrs", "dv_over_rd", "value"], 1)
        sc = _first_present(cols, ["sigma", "err"], 2)
        tc = cols.get("survey") or cols.get("tracer")
        return [
            BaoPoint(
                z=_safe_float(r[zc]),
                value=_safe_float(r[vc]),
                sigma=_safe_float(r[sc], 0.1),
                observable="DV_over_rd",
                tracer=r.get(tc, "") if tc else "",
                release="legacy_dv",
            )
            for r in reader
        ]


def load_bao_covariance_summary(path: Path) -> dict[str, BaoCovarianceBlock]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        blocks: dict[str, BaoCovarianceBlock] = {}
        for r in reader:
            block = BaoCovarianceBlock(
                covariance_block=r["covariance_block"],
                tracer=r.get("tracer", ""),
                z=_safe_float(r.get("z_eff", "0")),
                observable_a=_normalise_observable(r["observable_a"]),
                sigma_a=_safe_float(r["sigma_a"]),
                observable_b=_normalise_observable(r["observable_b"]),
                sigma_b=_safe_float(r["sigma_b"]),
                correlation_coefficient=_safe_float(r["correlation_coefficient"]),
                covariance=_safe_float(r["covariance"]),
            )
            blocks[block.covariance_block] = block
        return blocks


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


def dm_over_rd_model(z: float, h0: float, model: str, om: float, w0: float, wa: float, rs_drag: float) -> float:
    return d_c(z, h0, model, om, w0, wa) / rs_drag


def dh_over_rd_model(z: float, h0: float, model: str, om: float, w0: float, wa: float, rs_drag: float) -> float:
    return C_KM_S / h_model(z, h0, model, om, w0, wa) / rs_drag


def dv_over_rd_model(z: float, h0: float, model: str, om: float, w0: float, wa: float, rs_drag: float) -> float:
    dm = dm_over_rd_model(z, h0, model, om, w0, wa, rs_drag)
    dh = dh_over_rd_model(z, h0, model, om, w0, wa, rs_drag)
    return (z * dm * dm * dh) ** (1 / 3)


def dv_over_rs_model(z: float, h0: float, model: str, om: float, w0: float, wa: float, rs_drag: float) -> float:
    """Backward-compatible alias for the legacy BAO naming convention."""
    return dv_over_rd_model(z, h0, model, om, w0, wa, rs_drag)


def bao_model_value(p: BaoPoint, *, h0: float, model: str, om: float, w0: float, wa: float, rs_drag: float) -> float:
    if p.observable in BAO_DV_OBSERVABLES:
        return dv_over_rd_model(p.z, h0, model, om, w0, wa, rs_drag)
    if p.observable == BAO_DM_OBSERVABLE:
        return dm_over_rd_model(p.z, h0, model, om, w0, wa, rs_drag)
    if p.observable == BAO_DH_OBSERVABLE:
        return dh_over_rd_model(p.z, h0, model, om, w0, wa, rs_drag)
    raise ValueError(f"Unsupported BAO observable {p.observable!r}")


def chi2_hz(data: Iterable[DataPoint], *, h0: float, model: str, om: float, w0: float, wa: float) -> float:
    return sum(((p.value - h_model(p.z, h0, model, om, w0, wa)) / p.sigma) ** 2 for p in data)


def _chi2_correlated_pair(r1: float, r2: float, sigma1: float, sigma2: float, covariance: float) -> float:
    det = sigma1 * sigma1 * sigma2 * sigma2 - covariance * covariance
    if det <= 0.0:
        raise ValueError("Invalid non-positive BAO covariance determinant")
    return (sigma2 * sigma2 * r1 * r1 - 2.0 * covariance * r1 * r2 + sigma1 * sigma1 * r2 * r2) / det


def chi2_bao(
    data: Sequence[BaoPoint],
    *,
    h0: float,
    model: str,
    om: float,
    w0: float,
    wa: float,
    rs_drag: float,
    covariance_blocks: dict[str, BaoCovarianceBlock] | None = None,
) -> float:
    covariance_blocks = covariance_blocks or {}
    by_block: dict[str, list[BaoPoint]] = {}
    chi2 = 0.0

    for p in data:
        if p.observable in {BAO_DM_OBSERVABLE, BAO_DH_OBSERVABLE} and p.covariance_block in covariance_blocks:
            by_block.setdefault(p.covariance_block, []).append(p)
        else:
            pred = bao_model_value(p, h0=h0, model=model, om=om, w0=w0, wa=wa, rs_drag=rs_drag)
            chi2 += ((p.value - pred) / p.sigma) ** 2

    for block_name, points in by_block.items():
        if len(points) != 2:
            for p in points:
                pred = bao_model_value(p, h0=h0, model=model, om=om, w0=w0, wa=wa, rs_drag=rs_drag)
                chi2 += ((p.value - pred) / p.sigma) ** 2
            continue
        point_by_observable = {p.observable: p for p in points}
        block = covariance_blocks[block_name]
        try:
            pa = point_by_observable[block.observable_a]
            pb = point_by_observable[block.observable_b]
        except KeyError:
            for p in points:
                pred = bao_model_value(p, h0=h0, model=model, om=om, w0=w0, wa=wa, rs_drag=rs_drag)
                chi2 += ((p.value - pred) / p.sigma) ** 2
            continue
        pred_a = bao_model_value(pa, h0=h0, model=model, om=om, w0=w0, wa=wa, rs_drag=rs_drag)
        pred_b = bao_model_value(pb, h0=h0, model=model, om=om, w0=w0, wa=wa, rs_drag=rs_drag)
        chi2 += _chi2_correlated_pair(pa.value - pred_a, pb.value - pred_b, pa.sigma, pb.sigma, block.covariance)

    return chi2


def aic(k: int, chisq: float) -> float:
    return 2 * k + chisq


def bic(k: int, n: int, chisq: float) -> float:
    return math.log(max(n, 1)) * k + chisq


def build_arg_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hz", default="data/real/Hz_data_real.csv")
    ap.add_argument("--bao", default=DEFAULT_BAO_PATH)
    ap.add_argument("--bao-format", choices=BAO_FORMATS, default="auto")
    ap.add_argument("--bao-covariance", default=DEFAULT_BAO_COVARIANCE_PATH)
    ap.add_argument("--bao-diagonal", action="store_true", help="Ignore BAO covariance summary and use diagonal errors only.")
    ap.add_argument("--out-csv", default="results/rll_vs_lcdm_predictions.csv")
    ap.add_argument("--out-json", default="results/rll_vs_lcdm_summary.json")
    ap.add_argument("--h0", type=float, default=67.4)
    ap.add_argument("--omega-m", type=float, default=0.315)
    ap.add_argument("--w0", type=float, default=-0.95)
    ap.add_argument("--wa", type=float, default=-0.2)
    ap.add_argument("--rs-drag", type=float, default=147.0)
    return ap


def _bao_covariance_mode(data: Sequence[BaoPoint], covariance_blocks: dict[str, BaoCovarianceBlock], diagonal: bool) -> dict[str, object]:
    correlated_blocks = sorted({p.covariance_block for p in data if p.covariance_block in covariance_blocks})
    missing_blocks = sorted(
        {
            p.covariance_block
            for p in data
            if p.observable in {BAO_DM_OBSERVABLE, BAO_DH_OBSERVABLE} and p.covariance_block and p.covariance_block not in covariance_blocks
        }
    )
    mode = "diagonal" if diagonal or not correlated_blocks else "block_covariance_summary"
    return {
        "mode": mode,
        "path": None if diagonal else DEFAULT_BAO_COVARIANCE_PATH,
        "correlated_blocks": correlated_blocks,
        "n_correlated_blocks": len(correlated_blocks),
        "diagonal_approximation": diagonal or bool(missing_blocks),
        "missing_covariance_blocks": missing_blocks,
    }


def main(argv: Sequence[str] | None = None) -> None:
    ap = build_arg_parser()
    args = ap.parse_args(argv)

    hz_data = load_hz(Path(args.hz))
    bao_data = load_bao(Path(args.bao), bao_format=args.bao_format)
    covariance_blocks = {} if args.bao_diagonal else load_bao_covariance_summary(Path(args.bao_covariance))

    c_h_l = chi2_hz(hz_data, h0=args.h0, model="lcdm", om=args.omega_m, w0=-1.0, wa=0.0)
    c_h_r = chi2_hz(hz_data, h0=args.h0, model="rll", om=args.omega_m, w0=args.w0, wa=args.wa)
    c_b_l = chi2_bao(bao_data, h0=args.h0, model="lcdm", om=args.omega_m, w0=-1.0, wa=0.0, rs_drag=args.rs_drag, covariance_blocks=covariance_blocks)
    c_b_r = chi2_bao(bao_data, h0=args.h0, model="rll", om=args.omega_m, w0=args.w0, wa=args.wa, rs_drag=args.rs_drag, covariance_blocks=covariance_blocks)
    c_lcdm, c_rll = c_h_l + c_b_l, c_h_r + c_b_r

    n = len(hz_data) + len(bao_data)
    k_lcdm, k_rll = 3, 5  # H0, Omega_m, r_s vs H0, Omega_m, w0, wa, r_s

    covariance_info = _bao_covariance_mode(bao_data, covariance_blocks, args.bao_diagonal)
    covariance_info["path"] = None if args.bao_diagonal else args.bao_covariance
    summary = {
        "input": {
            "hz": args.hz,
            "bao": args.bao,
            "bao_format": args.bao_format,
            "n_hz": len(hz_data),
            "n_bao": len(bao_data),
            "n_total": n,
        },
        "bao_covariance": covariance_info,
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
        w.writerow(["dataset", "tracer", "release", "observable", "z", "obs", "sigma", "lcdm_pred", "rll_pred", "eps_lcdm", "eps_rll"])
        for p in hz_data:
            hl = h_model(p.z, args.h0, "lcdm", args.omega_m, -1.0, 0.0)
            hr = h_model(p.z, args.h0, "rll", args.omega_m, args.w0, args.wa)
            w.writerow(["Hz", "", "", "H", p.z, p.value, p.sigma, hl, hr, p.value - hl, p.value - hr])
        for p in bao_data:
            bl = bao_model_value(p, h0=args.h0, model="lcdm", om=args.omega_m, w0=-1.0, wa=0.0, rs_drag=args.rs_drag)
            br = bao_model_value(p, h0=args.h0, model="rll", om=args.omega_m, w0=args.w0, wa=args.wa, rs_drag=args.rs_drag)
            w.writerow(["BAO", p.tracer, p.release, p.observable, p.z, p.value, p.sigma, bl, br, p.value - bl, p.value - br])

    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary["metrics"], indent=2))


if __name__ == "__main__":
    main()
