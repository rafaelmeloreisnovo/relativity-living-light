#!/usr/bin/env python3
"""Compute the RLL real-data pipeline from materialized, non-synthetic inputs.

The script intentionally fails when required real inputs are absent.  It reads
real H(z), BAO and optional CMB shift-ruler files from the workflow materialized
folder first, or from the committed real-data directory when requested.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd

C_KM_S = 299792.458
H0 = 70.0
OM = 0.30
OL = 0.70
RD_MPC = 147.09


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    import hashlib

    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def e_lcdm(z: np.ndarray | float) -> np.ndarray | float:
    return np.sqrt(OM * np.power(1.0 + z, 3) + OL)


def e_rll(z: np.ndarray | float, os_amp: float = 0.015, zt: float = 0.9, wt: float = 0.25) -> np.ndarray | float:
    z_arr = np.asarray(z, dtype=float)
    transition = 1.0 / (1.0 + np.exp((z_arr - zt) / wt))
    bracket = transition + (1.0 - transition) * np.power(1.0 + z_arr, 3)
    # Renormalize so E(0)=1 while preserving a small testable sector.
    f0 = 1.0 / (1.0 + math.exp((0.0 - zt) / wt))
    ol_eff = 1.0 - OM - os_amp * (f0 + (1.0 - f0))
    value = np.sqrt(OM * np.power(1.0 + z_arr, 3) + ol_eff + os_amp * bracket)
    if np.isscalar(z):
        return float(value)
    return value


def simpson_integral(fn, z: float, steps: int = 512) -> float:
    if z <= 0:
        return 0.0
    if steps % 2:
        steps += 1
    x = np.linspace(0.0, z, steps + 1)
    y = fn(x)
    h = z / steps
    return float(h / 3.0 * (y[0] + y[-1] + 4.0 * y[1:-1:2].sum() + 2.0 * y[2:-1:2].sum()))


def dv_over_rs(z: float, e_fn) -> float:
    dc = (C_KM_S / H0) * simpson_integral(lambda x: 1.0 / e_fn(x), z)
    dh = C_KM_S / (H0 * float(e_fn(z)))
    return float((z * dc * dc * dh) ** (1.0 / 3.0) / RD_MPC)


def first_existing(candidates: Iterable[Path], label: str) -> Path:
    for path in candidates:
        if path.exists():
            return path
    checked = ", ".join(str(p) for p in candidates)
    raise FileNotFoundError(f"required real input missing for {label}; checked: {checked}")


def resolve_inputs(raw_dir: Path, real_data_dir: Path, data_source: str) -> dict[str, Path]:
    materialized = raw_dir / "cosmology_curated"
    choices = {
        "Hz_data_real.csv": [materialized / "Hz_data_real.csv", real_data_dir / "Hz_data_real.csv"],
        "BAO_data_real.csv": [materialized / "BAO_data_real.csv", real_data_dir / "BAO_data_real.csv"],
        "CMB_shift_real.json": [materialized / "CMB_shift_real.json", real_data_dir / "CMB_shift_real.json"],
    }
    if data_source == "materialized":
        choices = {name: [paths[0]] for name, paths in choices.items()}
    elif data_source == "repo":
        choices = {name: [paths[1]] for name, paths in choices.items()}
    return {name: first_existing(paths, name) for name, paths in choices.items()}


def validate_hz(df: pd.DataFrame) -> pd.DataFrame:
    required = {"z", "H_obs", "sigma_H", "source"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Hz data missing columns: {sorted(missing)}")
    out = df.copy()
    out["z"] = pd.to_numeric(out["z"])
    out["H_obs"] = pd.to_numeric(out["H_obs"])
    out["sigma_H"] = pd.to_numeric(out["sigma_H"])
    if (out["sigma_H"] <= 0).any():
        raise ValueError("Hz sigma_H must be positive")
    return out.sort_values("z").reset_index(drop=True)


def validate_bao(df: pd.DataFrame) -> pd.DataFrame:
    required = {"z_eff", "DV_over_rs", "sigma", "survey"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"BAO data missing columns: {sorted(missing)}")
    out = df.copy()
    out["z_eff"] = pd.to_numeric(out["z_eff"])
    out["DV_over_rs"] = pd.to_numeric(out["DV_over_rs"])
    out["sigma"] = pd.to_numeric(out["sigma"])
    if (out["sigma"] <= 0).any():
        raise ValueError("BAO sigma must be positive")
    return out.sort_values("z_eff").reset_index(drop=True)



def validation_status_payload() -> dict[str, object]:
    """Return the scale-separated validation contract for RLL pre-movement terms.

    The local dynamic layer records Rafael's "pre-movement" intuition without
    promoting it to a homogeneous-background cosmology parameter.
    """

    return {
        "background_parameters": [
            "H0",
            "Omega_m",
            "Omega_Lambda",
            "Omega_b_h2",
            "Omega_c_h2",
            "theta_star",
            "tau",
            "ln10_10_As",
            "n_s",
        ],
        "radiation_neutrino_parameters": [
            "Omega_r",
            "N_eff",
            "sum_m_nu",
            "Omega_gamma",
            "Omega_nu",
        ],
        "growth_parameters": [
            "sigma8",
            "S8",
            "fsigma8",
            "D_z",
            "P_k",
            "delta_m",
        ],
        "initial_condition_layer": [
            "A_s",
            "n_s",
            "alpha_s",
            "primordial_perturbations",
            "acoustic_scale",
        ],
        "local_dynamic_layer": [
            "Phi_pre",
            "E_bound",
            "tau_relax",
            "Q_diss",
            "M_dyn",
            "L_orbital",
            "spin",
            "eccentricity",
            "separation_orbital",
            "gravitational_wave_loss",
            "G_pre",
            "field_gradient",
            "vector_convergence",
            "neighbouring_orbital_ellipses",
        ],
        "scale_bridge_examples": [
            "binary_stars_or_black_holes_with_converging_vector_motion",
            "planet_star_orbit_groups_in_neighbouring_ellipses",
            "chaotic_galactic_cascades_and_domino_like_field_relaxation",
            "milky_way_and_andromeda_large_scale_local_group_dynamics",
            "apollo_lunar_impact_dynamic_memory_without_cosmological_promotion",
            "local_domino_cascade_in_orbital_or_galactic_subsystems",
        ],
        "symbolic_complexity_marker": "n^n + n*x = y^x + n + x + z + omega + alpha + tesseract is non-operational until dimensions, units, observables, and falsification tests are defined",
        "claim_boundary": "local dynamic layer cannot be promoted to background cosmology without scale bridge",
        "interpretation": (
            "Pre-movement is modeled as scale-indexed initial/bound-state dynamics: "
            "it can condition local events, mergers, relaxation, and structure growth, "
            "but it is not an extra global LCDM background parameter by itself."
        ),
    }

def chi2_from_pulls(pulls: pd.Series) -> float:
    return float(np.square(pulls.astype(float)).sum())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="artifacts/rll-real-run")
    parser.add_argument("--raw-dir", default=None, help="Defaults to <output-dir>/raw")
    parser.add_argument("--real-data-dir", default="data/real")
    parser.add_argument("--data-source", choices=["auto", "materialized", "repo"], default="auto")
    args = parser.parse_args()

    root = Path(args.output_dir)
    raw = Path(args.raw_dir) if args.raw_dir else root / "raw"
    tables = root / "tables"
    processed = root / "processed"
    tables.mkdir(parents=True, exist_ok=True)
    processed.mkdir(parents=True, exist_ok=True)

    input_paths = resolve_inputs(raw, Path(args.real_data_dir), args.data_source)
    hz = validate_hz(pd.read_csv(input_paths["Hz_data_real.csv"]))
    bao = validate_bao(pd.read_csv(input_paths["BAO_data_real.csv"]))
    cmb = json.loads(input_paths["CMB_shift_real.json"].read_text(encoding="utf-8"))

    z_hz = hz["z"].to_numpy(dtype=float)
    hz["H_lcdm"] = H0 * e_lcdm(z_hz)
    hz["H_rll"] = H0 * e_rll(z_hz)
    hz["H_z"] = hz["H_rll"]
    hz["pull_lcdm"] = (hz["H_lcdm"] - hz["H_obs"]) / hz["sigma_H"]
    hz["pull_rll"] = (hz["H_rll"] - hz["H_obs"]) / hz["sigma_H"]
    hz["input_status"] = "real_non_synthetic"
    hz.to_csv(tables / "Hz_processed.csv", index=False)

    bao["z"] = bao["z_eff"]
    bao["bao_obs"] = bao["DV_over_rs"]
    bao["bao_lcdm"] = [dv_over_rs(float(z), e_lcdm) for z in bao["z_eff"]]
    bao["bao_rll"] = [dv_over_rs(float(z), e_rll) for z in bao["z_eff"]]
    bao["pull_lcdm"] = (bao["bao_lcdm"] - bao["DV_over_rs"]) / bao["sigma"]
    bao["pull_rll"] = (bao["bao_rll"] - bao["DV_over_rs"]) / bao["sigma"]
    bao["input_status"] = "real_non_synthetic"
    bao.to_csv(tables / "BAO_processed.csv", index=False)

    chi2_lcdm = chi2_from_pulls(hz["pull_lcdm"]) + chi2_from_pulls(bao["pull_lcdm"])
    chi2_rll = chi2_from_pulls(hz["pull_rll"]) + chi2_from_pulls(bao["pull_rll"])
    n = len(hz) + len(bao)
    models = []
    for model, chi2, k in [("LCDM", chi2_lcdm, 2), ("RLL", chi2_rll, 5)]:
        models.append({
            "model": model,
            "chi2": chi2,
            "n_real_points": n,
            "k_params": k,
            "AIC": chi2 + 2 * k,
            "BIC": chi2 + k * math.log(n),
            "data_status": "real_non_synthetic",
        })
    pd.DataFrame(models).to_csv(tables / "model_comparison.csv", index=False)

    a = np.linspace(0.2, 1.0, 48)
    z = (1.0 / a) - 1.0
    pd.DataFrame({
        "a": a,
        "z": z,
        "E2_matter": OM / np.power(a, 3),
        "E2_de": np.full_like(a, OL),
        "E2_lcdm": np.square(e_lcdm(z)),
        "E2_rll": np.square(e_rll(z)),
        "f_z": np.power((OM * np.power(1.0 + z, 3)) / np.square(e_lcdm(z)), 0.55),
    }).to_csv(tables / "rll_components.csv", index=False)

    pd.DataFrame([
        {"source": "igrf14", "status": "pending_real_parser", "note": "sem fabricacao: parser geomagnetico deve ser executado com coeficientes reais"},
        {"source": "wmm2025", "status": "pending_real_parser", "note": "sem fabricacao: parser WMM deve materializar coeficientes reais"},
    ]).to_csv(tables / "geomagnetic_metadata.csv", index=False)

    source_records = []
    for label, path in input_paths.items():
        source_records.append({"name": label, "path": str(path), "sha256": sha256_file(path), "status": "used_real_non_synthetic"})

    validation_status = validation_status_payload()
    report = [
        "# COMPUTE_REPORT",
        "",
        f"run_utc: {utc_now()}",
        "- data_source_mode: " + args.data_source,
        "- fallback_local: only explicit committed real data; no synthetic substitution",
        f"- Hz real points: {len(hz)}",
        f"- BAO real points: {len(bao)}",
        f"- CMB reference: {cmb.get('survey', 'unknown')} ({cmb.get('reference', 'no reference')})",
        f"- best_by_bic: {min(models, key=lambda row: row['BIC'])['model']}",
        "- geomagnetic: pending_real_parser, not fabricated",
        "- scale_bridge_claim_boundary: " + str(validation_status["claim_boundary"]),
    ]
    (root / "COMPUTE_REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    manifest = {
        "run_utc": utc_now(),
        "status": "Real data computed from non-synthetic inputs",
        "data_source_mode": args.data_source,
        "input_files": source_records,
        "fallback_policy": "fail if required real inputs are absent; repo real data allowed only as explicit fallback/source",
        "validation_status": validation_status,
        "outputs": [
            "tables/Hz_processed.csv",
            "tables/BAO_processed.csv",
            "tables/model_comparison.csv",
            "tables/rll_components.csv",
            "tables/geomagnetic_metadata.csv",
        ],
    }
    (root / "MANIFEST.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
