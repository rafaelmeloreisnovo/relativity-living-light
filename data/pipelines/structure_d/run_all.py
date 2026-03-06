import argparse
import csv
import json
import os
import subprocess
import time
import subprocess

import numpy as np
import pandas as pd

from .data_access import load_active_datasets, load_run_config
from .inference import run_lcdm_bayes, run_rll_like_agn_bayes
from .likelihood import (
    aic,
    bayes_factor_interpretation_contract,
    bic,
    chi2,
    chi2_with_covariance,
    estimate_log_evidence,
    evaluate_model,
    write_bayes_factor_interpretation,
)
from .models import (
    N_FREE_PARAMS_LCDM,
    N_FREE_PARAMS_RLL,
    model_LCDM_Hz,
    model_LCDM_bao_dv_over_rs,
    model_LCDM_fs8,
    model_RLL_like_Hz,
    model_RLL_like_bao_dv_over_rs,
    model_RLL_like_fs8,
)
from .reporting import run_reporting_pipeline
from . import run_all_real

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RESULTS = os.path.join(BASE_DIR, "results", "structure_d")
DEFAULT_CONFIG = os.path.join("data", "pipelines", "structure_d", "datasets_config.json")
DEFAULT_PROFILE = "structure_d_default"
REAL_PROFILE = "structure_d_real_validation"
MODEL_LCDM = "lcdm"
MODEL_RLL_AGN = "rll_like_agn"
REGIME_SYNTHETIC = "synthetic"
REGIME_REAL = "real"

REQUIRED_OUTPUTS = [
    "model_comparison.csv",
    "covariance_usage.csv",
    "error_mode_usage.csv",
    "rll_regime_summary.csv",
    "reproduction_contract.json",
]
OPTIONAL_OUTPUTS = {
    "bayes_evidence_bic_proxy.csv": "optional Bayesian summary via BIC proxy; generated only when --bayes --bayes-mode bic_proxy is used",
    "bayes_evidence_inference.csv": "optional Bayesian summary via nested inference; generated only when --bayes --bayes-mode inference is used",
    "bayes_factor_interpretation.csv": "optional Bayesian interpretation table; generated only when --bayes is used",
}

SUPPORTED_COVARIANCE_POLICIES = ["prefer_full", "diagonal_only", "full_required"]

EXPECTED_SCHEMA_BY_OUTPUT = {
    "model_comparison.csv": [
        "model",
        "regime",
        "chi2",
        "AIC",
        "BIC",
        "N",
        "k",
        "datasets_used",
        "run_name",
        "profile_name",
        "covariance_policy",
    ],
    "covariance_usage.csv": [
        "dataset_id",
        "block",
        "dataset_source",
        "covariance_mode",
        "effective_decision",
        "has_full_covariance",
        "has_diagonal_sigma",
    ],
    "error_mode_usage.csv": [
        "dataset_id",
        "observable",
        "error_mode",
    ],
    "rll_regime_summary.csv": [
        "z_min",
        "z_max",
        "R_mean",
        "dominant_regime",
        "top_parameters",
        "notes",
    ],
}


EXECUTION_TIMING_BASENAME = "execution_timing"


def _safe_git_commit():
    head_file = os.path.join(BASE_DIR, ".git", "HEAD")
    if not os.path.exists(head_file):
        return None
    try:
        import subprocess

        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=BASE_DIR, text=True).strip()
    except Exception:
        return None


def _safe_dirty_worktree():
    try:
        import subprocess

        out = subprocess.check_output(["git", "status", "--porcelain"], cwd=BASE_DIR, text=True)
        return bool(out.strip())
    except Exception:
        return None


def _validate_profile_name(cfg, profile_name):
    profiles = cfg.get("profiles")
    if not profiles:
        return

    selected_profile = profile_name or cfg.get("default_profile", DEFAULT_PROFILE)
    if selected_profile in profiles:
        return

    available_profiles = ", ".join(sorted(profiles.keys()))
    raise ValueError(
        "profile inválido: "
        f"{selected_profile!r}. "
        "Perfis disponíveis: "
        f"{available_profiles}"
    )


MODEL_BY_DATASET = {
    "hz": (model_LCDM_Hz, model_RLL_like_Hz),
    "real_hz": (model_LCDM_Hz, model_RLL_like_Hz),
    "fsigma8": (model_LCDM_fs8, model_RLL_like_fs8),
    "hz_cov_synth": (model_LCDM_Hz, model_RLL_like_Hz),
    "fsigma8_cov_synth": (model_LCDM_fs8, model_RLL_like_fs8),
    "real_bao": (model_LCDM_bao_dv_over_rs, model_RLL_like_bao_dv_over_rs),
}

