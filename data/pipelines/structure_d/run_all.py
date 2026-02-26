import argparse
import os
import argparse
import numpy as np
import pandas as pd

from .data_access import load_active_datasets, load_run_config
from .inference import run_nested_dynesty
from .likelihood import chi2, chi2_with_covariance, aic, bic, evaluate_model
from .models import model_LCDM_Hz, model_RLL_like_Hz, model_LCDM_fs8, model_RLL_like_fs8

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RESULTS = os.path.join(BASE_DIR, "results", "structure_d")
INPUTS_DIR = os.path.join(BASE_DIR, "data", "inputs", "structure_d")


def _resolve_column(df, aliases, required=False):
    lower_map = {c.lower(): c for c in df.columns}
    for alias in aliases:
        col = lower_map.get(alias.lower())
        if col is not None:
            return col
    if required:
        raise ValueError(f"missing required column among aliases: {aliases}")
    return None


def _find_dataset_file(stem):
    variants = [
        f"{stem}.csv",
        f"{stem.lower()}.csv",
        f"{stem.upper()}.csv",
        f"{stem.capitalize()}.csv",
    ]
    for name in variants:
        path = os.path.join(INPUTS_DIR, name)
        if os.path.exists(path):
            return path
    return None


def _find_covariance_file(stem):
    variants = [
        f"{stem}_cov.csv",
        f"{stem}_covariance.csv",
        f"{stem}_C.csv",
        f"C_{stem}.csv",
        f"{stem.lower()}_cov.csv",
        f"{stem.lower()}_covariance.csv",
        f"{stem.lower()}_C.csv",
        f"C_{stem.lower()}.csv",
    ]
    for name in variants:
        path = os.path.join(INPUTS_DIR, name)
        if os.path.exists(path):
            return np.loadtxt(path, delimiter=",")
    return None


def _load_block(block_name, obs_aliases):
    path = _find_dataset_file(block_name)
    if path is None:
        return None

    df = pd.read_csv(path)
    z_col = _resolve_column(df, ["z"], required=True)
    obs_col = _resolve_column(df, ["obs", *obs_aliases], required=True)
    sigma_col = _resolve_column(df, ["sigma"])

    cov = _find_covariance_file(block_name)
    if sigma_col is None and cov is None:
        raise ValueError(
            f"{os.path.basename(path)} requires 'sigma' for diagonal fallback or an external covariance matrix"
        )

    z = df[z_col].to_numpy(dtype=float)
    obs = df[obs_col].to_numpy(dtype=float)

    block = {
        "name": block_name,
        "z": z,
        "obs": obs,
        "mod": np.zeros_like(obs),
    }

    if sigma_col is not None:
        block["sigma"] = df[sigma_col].to_numpy(dtype=float)
    if cov is not None:
        block["C"] = np.asarray(cov, dtype=float)

    return block


def _base_blocks():
    candidates = [
        ("Hz", ["Hz", "H_obs"]),
        ("fsigma8", ["fs8", "f_sigma8", "fsigma8"]),
        ("sne", ["mu", "mub", "distance_modulus", "sne"]),
        ("bao", ["DV_over_rs", "bao", "obs_bao"]),
        ("lenses", ["lenses", "obs_lenses", "Ddt"]),
    ]

    blocks = []
    for name, aliases in candidates:
        block = _load_block(name, aliases)
        if block is not None:
            blocks.append(block)
    return blocks


def _apply_model_predictions(blocks, model_params, model_name):
    for block in blocks:
        if block["name"] == "Hz":
            block["mod"] = model_LCDM_Hz(block["z"], model_params) if model_name == "LCDM" else model_RLL_like_Hz(block["z"], model_params)
        elif block["name"] == "fsigma8":
            block["mod"] = model_LCDM_fs8(block["z"], model_params) if model_name == "LCDM" else model_RLL_like_fs8(block["z"], model_params)
        else:
            # Blocos sem modelagem explícita neste pipeline: mantemos contribuição nula (obs-mod = 0)
            block["mod"] = block["obs"].copy()


