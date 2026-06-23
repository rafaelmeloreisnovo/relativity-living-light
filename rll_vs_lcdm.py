#!/usr/bin/env python3
"""RLL model-selection comparator for H(z)+BAO.

Models:
- lcdm: ΛCDM null baseline.
- w0wa: CPL/w0waCDM adversary.
- rll: logistic Relativity Living Light background sector.

Bayes output is a BIC/Schwarz approximation, not nested-sampling evidence.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
from typing import Iterable, Sequence

C_KM_S = 299792.458
DEFAULT_BAO_PATH = "data/real/cosmology/desi_dr2_bao_primary_points.csv"
DEFAULT_BAO_COVARIANCE_PATH = "data/real/cosmology/desi_dr2_bao_covariance_summary.csv"
BAO_FORMATS = ("auto", "legacy_dv", "desi_dr2_primary")
ADVERSARY_CHOICES = ("lcdm", "w0wa", "w0waCDM", "both")
BAO_DV = {"DV_over_rd", "DV_over_rs"}
BAO_DM = "DM_over_rd"
BAO_DH = "DH_over_rd"


def _safe_float(text: str, default: float | None = None) -> float:
    try:
        return float(text)
    except Exception:
        if default is None:
            raise
        return default


def _first(cols: dict[str, str], options: list[str], fallback_index: int) -> str:
    for opt in options:
        if opt in cols:
            return cols[opt]
    return list(cols.values())[fallback_index]


def _obs(name: str) -> str:
    aliases = {
        "dv_over_rs": "DV_over_rd",
        "dvrs": "DV_over_rd",
        "dv_over_rd": "DV_over_rd",
        "dm_over_rd": "DM_over_rd",
        "dh_over_rd": "DH_over_rd",
    }
    key = name.strip().lower()
    return aliases.get(key, name.strip())


def _adversary(value: str) -> str:
    return "w0wa" if value == "w0waCDM" else value


def load_hz(path: Path) -> list[dict[str, float]]:
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cols = {c.lower(): c for c in (reader.fieldnames or [])}
        zc = _first(cols, ["z", "z_eff"], 0)
        hc = _first(cols, ["h", "hz", "h_obs"], 1)
        sc = _first(cols, ["sigma_h", "sigma", "err"], 2)
        return [{"z": _safe_float(r[zc]), "value": _safe_float(r[hc]), "sigma": _safe_float(r[sc], 10.0)} for r in reader]


def _detect_bao(cols: dict[str, str]) -> str:
    return "desi_dr2_primary" if {"z_eff", "observable", "value", "sigma", "tracer", "release"}.issubset(cols) else "legacy_dv"


def load_bao(path: Path, *, bao_format: str = "auto") -> list[dict[str, object]]:
    if bao_format not in BAO_FORMATS:
        raise ValueError(f"Unsupported BAO format {bao_format!r}")
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cols = {c.lower(): c for c in (reader.fieldnames or [])}
        fmt = _detect_bao(cols) if bao_format == "auto" else bao_format
        if fmt == "desi_dr2_primary":
            zc = _first(cols, ["z_eff", "z"], 2)
            oc = _first(cols, ["observable"], 3)
            vc = _first(cols, ["value"], 4)
            sc = _first(cols, ["sigma", "err"], 5)
            tc = _first(cols, ["tracer", "survey"], 1)
            rc = _first(cols, ["release"], 0)
            bc = cols.get("covariance_block")
            return [
                {
                    "z": _safe_float(r[zc]),
                    "value": _safe_float(r[vc]),
                    "sigma": _safe_float(r[sc], 0.1),
                    "observable": _obs(r[oc]),
                    "tracer": r.get(tc, ""),
                    "release": r.get(rc, ""),
                    "covariance_block": r.get(bc, "") if bc else "",
                }
                for r in reader
            ]
        zc = _first(cols, ["z", "z_eff"], 0)
        vc = _first(cols, ["dv_over_rs", "dvrs", "dv_over_rd", "value"], 1)
        sc = _first(cols, ["sigma", "err"], 2)
        tc = cols.get("survey") or cols.get("tracer")
        return [
            {
                "z": _safe_float(r[zc]),
                "value": _safe_float(r[vc]),
                "sigma": _safe_float(r[sc], 0.1),
                "observable": "DV_over_rd",
                "tracer": r.get(tc, "") if tc else "",
                "release": "legacy_dv",
                "covariance_block": "",
            }
            for r in reader
        ]


def load_bao_covariance_summary(path: Path) -> dict[str, dict[str, object]]:
    if not path.exists():
        return {}
    blocks: dict[str, dict[str, object]] = {}
    with path.open("r", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            blocks[r["covariance_block"]] = {
                "observable_a": _obs(r["observable_a"]),
                "observable_b": _obs(r["observable_b"]),
                "sigma_a": _safe_float(r["sigma_a"]),
                "sigma_b": _safe_float(r["sigma_b"]),
                "covariance": _safe_float(r["covariance"]),
            }
    return blocks


def _safe_exp(x: float) -> float:
    return math.exp(max(-700.0, min(700.0, x)))


def rll_transition_f(z: float, zt: float, wt: float) -> float:
    if wt <= 0.0:
        raise ValueError("RLL transition width wt must be positive")
    return 1.0 / (1.0 + _safe_exp((z - zt) / wt))


def e_lcdm(z: float, om: float) -> float:
    e2 = om * (1 + z) ** 3 + (1 - om)
    if e2 <= 0:
        raise ValueError(f"LCDM E² non-positive at z={z}: {e2}")
    return math.sqrt(e2)


def e_w0wa(z: float, om: float, w0: float, wa: float) -> float:
    de = (1 + z) ** (3 * (1 + w0 + wa)) * math.exp(-3 * wa * z / (1 + z))
    e2 = om * (1 + z) ** 3 + (1 - om) * de
    if e2 <= 0:
        raise ValueError(f"w0wa E² non-positive at z={z}: {e2}")
    return math.sqrt(e2)


def e_rll_logistic(z: float, om: float, omega_s0: float, zt: float, wt: float) -> float:
    """RLL logistic background: E²=Ωm(1+z)^3+ΩΛ+Ωs0[f+(1-f)(1+z)^3]."""
    if omega_s0 < 0:
        raise ValueError("omega_s0 must be non-negative")
    fz = rll_transition_f(z, zt, wt)
    omega_lambda = 1.0 - om - omega_s0
    e2 = om * (1 + z) ** 3 + omega_lambda + omega_s0 * (fz + (1 - fz) * (1 + z) ** 3)
    if e2 <= 0:
        raise ValueError(f"RLL E² non-positive at z={z}: {e2}")
    return math.sqrt(e2)


def model_params(model: str, args: argparse.Namespace) -> tuple[float, float, float, float, float]:
    if model == "lcdm":
        return -1.0, 0.0, 0.0, args.zt, args.wt
    if model == "w0wa":
        return args.w0, args.wa, 0.0, args.zt, args.wt
    if model == "rll":
        return -1.0, 0.0, args.omega_s0, args.zt, args.wt
    raise ValueError(f"Unsupported model {model!r}")


def h_model(z: float, h0: float, model: str, om: float, w0: float, wa: float, omega_s0: float, zt: float, wt: float) -> float:
    if model == "lcdm":
        return h0 * e_lcdm(z, om)
    if model == "w0wa":
        return h0 * e_w0wa(z, om, w0, wa)
    if model == "rll":
        return h0 * e_rll_logistic(z, om, omega_s0, zt, wt)
    raise ValueError(f"Unsupported model {model!r}")


def simpson(func, a: float, b: float, n: int = 600) -> float:
    if b <= a:
        return 0.0
    if n % 2:
        n += 1
    h = (b - a) / n
    s = func(a) + func(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * func(a + i * h)
    return s * h / 3.0


def d_c(z: float, args: argparse.Namespace, model: str) -> float:
    w0, wa, os0, zt, wt = model_params(model, args)
    return C_KM_S * simpson(lambda zp: 1.0 / h_model(zp, args.h0, model, args.omega_m, w0, wa, os0, zt, wt), 0.0, z)


def bao_pred(p: dict[str, object], args: argparse.Namespace, model: str) -> float:
    z = float(p["z"])
    w0, wa, os0, zt, wt = model_params(model, args)
    dm = d_c(z, args, model) / args.rs_drag
    dh = C_KM_S / h_model(z, args.h0, model, args.omega_m, w0, wa, os0, zt, wt) / args.rs_drag
    observable = str(p["observable"])
    if observable in BAO_DV:
        return (z * dm * dm * dh) ** (1 / 3)
    if observable == BAO_DM:
        return dm
    if observable == BAO_DH:
        return dh
    raise ValueError(f"Unsupported BAO observable {observable!r}")


def chi2_hz(data: Iterable[dict[str, float]], args: argparse.Namespace, model: str) -> float:
    w0, wa, os0, zt, wt = model_params(model, args)
    return sum(((p["value"] - h_model(p["z"], args.h0, model, args.omega_m, w0, wa, os0, zt, wt)) / p["sigma"]) ** 2 for p in data)


def _chi2_pair(r1: float, r2: float, s1: float, s2: float, cov: float) -> float:
    det = s1 * s1 * s2 * s2 - cov * cov
    if det <= 0:
        raise ValueError("Invalid BAO covariance determinant")
    return (s2 * s2 * r1 * r1 - 2.0 * cov * r1 * r2 + s1 * s1 * r2 * r2) / det


def chi2_bao(data: Sequence[dict[str, object]], args: argparse.Namespace, model: str, cov_blocks: dict[str, dict[str, object]]) -> float:
    chi2 = 0.0
    by_block: dict[str, list[dict[str, object]]] = {}
    for p in data:
        block = str(p.get("covariance_block", ""))
        if p["observable"] in {BAO_DM, BAO_DH} and block in cov_blocks:
            by_block.setdefault(block, []).append(p)
        else:
            pred = bao_pred(p, args, model)
            chi2 += ((float(p["value"]) - pred) / float(p["sigma"])) ** 2
    for block_name, points in by_block.items():
        if len(points) != 2:
            for p in points:
                pred = bao_pred(p, args, model)
                chi2 += ((float(p["value"]) - pred) / float(p["sigma"])) ** 2
            continue
        block = cov_blocks[block_name]
        by_obs = {str(p["observable"]): p for p in points}
        pa = by_obs.get(str(block["observable_a"]))
        pb = by_obs.get(str(block["observable_b"]))
        if pa is None or pb is None:
            for p in points:
                pred = bao_pred(p, args, model)
                chi2 += ((float(p["value"]) - pred) / float(p["sigma"])) ** 2
            continue
        chi2 += _chi2_pair(
            float(pa["value"]) - bao_pred(pa, args, model),
            float(pb["value"]) - bao_pred(pb, args, model),
            float(pa["sigma"]),
            float(pb["sigma"]),
            float(block["covariance"]),
        )
    return chi2


def aic(k: int, chi2: float) -> float:
    return chi2 + 2 * k


def bic(k: int, n: int, chi2: float) -> float:
    return chi2 + math.log(max(n, 1)) * k


def bayes_factor_from_bic(bic_candidate: float, bic_reference: float) -> float:
    exponent = 0.5 * (bic_reference - bic_candidate)
    if exponent > 700:
        return math.inf
    if exponent < -745:
        return 0.0
    return math.exp(exponent)


def k_params(model: str) -> int:
    return {"lcdm": 3, "w0wa": 5, "rll": 6}[model]


def ordered_models(adversary: str) -> list[str]:
    adversary = _adversary(adversary)
    if adversary == "lcdm":
        return ["lcdm", "rll"]
    if adversary in {"w0wa", "both"}:
        return ["lcdm", "w0wa", "rll"]
    raise ValueError(f"Unsupported adversary {adversary!r}")


def parameter_payload(model: str, args: argparse.Namespace) -> dict[str, float]:
    common = {"H0": args.h0, "Omega_m": args.omega_m, "r_s": args.rs_drag}
    if model == "lcdm":
        return {**common, "w0": -1.0, "wa": 0.0}
    if model == "w0wa":
        return {**common, "w0": args.w0, "wa": args.wa}
    return {**common, "Omega_s0": args.omega_s0, "Omega_Lambda_derived": 1 - args.omega_m - args.omega_s0, "z_t": args.zt, "w_t": args.wt}


def evaluate(model: str, hz: Sequence[dict[str, float]], bao: Sequence[dict[str, object]], args: argparse.Namespace, cov: dict[str, dict[str, object]]) -> dict[str, float | int]:
    ch = chi2_hz(hz, args, model)
    cb = chi2_bao(bao, args, model, cov)
    total = ch + cb
    k = k_params(model)
    n = len(hz) + len(bao)
    return {"chi2_hz": ch, "chi2_bao": cb, "chi2_total": total, "n_params": k, "aic": aic(k, total), "bic": bic(k, n, total)}


def comparisons(results: dict[str, dict[str, float | int]], with_bayes: bool) -> dict[str, float | str]:
    out: dict[str, float | str] = {}
    rll = results["rll"]
    for ref_name in ("lcdm", "w0wa"):
        if ref_name not in results:
            continue
        ref = results[ref_name]
        out[f"delta_chi2_rll_minus_{ref_name}"] = float(rll["chi2_total"]) - float(ref["chi2_total"])
        out[f"delta_aic_rll_minus_{ref_name}"] = float(rll["aic"]) - float(ref["aic"])
        out[f"delta_bic_rll_minus_{ref_name}"] = float(rll["bic"]) - float(ref["bic"])
        if with_bayes:
            out[f"bayes_factor_bic_approx_rll_over_{ref_name}"] = bayes_factor_from_bic(float(rll["bic"]), float(ref["bic"]))
    if with_bayes:
        out["bayes_method"] = "BIC/Schwarz approximation; TOKEN_VAZIO for full nested-sampling evidence"
    return out


def covariance_info(bao: Sequence[dict[str, object]], cov: dict[str, dict[str, object]], diagonal: bool, path: str) -> dict[str, object]:
    correlated = sorted({str(p["covariance_block"]) for p in bao if p.get("covariance_block") in cov})
    missing = sorted({str(p.get("covariance_block", "")) for p in bao if p["observable"] in {BAO_DM, BAO_DH} and p.get("covariance_block") and p.get("covariance_block") not in cov})
    return {
        "mode": "diagonal" if diagonal or not correlated else "block_covariance_summary",
        "path": None if diagonal else path,
        "correlated_blocks": correlated,
        "n_correlated_blocks": len(correlated),
        "diagonal_approximation": diagonal or bool(missing),
        "missing_covariance_blocks": missing,
    }


def growth_status(with_growth: bool) -> dict[str, object]:
    if not with_growth:
        return {"requested": False}
    return {
        "requested": True,
        "status": "TOKEN_VAZIO",
        "reason": "fσ8 growth integration is intentionally not fabricated in this point-evaluation script.",
        "next_step": "Implement δ(a), f=dlnδ/dlna, σ8(z), and BOSS/eBOSS fσ8 likelihood in a dedicated growth module.",
    }


def write_predictions(path: Path, hz: Sequence[dict[str, float]], bao: Sequence[dict[str, object]], models: Sequence[str], args: argparse.Namespace) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    header = ["dataset", "tracer", "release", "observable", "z", "obs", "sigma"]
    for model in models:
        header += [f"{model}_pred", f"{model}_resid"]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for p in hz:
            row: list[object] = ["Hz", "", "", "H", p["z"], p["value"], p["sigma"]]
            for model in models:
                w0, wa, os0, zt, wt = model_params(model, args)
                pred = h_model(p["z"], args.h0, model, args.omega_m, w0, wa, os0, zt, wt)
                row += [pred, p["value"] - pred]
            writer.writerow(row)
        for p in bao:
            row = ["BAO", p.get("tracer", ""), p.get("release", ""), p["observable"], p["z"], p["value"], p["sigma"]]
            for model in models:
                pred = bao_pred(p, args, model)
                row += [pred, float(p["value"]) - pred]
            writer.writerow(row)


def build_arg_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hz", default="data/real/Hz_data_real.csv")
    ap.add_argument("--bao", default=DEFAULT_BAO_PATH)
    ap.add_argument("--bao-format", choices=BAO_FORMATS, default="auto")
    ap.add_argument("--bao-covariance", default=DEFAULT_BAO_COVARIANCE_PATH)
    ap.add_argument("--bao-diagonal", action="store_true")
    ap.add_argument("--out-csv", default="results/rll_model_comparison_predictions.csv")
    ap.add_argument("--out-json", default="results/rll_model_comparison_summary.json")
    ap.add_argument("--adversary", choices=ADVERSARY_CHOICES, default="both")
    ap.add_argument("--with-bayes", action="store_true")
    ap.add_argument("--with-growth", action="store_true")
    ap.add_argument("--h0", type=float, default=67.4)
    ap.add_argument("--omega-m", type=float, default=0.315)
    ap.add_argument("--w0", type=float, default=-0.95, help="CPL/w0waCDM w0 parameter")
    ap.add_argument("--wa", type=float, default=-0.2, help="CPL/w0waCDM wa parameter")
    ap.add_argument("--omega-s0", type=float, default=0.059, help="RLL logistic Ω_s0")
    ap.add_argument("--zt", type=float, default=1.164, help="RLL logistic transition redshift")
    ap.add_argument("--wt", type=float, default=0.405, help="RLL logistic transition width; must be positive")
    ap.add_argument("--rs-drag", type=float, default=147.0)
    return ap


def main(argv: Sequence[str] | None = None) -> None:
    args = build_arg_parser().parse_args(argv)
    hz = load_hz(Path(args.hz))
    bao = load_bao(Path(args.bao), bao_format=args.bao_format)
    cov = {} if args.bao_diagonal else load_bao_covariance_summary(Path(args.bao_covariance))
    models = ordered_models(args.adversary)
    results = {model: evaluate(model, hz, bao, args, cov) for model in models}
    summary = {
        "input": {"hz": args.hz, "bao": args.bao, "bao_format": args.bao_format, "adversary": _adversary(args.adversary), "n_hz": len(hz), "n_bao": len(bao), "n_total": len(hz) + len(bao)},
        "epistemic_boundary": {"claim_status": "point-evaluation only; not MCMC and not full evidence", "rll_model": "logistic background sector", "w0wa_model": "CPL adversary", "token_vazio": "full DESI DR2 covariance matrix and nested-sampling evidence unless externally supplied"},
        "bao_covariance": covariance_info(bao, cov, args.bao_diagonal, args.bao_covariance),
        "params": {model: parameter_payload(model, args) for model in models},
        "models": results,
        "comparisons": comparisons(results, args.with_bayes),
        "growth": growth_status(args.with_growth),
    }
    write_predictions(Path(args.out_csv), hz, bao, models, args)
    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary["comparisons"], indent=2))


if __name__ == "__main__":
    main()