C_KMS = 299792.458
Z_CMB = 1089.92


def _dataset_block_name(dataset_id, entry):
    observable = str(entry.get("observable", dataset_id)).lower()
    if dataset_id in {"hz", "real_hz", "hz_cov_synth"} or "hz" in observable:
        return "Hz"
    if dataset_id in {"fsigma8", "fsigma8_cov_synth"} or "fs" in observable:
        return "fσ8"
    if "bao" in observable:
        return "BAO"
    if "sne" in observable:
        return "SNe"
    if "lens" in observable:
        return "lenses"
    return str(entry.get("observable", dataset_id))


def _build_error_mode_rows(datasets):
    rows = []
    for dataset_id, entry in datasets.items():
        has_cov = entry.get("covariance") is not None
        has_err = entry.get("errors") is not None
        if has_cov and has_err:
            mode = "both"
        elif has_cov:
            mode = "covariance"
        elif has_err:
            mode = "errors"
        else:
            mode = "none"
        rows.append(
            {
                "dataset_id": dataset_id,
                "observable": entry.get("observable", "unknown"),
                "error_mode": mode,
            }
        )
    return rows


def _apply_covariance_policy(datasets, covariance_policy):
    if covariance_policy == "full_required":
        incompatible_ids = [dataset_id for dataset_id, entry in datasets.items() if entry.get("covariance") is None]
        if incompatible_ids:
            incompatible_ids = sorted(incompatible_ids)
            raise ValueError(
                "covariance_policy='full_required' requires full covariance for all active datasets; "
                f"incompatible datasets: {incompatible_ids}"
            )

    for entry in datasets.values():
        if covariance_policy == "diagonal_only" and entry.get("covariance") is not None:
            entry["errors"] = np.sqrt(np.diag(np.asarray(entry["covariance"], dtype=float)))
            entry["covariance"] = None
    return covariance_policy


def _find_dataset_by_kind(datasets, kind):
    target = str(kind).lower()
    for dataset_id, entry in datasets.items():
        observable = str(entry.get("observable", "")).lower()
        dataset_name = str(dataset_id).lower()
        if target == "hz" and ("hz" in dataset_name or "hz" in observable):
            return entry
        if target == "fsigma8" and ("fsigma8" in dataset_name or "fs8" in observable or "fsigma8" in observable):
            return entry
    return None


def _chi2_from_entry(entry, model_values):
    if entry.get("errors") is not None:
        return chi2(entry["values"], model_values, entry["errors"])
    return chi2_with_covariance(entry["values"], model_values, entry["covariance"])


def _chi2_bao_from_entry(entry, model_values):
    return _chi2_from_entry(entry, model_values)


def _comoving_distance_mpc(z, hz_model, params, n_steps=2048):
    z_scalar = float(z)
    if not np.isfinite(z_scalar) or z_scalar <= 0.0:
        return float("nan")
    grid = np.linspace(0.0, z_scalar, int(max(64, n_steps)))
    hz = np.asarray(hz_model(grid, params), dtype=float)
    if np.any(~np.isfinite(hz)) or np.any(hz <= 0.0):
        return float("nan")
    return float(np.trapz(C_KMS / hz, grid))


def _cmb_shift_prediction(params, hz_model):
    dc_cmb = _comoving_distance_mpc(Z_CMB, hz_model, params)
    if not np.isfinite(dc_cmb) or dc_cmb <= 0.0:
        return np.array([np.nan, np.nan], dtype=float)
    r_th = np.sqrt(params["Om"]) * params["H0"] / C_KMS * dc_cmb
    rs = 147.78 * (params["Om"] * (params["H0"] / 100.0) ** 2 / 0.1432) ** (-0.255) * (params.get("Ob_h2", 0.02236) / 0.02236) ** (-0.134)
    la_th = np.pi * dc_cmb / rs
    return np.array([r_th, la_th], dtype=float)


def _chi2_scalar_by_observable(entry, lcdm, rll):
    observable = str(entry.get("observable", "")).strip().lower()
    if observable == "cmb_shift":
        lcdm_prediction = _cmb_shift_prediction(lcdm, model_LCDM_Hz)
        rll_prediction = _cmb_shift_prediction(rll, model_RLL_like_Hz)
        return _chi2_from_entry(entry, lcdm_prediction), _chi2_from_entry(entry, rll_prediction)
    raise ValueError(
        f"unsupported scalar dataset {entry['dataset_id']!r} with observable={entry.get('observable')!r}; "
        "add explicit scalar handling instead of silently discarding"
    )