def _chi2_blocks(blocks):
    total = 0.0
    for block in blocks:
        if "C" in block:
            total += chi2_with_covariance(block["obs"], block["mod"], block["C"])
        else:
            total += chi2(block["obs"], block["mod"], block["sigma"])
    return float(total)


def covariance_usage_summary(blocks):
    rows = []
    for block in blocks:
        rows.append(
            {
                "block": block["name"],
                "covariance_mode": "full" if "C" in block else "diagonal",
                "has_full_covariance": "C" in block,
                "has_diagonal_sigma": "sigma" in block,
            }
        )
    return pd.DataFrame(rows)


def _chi2_from_entry(entry, model_values):
    if entry["errors"] is not None:
        return chi2(entry["values"], model_values, entry["errors"])
    return chi2_with_covariance(entry["values"], model_values, entry["covariance"])


def _evaluate_supported_dataset(dataset_id, entry, lcdm, rll):
    z_values = entry.get("z")
    if z_values is None:
        return 0.0, 0.0, 0

    observable = str(entry.get("observable", dataset_id)).lower()
    if "hz" in observable:
        lcdm_model = model_LCDM_Hz(z_values, lcdm)
        rll_model = model_RLL_like_Hz(z_values, rll)
    elif "fs" in observable:
        lcdm_model = model_LCDM_fs8(z_values, lcdm)
        rll_model = model_RLL_like_fs8(z_values, rll)
    else:
        return 0.0, 0.0, 0

    c2_lcdm = _chi2_from_entry(entry, lcdm_model)
    c2_rll = _chi2_from_entry(entry, rll_model)
    return c2_lcdm, c2_rll, len(entry["values"])


def _to_inference_frame(entry, value_name):
    if entry.get("errors") is None:
        return None
    z_values = entry.get("z")
    if z_values is None:
        return None
    return pd.DataFrame({"z": z_values, value_name: entry["values"], "sigma": entry["errors"]})


def run_classic_metrics(cfg_meta, datasets, covariance_policy):
    """# Bloco 1: Métrica clássica (χ²/AIC/BIC)."""
    rows = []

    lcdm = dict(H0=70.0, Om=0.3, Ol=0.7, sigma8=0.8, gamma=0.55)
    rll = dict(H0=70.0, Om=0.3, Ol=0.7, sigma8=0.8, gamma=0.55, alpha=0.06, z_peak=2.0, width=1.2, beta=0.00)

    fit_params_lcdm = ["H0", "Om", "sigma8", "gamma"]
    fit_params_rll = fit_params_lcdm + ["alpha", "z_peak", "width"]
    fixed_params_lcdm = sorted(set(lcdm) - set(fit_params_lcdm))
    fixed_params_rll = sorted(set(rll) - set(fit_params_rll))

    blocks_lcdm_active = _base_blocks()
    blocks_rll_active = [
        {
            k: (v.copy() if isinstance(v, np.ndarray) else v)
            for k, v in block.items()
        }
        for block in blocks_lcdm_active
    ]

    _apply_model_predictions(blocks_lcdm_active, lcdm, "LCDM")
    _apply_model_predictions(blocks_rll_active, rll, "RLL_like+AGN")

    chi2_lcdm = _chi2_blocks(blocks_lcdm_active)
    chi2_rll = _chi2_blocks(blocks_rll_active)
    total_observables = int(sum(len(block["obs"]) for block in blocks_lcdm_active))

    active_datasets = ",".join(block["name"] for block in blocks_lcdm_active)

    k_lcdm = len(fit_params_lcdm)
    k_rll = len(fit_params_rll)

    rows.append(dict(model="LCDM", chi2=chi2_lcdm, AIC=aic(chi2_lcdm, k_lcdm), BIC=bic(chi2_lcdm, k_lcdm, total_observables),
                     N=total_observables, k=k_lcdm, fit_params=",".join(fit_params_lcdm), fixed_params=",".join(fixed_params_lcdm),
                     datasets_used=active_datasets, run_name=cfg_meta.get("run_name", "unknown"), covariance_policy=covariance_policy))
    rows.append(dict(model="RLL_like+AGN", chi2=chi2_rll, AIC=aic(chi2_rll, k_rll), BIC=bic(chi2_rll, k_rll, total_observables),
                     N=total_observables, k=k_rll, fit_params=",".join(fit_params_rll), fixed_params=",".join(fixed_params_rll),
                     datasets_used=active_datasets, run_name=cfg_meta.get("run_name", "unknown"), covariance_policy=covariance_policy))

    out = os.path.join(RESULTS, "model_comparison.csv")
    df = evaluate_model(rows, out)
    return df, out


