import argparse
import os

import numpy as np
import pandas as pd

from .data_access import load_active_datasets, load_run_config
from .likelihood import chi2, chi2_with_covariance, aic, bic, evaluate_model
from .models import model_LCDM_Hz, model_RLL_like_Hz, model_LCDM_fs8, model_RLL_like_fs8
from .sensitivity import analyze_rll_degeneracy, top_degenerate_pairs_by_bin

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
    if entry.get("z") is None:
        raise ValueError(f"dataset {dataset_id} does not provide z values")

    z = np.asarray(entry["z"], dtype=float)
    block_name = _dataset_block_name(dataset_id, entry)

    if block_name == "Hz":
        c2_l = _chi2_from_entry(entry, model_LCDM_Hz(z, lcdm))
        c2_r = _chi2_from_entry(entry, model_RLL_like_Hz(z, rll))
    elif block_name == "fσ8":
        c2_l = _chi2_from_entry(entry, model_LCDM_fs8(z, lcdm))
        c2_r = _chi2_from_entry(entry, model_RLL_like_fs8(z, rll))
    else:
        raise ValueError(f"unsupported dataset for current model set: {dataset_id} ({block_name})")

    return float(c2_l), float(c2_r), int(len(entry["values"]))


def _artifact_kind(file_path):
    name = os.path.basename(file_path).lower()
    bayes_tokens = ("bayes", "evidence", "posterior", "nested", "mcmc")
    return "bayes" if any(token in name for token in bayes_tokens) else "classic"


def _print_written_artifact(file_path, kind):
    print(f"[{kind}] wrote: {os.path.abspath(file_path)}")


def _print_all_result_artifacts(results_dir, bayes, skip_paths=None):
    skip_paths = {os.path.abspath(path) for path in (skip_paths or [])}
    bayes_count = 0
    for name in sorted(os.listdir(results_dir)):
        artifact = os.path.abspath(os.path.join(results_dir, name))
        if artifact in skip_paths or not os.path.isfile(artifact):
            continue
        kind = _artifact_kind(artifact)
        if kind == "bayes":
            bayes_count += 1
            if not bayes:
                continue
        _print_written_artifact(artifact, kind)
    if bayes and bayes_count == 0:
        print("[bayes] wrote: none")


def main(config_path=DEFAULT_CONFIG, covariance_policy=None, profile_name=DEFAULT_PROFILE, bayes=False):
    os.makedirs(RESULTS, exist_ok=True)
    rows = []

    full_cfg = load_run_config(config_path)
    cfg_meta, datasets = load_active_datasets(config_path, profile_name=profile_name)
    covariance_policy, active_blocks, block_reports = _apply_covariance_policy(full_cfg, datasets, covariance_policy)

    lcdm = dict(H0=70.0, Om=0.3, Ol=0.7, sigma8=0.8, gamma=0.55)
    rll = dict(H0=70.0, Om=0.3, Ol=0.7, sigma8=0.8, gamma=0.55, alpha=0.06, z_peak=2.0, width=1.2, beta=0.00)

    fit_params_lcdm = ["H0", "Om", "sigma8", "gamma"]
    fit_params_rll = fit_params_lcdm + ["alpha", "z_peak", "width"]
    fixed_params_lcdm = sorted(set(lcdm) - set(fit_params_lcdm))
    fixed_params_rll = sorted(set(rll) - set(fit_params_rll))

    model_map_lcdm = {
        "hz": model_LCDM_Hz,
        "fsigma8": model_LCDM_fs8,
        "real_hz": model_LCDM_Hz,
        "real_bao": model_LCDM_BAO,
        "sne": model_LCDM_SNe,
        "lenses": model_LCDM_lenses,
    }
    model_map_rll = {
        "hz": model_RLL_like_Hz,
        "fsigma8": model_RLL_like_fs8,
        "real_hz": model_RLL_like_Hz,
        "real_bao": model_RLL_like_BAO,
        "sne": model_RLL_like_SNe,
        "lenses": model_RLL_like_lenses,
    }

    blocks_lcdm_active = []
    blocks_rll_active = []
    total_observables = 0

    for dataset_id in cfg["active_datasets"]:
        entry = datasets[dataset_id]
        z = entry.get("z")
        if z is None:
            continue

        model_fn_lcdm = model_map_lcdm.get(dataset_id)
        model_fn_rll = model_map_rll.get(dataset_id)
        if model_fn_lcdm is None or model_fn_rll is None:
            continue

        mod_lcdm = model_fn_lcdm(z, lcdm)
        mod_rll = model_fn_rll(z, rll)

        obs_lcdm, mod_lcdm = _normalize_for_block(entry, mod_lcdm, dataset_id)
        obs_rll, mod_rll = _normalize_for_block(entry, mod_rll, dataset_id)

        block_name = _dataset_block_name(entry)
        block_common = {
            "block": block_name,
            "observable": entry.get("observable", block_name),
            "N": len(entry["values"]),
            "errors": entry.get("errors"),
            "covariance": entry.get("covariance"),
        }

        blocks_lcdm_active.append({**block_common, "obs": obs_lcdm, "mod": mod_lcdm})
        blocks_rll_active.append({**block_common, "obs": obs_rll, "mod": mod_rll})
        total_observables += len(entry["values"])

    chi2_lcdm = chi2_blocks(blocks_lcdm_active)
    chi2_rll = chi2_blocks(blocks_rll_active)

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
        summary_df = covariance_usage_summary(active_blocks, diagonal_fallback=True)
        missing = [
            {"block": b, "observable": b, "N": 0, "covariance_mode": "not_used", "has_full_covariance": False, "has_diagonal_sigma": False}
            for b in expected_blocks if b not in set(summary_df["block"].tolist())
        ]
        if missing:
            summary_df = pd.concat([summary_df, pd.DataFrame(missing)], ignore_index=True)
        summary_df.insert(0, "model", model_name)
        cov_rows.append(summary_df)
    cov_out = os.path.join(RESULTS, "covariance_usage.csv")
    evaluate_model(summary_rows, cov_out)

    deg_df, deg_out = analyze_rll_degeneracy(hz, fs8, rll, RESULTS, fit_params=fit_params_rll)
    deg_pairs = top_degenerate_pairs_by_bin(deg_df, top_n=3)

    sens_out = os.path.join(RESULTS, "rll_sensitivity_derivatives.csv")
    sensitivity_table_by_redshift().to_csv(sens_out, index=False)

    deg_df, deg_out = analyze_rll_degeneracy(hz, fs8, rll, RESULTS, fit_params=fit_params_rll)
    deg_pairs = top_degenerate_pairs_by_bin(deg_df, top_n=3)

    print(df.to_string(index=False))
    _print_written_artifact(out, "classic")
    _print_written_artifact(cov_out, "classic")
    _print_all_result_artifacts(RESULTS, bayes=bayes, skip_paths=[out, cov_out])


def _build_parser():
    parser = argparse.ArgumentParser(description="Executa o pipeline structure_d")
    parser.add_argument("--config", default=DEFAULT_CONFIG)
    parser.add_argument("--profile", default=os.environ.get("STRUCTURE_D_PROFILE", DEFAULT_PROFILE))
    parser.add_argument("--covariance-policy", default=None, choices=["prefer_full", "diagonal_only", "full_required"])
    parser.add_argument("--bayes", action="store_true", help="Exibe também artefatos bayesianos gerados")
    return parser


if __name__ == "__main__":
    args = _build_parser().parse_args()
    main(config_path=args.config, covariance_policy=args.covariance_policy, profile_name=args.profile, bayes=args.bayes)