def _find_dataset_by_kind(datasets, kind):
    kind_aliases = {
        "hz": {"hz", "real_hz", "hz_cov_synth"},
        "fsigma8": {"fsigma8", "fsigma8_cov_synth"},
    }
    target_ids = kind_aliases.get(kind, {kind})
    for dataset_id in target_ids:
        if dataset_id in datasets:
            return datasets[dataset_id]
    return None

def run_classic_metrics(cfg_meta, datasets, covariance_policy):
    lcdm = dict(H0=70.0, Om=0.3, Ol=0.7, sigma8=0.8, gamma=0.55, Ob_h2=0.02236)
    rll = dict(H0=70.0, Om=0.3, Ol=0.7, sigma8=0.8, gamma=0.55, alpha=0.06, z_peak=2.0, width=1.2, beta=0.00, Ob_h2=0.02236)
    fit_params_lcdm = ["H0", "Om", "sigma8", "gamma"]
    fit_params_rll = fit_params_lcdm + ["alpha", "z_peak", "width"]
    fixed_params_lcdm = sorted(set(lcdm) - set(fit_params_lcdm))
    fixed_params_rll = sorted(set(rll) - set(fit_params_rll))

    rows = []
    cov_rows = []
    chi2_lcdm = 0.0
    chi2_rll = 0.0
    n_obs = 0

    for dataset_id in cfg_meta["active_datasets"]:
        entry = datasets[dataset_id]
        cov_rows.append(
            {
                "dataset_id": dataset_id,
                "block": _dataset_block_name(dataset_id, entry),
                "dataset_source": entry.get("dataset_source", "unknown"),
                "covariance_mode": "full" if entry.get("covariance") is not None else "diagonal",
                "effective_decision": "full" if entry.get("covariance") is not None else "diag",
                "has_full_covariance": bool(entry.get("covariance") is not None),
                "has_diagonal_sigma": bool(entry.get("errors") is not None),
            }
        )

        model_pair = MODEL_BY_DATASET.get(dataset_id)
        has_z = entry.get("z") is not None

        if model_pair is None and has_z:
            raise ValueError(
                f"dataset {dataset_id!r} has redshift samples but no registered model pair; "
                "add MODEL_BY_DATASET mapping instead of silently discarding"
            )

        if not has_z:
            scalar_chi2_lcdm, scalar_chi2_rll = _chi2_scalar_by_observable(entry, lcdm, rll)
            chi2_lcdm += scalar_chi2_lcdm
            chi2_rll += scalar_chi2_rll
            n_obs += len(entry["values"])
            continue

        if model_pair is None:
            raise ValueError(
                f"dataset {dataset_id!r} is unsupported by classical metrics; "
                "explicitly register the observable/model before using it"
            )

        model_lcdm, model_rll = model_pair
        z = np.asarray(entry["z"], dtype=float)
        lcdm_prediction = model_lcdm(z, lcdm)
        rll_prediction = model_rll(z, rll)
        model_kind = "bao" if entry.get("observable") == "DV_over_rs" else "default"

        if "bao" in str(entry.get("observable", "")).lower():
            chi2_lcdm += _chi2_bao_from_entry(entry, lcdm_prediction)
            chi2_rll += _chi2_bao_from_entry(entry, rll_prediction)
        else:
            chi2_lcdm += _chi2_from_entry(entry, lcdm_prediction)
            chi2_rll += _chi2_from_entry(entry, rll_prediction)

        n_obs += len(entry["values"])

    if n_obs == 0:
        raise ValueError("no supported datasets were active for classical metrics")
    if not cov_rows:
        profile_name = cfg_meta.get("profile_name", DEFAULT_PROFILE)
        active = cfg_meta.get("active_datasets", [])
        raise ValueError(
            "covariance_usage.csv would be empty: no covariance rows generated "
            f"for profile={profile_name!r} with active_datasets={active}"
        )

    rows.append(
        {
            "model": MODEL_LCDM,
            "regime": REGIME_SYNTHETIC,
            "chi2": float(chi2_lcdm),
            "AIC": aic(chi2_lcdm, N_FREE_PARAMS_LCDM),
            "BIC": bic(chi2_lcdm, N_FREE_PARAMS_LCDM, n_obs),
            "N": int(n_obs),
            "k": N_FREE_PARAMS_LCDM,
            "fit_params": ",".join(fit_params_lcdm),
            "fixed_params": ",".join(fixed_params_lcdm),
            "datasets_used": ",".join(cfg_meta["active_datasets"]),
            "run_name": cfg_meta.get("run_name", "unknown"),
            "profile_name": cfg_meta.get("profile_name", DEFAULT_PROFILE),
            "covariance_policy": covariance_policy,
        }
    )
    rows.append(
        {
            "model": MODEL_RLL_AGN,
            "regime": REGIME_SYNTHETIC,
            "chi2": float(chi2_rll),
            "AIC": aic(chi2_rll, N_FREE_PARAMS_RLL),
            "BIC": bic(chi2_rll, N_FREE_PARAMS_RLL, n_obs),
            "N": int(n_obs),
            "k": N_FREE_PARAMS_RLL,
            "fit_params": ",".join(fit_params_rll),
            "fixed_params": ",".join(fixed_params_rll),
            "datasets_used": ",".join(cfg_meta["active_datasets"]),
            "run_name": cfg_meta.get("run_name", "unknown"),
            "profile_name": cfg_meta.get("profile_name", DEFAULT_PROFILE),
            "covariance_policy": covariance_policy,
        }
    )

    out_model = os.path.join(RESULTS, "model_comparison.csv")
    out_cov = os.path.join(RESULTS, "covariance_usage.csv")
    out_error_mode = os.path.join(RESULTS, "error_mode_usage.csv")
    evaluate_model(rows, out_model)
    evaluate_model(cov_rows, out_cov)
    evaluate_model(_build_error_mode_rows(datasets), out_error_mode)
    return pd.DataFrame(rows), out_model, out_cov, bool(cov_rows)