def run_bayesian_evidence(cfg_meta, datasets):
    """# Bloco 2: Evidência Bayesiana."""
    hz_entry = None
    fs_entry = None
    for dataset_id, entry in datasets.items():
        observable = str(entry.get("observable", dataset_id)).lower()
        if hz_entry is None and "hz" in observable:
            hz_entry = entry
        if fs_entry is None and "fs" in observable:
            fs_entry = entry

    data_hz = _to_inference_frame(hz_entry, "Hz") if hz_entry is not None else None
    data_fs8 = _to_inference_frame(fs_entry, "fs8") if fs_entry is not None else None
    if data_hz is None or data_fs8 is None:
        print("[bayes] skipped: requires Hz + fσ8 datasets with diagonal sigma errors")
        return None, None

    rows = []
    for model_name in ["LCDM", "RLL_like+AGN"]:
        result = run_nested_dynesty(model_name, data_hz, data_fs8)
        rows.append(
            {
                "model": model_name,
                "logZ": result["logZ"],
                "logZ_err": result["logZ_err"],
                "datasets_used": ",".join(cfg_meta["active_datasets"]),
                "run_name": cfg_meta.get("run_name", "unknown"),
            }
        )

    out = os.path.join(RESULTS, "bayesian_evidence.csv")
    df = evaluate_model(rows, out)
    return df, out


def main(config_path=DEFAULT_CONFIG, profile_name=DEFAULT_PROFILE, covariance_policy=None, bayes=False):
    os.makedirs(RESULTS, exist_ok=True)

    cfg = load_run_config(config_path)
    cfg_meta, datasets = load_active_datasets(config_path, profile_name=profile_name)
    covariance_policy, active_blocks, block_reports = _apply_covariance_policy(cfg, datasets, covariance_policy)

    # Bloco 1: Métrica clássica (χ²/AIC/BIC)
    df, out = run_classic_metrics(cfg_meta, datasets, covariance_policy)

    cov_rows = []
    for model_name, active_blocks in (("LCDM", blocks_lcdm_active), ("RLL_like+AGN", blocks_rll_active)):
        summary_df = covariance_usage_summary(active_blocks)
        summary_df.insert(0, "model", model_name)
        cov_rows.append(summary_df)
    cov_out = os.path.join(RESULTS, "covariance_usage.csv")
    evaluate_model(summary_rows, cov_out)

    print(df.to_string(index=False))
    print(f"\nWrote: {out}")
    print(f"Wrote: {cov_out}")

    # Bloco 2: Evidência Bayesiana
    if bayes:
        bayes_df, bayes_out = run_bayesian_evidence(cfg_meta, datasets)
        if bayes_df is not None:
            print("\nBayesian evidence:")
            print(bayes_df.to_string(index=False))
            print(f"Wrote: {bayes_out}")


def _build_arg_parser():
    parser = argparse.ArgumentParser(description="Run Structure D model comparison pipeline")
    parser.add_argument("--config", default=DEFAULT_CONFIG, help="Path to dataset config JSON")
    parser.add_argument("--profile", default=DEFAULT_PROFILE, help="Profile name from config")
    parser.add_argument("--covariance-policy", default=None, choices=["prefer_full", "diagonal_only", "full_required"], help="Covariance handling policy")
    parser.add_argument("--bayes", action="store_true", help="Enable Bayesian evidence estimation via dynesty")
    return parser


if __name__ == "__main__":
    parser = _build_arg_parser()
    args = parser.parse_args()
    env_profile = os.environ.get("STRUCTURE_D_PROFILE")
    selected_profile = args.profile if args.profile is not None else env_profile
    main(config_path=args.config, profile_name=selected_profile, covariance_policy=args.covariance_policy, bayes=args.bayes)