def _find_dataset_by_kind(datasets, kind):
    kind_l = str(kind).lower()
    aliases = {kind_l}
    if kind_l == "fsigma8":
        aliases.update({"fs8", "fσ8", "f_sigma8"})

    for dataset_id, entry in datasets.items():
        observable = str(entry.get("observable", "")).lower()
        dataset_id_l = dataset_id.lower()
        if any(alias in dataset_id_l or alias in observable for alias in aliases):
            z = entry.get("z")
            values = entry.get("values")
            errors = entry.get("errors")
            if z is None or values is None or errors is None:
                continue
            return entry
    return None

def run_optional_bayes_summary_bic_proxy(df_model):
    rows = []
    for _, row in df_model.iterrows():
        logz, logz_err = estimate_log_evidence(bic_value=float(row["BIC"]))
        rows.append(
            {
                "model": row["model"],
                "regime": row.get("regime", REGIME_SYNTHETIC),
                "log_evidence": logz,
                "log_evidence_std": logz_err,
                "log_evidence_std_defined": bool(np.isfinite(logz_err)),
                "source": "bic_proxy",
            }
        )

    out_evidence = os.path.join(RESULTS, "bayes_evidence_bic_proxy.csv")
    out_interp = os.path.join(RESULTS, "bayes_factor_interpretation.csv")
    evaluate_model(rows, out_evidence)
    write_bayes_factor_interpretation(out_interp)
    return [out_evidence, out_interp]


def run_optional_bayes_summary_inference(hz_df, fs8_df, seed, nwalkers, nsteps, nlive):
    rows = []
    for runner in (run_lcdm_bayes, run_rll_like_agn_bayes):
        result = runner(hz_df, fs8_df, seed=seed, nwalkers=nwalkers, nsteps=nsteps, nlive=nlive, output_dir=RESULTS)
        row = dict(result["row"])
        row["regime"] = REGIME_SYNTHETIC
        row["source"] = "inference"
        rows.append(row)

    out_evidence = os.path.join(RESULTS, "bayes_evidence_inference.csv")
    out_interp = os.path.join(RESULTS, "bayes_factor_interpretation.csv")
    evaluate_model(rows, out_evidence)
    write_bayes_factor_interpretation(out_interp)
    return [out_evidence, out_interp]


def _git_metadata():
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        commit = None
    try:
        dirty = bool(subprocess.check_output(["git", "status", "--porcelain"], text=True).strip())
    except Exception:
        dirty = None
    return commit, dirty


def _dataset_contract_block(cfg_meta, datasets):
    rows = []
    for dataset_id in cfg_meta.get("active_datasets", []):
        source = datasets.get(dataset_id, {}).get("source", {})
        rows.append(
            {
                "dataset_id": dataset_id,
                "path_abs": source.get("path_abs"),
                "timestamp_utc": source.get("timestamp_utc"),
                "sha256": source.get("sha256"),
            }
        )
    return rows


def _write_reproduction_contract(profile_name, covariance_policy, bayes, bayes_mode, produced_optional, covariance_usage_non_empty, cfg_meta=None, datasets=None, inference_hyperparameters=None, execution_timing_outputs=None, bayes_seed=None, bayes_nwalkers=None, bayes_nsteps=None, bayes_nlive=None):
    git_commit, dirty_worktree = _git_metadata()
    if inference_hyperparameters is None and all(v is not None for v in (bayes_seed, bayes_nwalkers, bayes_nsteps, bayes_nlive)):
        inference_hyperparameters = {
            "seed": int(bayes_seed),
            "nwalkers": int(bayes_nwalkers),
            "nsteps": int(bayes_nsteps),
            "nlive": int(bayes_nlive),
        }

    cfg_meta = cfg_meta or {}
    datasets = datasets or {}
    contract = {
        "command": "python -m data.pipelines.structure_d.run_all",
        "execution_path": "classic",
        "profile": profile_name,
        "git_commit": git_commit,
        "dirty_worktree": dirty_worktree,
        "covariance_policy": covariance_policy,
        "covariance_policy_supported": SUPPORTED_COVARIANCE_POLICIES,
        "mock_data_contract": "data/inputs/structure_d/mock_data_contract.json",
        "required_outputs": REQUIRED_OUTPUTS,
        "optional_outputs": [
            {
                "file": name,
                "produced": name in produced_optional,
                "reason": reason,
            }
            for name, reason in OPTIONAL_OUTPUTS.items()
        ],
        "bayes_enabled": bool(bayes),
        "bayes_mode": bayes_mode if bayes else None,
        "bayes_inference_hyperparameters": inference_hyperparameters if bayes else None,
        "covariance_usage_non_empty": bool(covariance_usage_non_empty),
        "datasets": _dataset_contract_block(cfg_meta, datasets),
        "execution_timing_outputs": execution_timing_outputs or [],
    }
    out_contract = os.path.join(RESULTS, "reproduction_contract.json")
    with open(out_contract, "w", encoding="utf-8") as fp:
        json.dump(contract, fp, ensure_ascii=False, indent=2)
    return out_contract


def _build_main_result(df_model, effective_profile, effective_policy, output_paths, extra_paths=None):
    payload = {
        "rows": int(len(df_model)),
        "profile": effective_profile,
        "covariance_policy": effective_policy,
        "output_paths": output_paths,
    }
    if extra_paths:
        payload["extra_paths"] = extra_paths
    return payload


def _write_execution_timing(records, basename=EXECUTION_TIMING_BASENAME):
    out_timing_csv = os.path.join(RESULTS, f"{basename}.csv")
    out_timing_json = os.path.join(RESULTS, f"{basename}.json")

    with open(out_timing_csv, "w", encoding="utf-8", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=["block", "duration_seconds"])
        writer.writeheader()
        for record in records:
            writer.writerow(record)

    with open(out_timing_json, "w", encoding="utf-8") as fp:
        json.dump(records, fp, ensure_ascii=False, indent=2)

    return out_timing_csv, out_timing_json


def _write_real_reproduction_contract(profile_name, covariance_policy, maxiter_lcdm, maxiter_rll, tol, seed, execution_timing_outputs=None):
    contract = {
        "command": "python -m data.pipelines.structure_d.run_all --profile structure_d_real_validation",
        "execution_path": "run_all_real",
        "delegated_module": "data.pipelines.structure_d.run_all_real",
        "profile": profile_name,
        "covariance_policy": covariance_policy,
        "maxiter_lcdm": int(maxiter_lcdm),
        "maxiter_rll": int(maxiter_rll),
        "tol": float(tol),
        "seed": int(seed),
        "required_outputs": REQUIRED_OUTPUTS,
        "optional_outputs": [
            {
                "file": name,
                "produced": False,
                "reason": reason,
            }
            for name, reason in OPTIONAL_OUTPUTS.items()
        ],
        "bayes_enabled": False,
        "bayes_mode": None,
        "bayes_runtime_metadata": None,
        "covariance_usage_non_empty": True,
        "real_execution_skipped": False,
        "real_execution_skip_reason": None,
        "execution_timing_outputs": execution_timing_outputs or [],
    }
    out_contract = os.path.join(RESULTS, "reproduction_contract.json")
    with open(out_contract, "w", encoding="utf-8") as fp:
        json.dump(contract, fp, ensure_ascii=False, indent=2)
    return out_contract


def _ensure_rll_regime_summary():
    out_path = os.path.join(RESULTS, "rll_regime_summary.csv")
    if os.path.exists(out_path):
        return out_path

    placeholder = pd.DataFrame(
        [
            {
                "z_min": np.nan,
                "z_max": np.nan,
                "R_mean": np.nan,
                "dominant_regime": "n/a",
                "top_parameters": "n/a",
                "notes": "placeholder summary (not produced by reporting pipeline)",
            }
        ]
    )
    placeholder.to_csv(out_path, index=False)
    return out_path


def _assert_required_outputs():
    for filename in REQUIRED_OUTPUTS:
        path = os.path.join(RESULTS, filename)
        if not os.path.exists(path):
            raise RuntimeError(f"arquivo inválido: {filename} (não foi gerado)")

        if filename.endswith(".csv"):
            _assert_csv_output_has_useful_content(filename, path)
        elif filename.endswith(".json"):
            _assert_json_output_has_useful_content(filename, path)


def _assert_csv_output_has_useful_content(filename, path):
    try:
        df = pd.read_csv(path)
    except Exception as exc:
        raise RuntimeError(f"arquivo inválido: {filename} (CSV não parseável)") from exc

    if df.empty:
        raise RuntimeError(f"arquivo inválido: {filename} (CSV sem linhas de dados)")

    useful_rows = 0
    for row in df.itertuples(index=False, name=None):
        has_value = any(
            value is not None
            and not pd.isna(value)
            and str(value).strip() != ""
            for value in row
        )
        if has_value:
            useful_rows += 1
            break

    if useful_rows == 0:
        raise RuntimeError(f"arquivo inválido: {filename} (CSV sem linha útil)")


def _assert_json_output_has_useful_content(filename, path):
    try:
        with open(path, "r", encoding="utf-8") as fp:
            content = json.load(fp)
    except Exception as exc:
        raise RuntimeError(f"arquivo inválido: {filename} (JSON não parseável)") from exc

    if isinstance(content, dict):
        has_useful_content = any(value not in (None, "", [], {}) for value in content.values())
    elif isinstance(content, list):
        has_useful_content = len(content) > 0
    else:
        has_useful_content = content not in (None, "")

    if not has_useful_content:
        raise RuntimeError(f"arquivo inválido: {filename} (JSON sem conteúdo útil)")


def _validate_output_schema(filename, expected_header):
    path = os.path.join(RESULTS, filename)
    actual_header = list(pd.read_csv(path, nrows=0).columns)
    missing = [column for column in expected_header if column not in actual_header]
    if missing:
        raise RuntimeError(
            f"schema mismatch for {filename}: missing required columns {missing}; got {actual_header}"
        )


def _validate_required_csv_schemas():
    required_csv_outputs = [name for name in REQUIRED_OUTPUTS if name.endswith(".csv")]
    missing_schema_definitions = [name for name in required_csv_outputs if name not in EXPECTED_SCHEMA_BY_OUTPUT]
    if missing_schema_definitions:
        raise RuntimeError(
            "missing expected schema definition for required csv outputs: "
            f"{missing_schema_definitions}"
        )

    for filename in required_csv_outputs:
        _validate_output_schema(filename, EXPECTED_SCHEMA_BY_OUTPUT[filename])




def _build_main_result(df_model, effective_profile, effective_policy, output_paths, extra_paths=None):
    result = {
        "profile": effective_profile,
        "covariance_policy": effective_policy,
        "rows": int(len(df_model)),
        "output_paths": dict(output_paths),
    }
    if extra_paths:
        result["extra_paths"] = dict(extra_paths)
    return result

def main(
    config_path=DEFAULT_CONFIG,
    profile_name=DEFAULT_PROFILE,
    covariance_policy=None,
    bayes=False,
    bayes_mode="bic_proxy",
    bayes_seed=42,
    bayes_nwalkers=32,
    bayes_nsteps=2000,
    bayes_nlive=400,
):
    os.makedirs(RESULTS, exist_ok=True)

    timing_records = []

    load_t0 = time.perf_counter()
    cfg = load_run_config(config_path)
    _validate_profile_name(cfg, profile_name)
    cfg_meta, datasets = load_active_datasets(config_path, profile_name=profile_name)
    effective_profile = cfg_meta.get("profile_name") or cfg.get("default_profile", DEFAULT_PROFILE)
    effective_policy = _apply_covariance_policy(datasets, covariance_policy or cfg_meta.get("covariance_policy") or cfg.get("covariance_policy", "prefer_full"))
    timing_records.append({"block": "load", "duration_seconds": time.perf_counter() - load_t0})

    if effective_profile == REAL_PROFILE:
        maxiter_lcdm = int(os.environ.get("STRUCTURE_D_MAXITER_LCDM", "120"))
        maxiter_rll = int(os.environ.get("STRUCTURE_D_MAXITER_RLL", "150"))
        tol = float(os.environ.get("STRUCTURE_D_TOL", "1e-6"))
        seed = int(os.environ.get("STRUCTURE_D_SEED", "42"))

        fit_t0 = time.perf_counter()
        df_model = run_all_real.main(
            config_path=config_path,
            profile_name=effective_profile,
            output_filename="model_comparison.csv",
            covariance_policy=effective_policy,
            include_fit_params=False,
        )
        model_path = os.path.join(RESULTS, "model_comparison.csv")
        model_df = pd.read_csv(model_path)
        model_df["model"] = model_df["model"].replace({"lcdm": "LCDM", "rll_like_agn": "RLL_like+AGN"})
        allowed_columns = EXPECTED_SCHEMA_BY_OUTPUT["model_comparison.csv"]
        missing_columns = [col for col in allowed_columns if col not in model_df.columns]
        if missing_columns:
            raise RuntimeError(f"schema mismatch for model_comparison.csv: missing required columns {missing_columns}")
        model_df = model_df[allowed_columns]
        model_df.to_csv(model_path, index=False)
        df_model = model_df
        out_cov = os.path.join(RESULTS, "covariance_usage.csv")
        out_error_mode = os.path.join(RESULTS, "error_mode_usage.csv")
        cov_rows = [
            {
                "dataset_id": dataset_id,
                "block": _dataset_block_name(dataset_id, entry),
                "dataset_source": entry.get("dataset_source", "unknown"),
                "covariance_mode": "full" if entry.get("covariance") is not None else "diagonal",
                "effective_decision": "full" if entry.get("covariance") is not None else "diag",
                "has_full_covariance": bool(entry.get("covariance") is not None),
                "has_diagonal_sigma": bool(entry.get("errors") is not None),
            }
            for dataset_id, entry in datasets.items()
        ]
        evaluate_model(cov_rows, out_cov)
        evaluate_model(_build_error_mode_rows(datasets), out_error_mode)
        _ensure_rll_regime_summary()
        timing_records.append({"block": "fit", "duration_seconds": time.perf_counter() - fit_t0})

        write_t0 = time.perf_counter()
        out_contract = _write_real_reproduction_contract(
            effective_profile,
            effective_policy,
            maxiter_lcdm=maxiter_lcdm,
            maxiter_rll=maxiter_rll,
            tol=tol,
            seed=seed,
            execution_timing_outputs=[
                f"{EXECUTION_TIMING_BASENAME}.csv",
                f"{EXECUTION_TIMING_BASENAME}.json",
            ],
        )
        timing_records.append({"block": "write", "duration_seconds": time.perf_counter() - write_t0})
        out_timing_csv, out_timing_json = _write_execution_timing(timing_records, basename=EXECUTION_TIMING_BASENAME)
        validate_t0 = time.perf_counter()
        _assert_required_outputs()
        _validate_required_csv_schemas()
        timing_records.append({"block": "validate", "duration_seconds": time.perf_counter() - validate_t0})
        out_timing_csv, out_timing_json = _write_execution_timing(timing_records, basename=EXECUTION_TIMING_BASENAME)

        print(df_model.to_string(index=False))
        print(f"[real] wrote: {os.path.join(RESULTS, 'model_comparison.csv')}")
        print(f"[real] wrote: {out_cov}")
        print(f"[real] wrote: {out_error_mode}")
        print(f"[real] wrote: {os.path.join(RESULTS, 'rll_regime_summary.csv')}")
        print(f"[real] wrote: {out_contract}")
        return _build_main_result(
            df_model=df_model,
            effective_profile=effective_profile,
            effective_policy=effective_policy,
            output_paths={
                "model_comparison": os.path.join(RESULTS, "model_comparison.csv"),
                "covariance_usage": out_cov,
                "rll_regime_summary": os.path.join(RESULTS, "rll_regime_summary.csv"),
                "reproduction_contract": out_contract,
            },
        )

    fit_t0 = time.perf_counter()
    df_model, out_model, out_cov, covariance_usage_non_empty = run_classic_metrics(cfg_meta, datasets, effective_policy)

    hz_df = None
    fs8_df = None
    hz = _find_dataset_by_kind(datasets, "hz")
    fs8 = _find_dataset_by_kind(datasets, "fsigma8")
    if hz is not None and fs8 is not None:
        hz_df = pd.DataFrame({"z": hz["z"], "Hz": hz["values"], "sigma": hz["errors"]})
        fs8_df = pd.DataFrame({"z": fs8["z"], "fs8": fs8["values"], "sigma": fs8["errors"]})
        rll = dict(H0=70.0, Om=0.3, Ol=0.7, sigma8=0.8, gamma=0.55, alpha=0.06, z_peak=2.0, width=1.2, beta=0.00)
        run_reporting_pipeline(params=rll, hz_data=hz_df, fs8_data=fs8_df)

    _ensure_rll_regime_summary()
    produced_optional = []
    if bayes:
        if bayes_mode == "bic_proxy":
            output_paths = run_optional_bayes_summary_bic_proxy(df_model)
        elif bayes_mode == "inference":
            if hz_df is None or fs8_df is None:
                raise ValueError("bayes_mode='inference' requires both hz and fsigma8 datasets")
            output_paths = run_optional_bayes_summary_inference(
                hz_df,
                fs8_df,
                seed=bayes_seed,
                nwalkers=bayes_nwalkers,
                nsteps=bayes_nsteps,
                nlive=bayes_nlive,
            )
        else:
            raise ValueError(f"unsupported bayes_mode: {bayes_mode}")
        for path in output_paths:
            produced_optional.append(os.path.basename(path))
    timing_records.append({"block": "fit", "duration_seconds": time.perf_counter() - fit_t0})

    write_t0 = time.perf_counter()
    timing_records.append({"block": "write", "duration_seconds": time.perf_counter() - write_t0})
    out_contract = _write_reproduction_contract(
        effective_profile,
        effective_policy,
        bayes,
        bayes_mode,
        produced_optional,
        covariance_usage_non_empty,
        cfg_meta,
        datasets,
        inference_hyperparameters={
            "seed": int(bayes_seed),
            "nwalkers": int(bayes_nwalkers),
            "nsteps": int(bayes_nsteps),
            "nlive": int(bayes_nlive),
        } if bayes and bayes_mode == "inference" else None,
        execution_timing_outputs=[
            f"{EXECUTION_TIMING_BASENAME}.csv",
            f"{EXECUTION_TIMING_BASENAME}.json",
        ],
    )

    validate_t0 = time.perf_counter()
    _assert_required_outputs()
    _validate_required_csv_schemas()
    timing_records.append({"block": "validate", "duration_seconds": time.perf_counter() - validate_t0})
    out_timing_csv, out_timing_json = _write_execution_timing(timing_records, basename=EXECUTION_TIMING_BASENAME)

    print(df_model.to_string(index=False))
    print(f"[classic] wrote: {out_model}")
    print(f"[classic] wrote: {out_cov}")
    print(f"[classic] wrote: {os.path.join(RESULTS, 'error_mode_usage.csv')}")
    print(f"[classic] wrote: {os.path.join(RESULTS, 'rll_regime_summary.csv')}")
    print(f"[classic] wrote: {out_contract}")
    if bayes:
        for name in produced_optional:
            print(f"[bayes] wrote: {os.path.join(RESULTS, name)}")
        print(f"[bayes] mode: {bayes_mode}")
        if bayes_mode == "inference":
            print(
                "[bayes] inference hyperparameters: "
                f"seed={bayes_seed}, nwalkers={bayes_nwalkers}, nsteps={bayes_nsteps}, nlive={bayes_nlive}"
            )

    return _build_main_result(
        df_model=df_model,
        effective_profile=effective_profile,
        effective_policy=effective_policy,
        output_paths={
            "model_comparison": out_model,
            "covariance_usage": out_cov,
            "rll_regime_summary": os.path.join(RESULTS, "rll_regime_summary.csv"),
            "reproduction_contract": out_contract,
        },
        extra_paths={
            "bayes": [os.path.join(RESULTS, name) for name in produced_optional],
        }
        if bayes
        else None,
    )




def _build_main_result(df_model, effective_profile, effective_policy, output_paths, extra_paths=None):
    payload = {
        "effective_profile": effective_profile,
        "effective_policy": effective_policy,
        "rows": len(df_model),
        "output_paths": output_paths,
    }
    if extra_paths:
        payload["extra_paths"] = extra_paths
    return payload

def _build_parser():
    parser = argparse.ArgumentParser(description="Executa o pipeline structure_d")
    parser.add_argument("--config", default=DEFAULT_CONFIG)
    parser.add_argument("--profile", default=os.environ.get("STRUCTURE_D_PROFILE", DEFAULT_PROFILE))
    parser.add_argument("--covariance-policy", default=None, choices=["prefer_full", "diagonal_only", "full_required"])
    parser.add_argument("--bayes", action="store_true", help="Gera artefatos bayesianos opcionais")
    parser.add_argument("--bayes-mode", default="bic_proxy", choices=["bic_proxy", "inference"], help="Seleciona entre proxy BIC e inferência real")
    parser.add_argument("--bayes-seed", type=int, default=42)
    parser.add_argument("--bayes-nwalkers", type=int, default=32)
    parser.add_argument("--bayes-nsteps", type=int, default=2000)
    parser.add_argument("--bayes-nlive", type=int, default=400)
    return parser


if __name__ == "__main__":
    args = _build_parser().parse_args()
    main(
        config_path=args.config,
        profile_name=args.profile,
        covariance_policy=args.covariance_policy,
        bayes=args.bayes,
        bayes_mode=args.bayes_mode,
        bayes_seed=args.bayes_seed,
        bayes_nwalkers=args.bayes_nwalkers,
        bayes_nsteps=args.bayes_nsteps,
        bayes_nlive=args.bayes_nlive,
    )
