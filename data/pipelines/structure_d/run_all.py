import argparse
import os

import numpy as np
import pandas as pd

from .data_access import load_active_datasets
from .likelihood import (
    aic,
    bic,
    canonical_model_name,
    chi2,
    chi2_with_covariance,
    estimate_log_evidence,
    evaluate_model,
)
from .models import model_LCDM_Hz, model_RLL_like_Hz, model_LCDM_fs8, model_RLL_like_fs8
from .sensitivity import analyze_rll_degeneracy, top_degenerate_pairs_by_bin

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RESULTS = os.path.join(BASE_DIR, "results", "structure_d")
DEFAULT_CONFIG = os.path.join("data", "pipelines", "structure_d", "datasets_config.json")

BLOCK_COVARIANCE_FILENAMES = {
    "SNe": "cov_sne.csv",
    "BAO": "cov_bao.csv",
    "fσ8": "cov_fsigma8.csv",
    "lenses": "cov_lenses.csv",
}
DATASET_BLOCK_ALIASES = {
    "hz": "Hz",
    "real_hz": "Hz",
    "fsigma8": "fσ8",
    "real_bao": "BAO",
    "sne": "SNe",
    "lenses": "lenses",
}


def _dataset_block_name(dataset_id, entry):
    if dataset_id in DATASET_BLOCK_ALIASES:
        return DATASET_BLOCK_ALIASES[dataset_id]
    observable = str(entry.get("observable", dataset_id)).lower()
    if "bao" in observable:
        return "BAO"
    if "lens" in observable:
        return "lenses"
    if "sne" in observable or "supernova" in observable:
        return "SNe"
    if "fs" in observable:
        return "fσ8"
    return str(entry.get("observable", dataset_id))


def _validate_covariance_shape(covariance, obs_size, dataset_id, cov_path):
    cov = np.asarray(covariance, dtype=float)
    if cov.ndim != 2 or cov.shape[0] != cov.shape[1]:
        raise ValueError(f"covariance for {dataset_id} must be a square matrix: {cov_path}")
    if cov.shape != (obs_size, obs_size):
        raise ValueError(
            f"covariance shape mismatch for {dataset_id}: expected {(obs_size, obs_size)}, got {cov.shape} ({cov_path})"
        )
    return cov


def _resolve_covariance_file_path(dataset_desc, block_name):
    candidate_paths = []
    if dataset_desc.get("covariance_path"):
        candidate_paths.append(os.path.join(BASE_DIR, dataset_desc["covariance_path"]))
    dataset_path = os.path.join(BASE_DIR, dataset_desc["path"])
    block_filename = BLOCK_COVARIANCE_FILENAMES.get(block_name)
    if block_filename:
        candidate_paths.append(os.path.join(os.path.dirname(dataset_path), block_filename))
    for path in candidate_paths:
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


def _apply_covariance_policy(run_cfg, datasets, covariance_policy):
    policy = covariance_policy or run_cfg.get("covariance_policy", "prefer_full")
    if policy not in {"prefer_full", "diagonal_only", "full_required"}:
        raise ValueError(f"unsupported covariance_policy: {policy}")

    required_blocks = set(run_cfg.get("full_required_blocks", []))
    if policy == "full_required" and not required_blocks:
        required_blocks = {_dataset_block_name(dataset_id, entry) for dataset_id, entry in datasets.items()}

    cov = _find_covariance_file(block_name)
    if sigma_col is None and cov is None:
        raise ValueError(
            f"{os.path.basename(path)} requires 'sigma' for diagonal fallback or an external covariance matrix"
        )

    for dataset_id, entry in datasets.items():
        block_name = _dataset_block_name(dataset_id, entry)
        active_blocks.append(block_name)

        desc = run_cfg["datasets"][dataset_id]
        obs_size = len(entry["values"])
        cov_path = _resolve_covariance_file_path(desc, block_name)
        has_cov_file = bool(cov_path and os.path.exists(cov_path))
        has_sigma = entry.get("errors") is not None
        has_cov_in_entry = entry.get("covariance") is not None

        if policy == "diagonal_only":
            if has_sigma:
                entry["covariance"] = None
                mode = "diagonal_sigma"
                source = "fallback"
            elif has_cov_in_entry:
                sigma = np.sqrt(np.diag(np.asarray(entry["covariance"], dtype=float)))
                if len(sigma) != obs_size:
                    raise ValueError(f"covariance diagonal length mismatch for {dataset_id}")
                entry["errors"] = sigma
                entry["covariance"] = None
                mode = "diagonal_from_covariance"
                source = "fallback"
            else:
                raise ValueError(f"dataset {dataset_id} has neither sigma nor covariance to build diagonal-only likelihood")
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

    if dataset_id in {"hz", "real_hz"}:
        lcdm_values = model_LCDM_Hz(z_values, lcdm)
        rll_values = model_RLL_like_Hz(z_values, rll)
    elif dataset_id == "fsigma8":
        lcdm_values = model_LCDM_fs8(z_values, lcdm)
        rll_values = model_RLL_like_fs8(z_values, rll)
    else:
        return 0.0, 0.0, 0

    chi2_lcdm = _chi2_from_entry(entry, lcdm_values)
    chi2_rll = _chi2_from_entry(entry, rll_values)
    return chi2_lcdm, chi2_rll, len(entry["values"])


def _build_bayes_evidence_rows(model_rows):
    evidence_rows = []
    for row in model_rows:
        logz, logz_err = estimate_log_evidence(chi2_val=row["chi2"], k=row["k"], n_obs=row["N"])
        evidence_rows.append(
            {
                "model": canonical_model_name(row["model"]),
                "logZ": logz,
                "logZ_err": logz_err,
            }
        )
    return evidence_rows


def main(config_path=DEFAULT_CONFIG, profile_name=DEFAULT_PROFILE, covariance_policy=None):
    os.makedirs(RESULTS, exist_ok=True)
    rows = []

    cfg_meta, datasets = load_active_datasets(config_path, profile_name=profile_name)

    import json
    with open(os.path.join(BASE_DIR, config_path), "r", encoding="utf-8") as f:
        cfg = json.load(f)

    covariance_policy, active_blocks, block_reports = _apply_covariance_policy(cfg, datasets, covariance_policy)

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

    active_datasets = ",".join(cfg["active_datasets"])

    k_lcdm = len(fit_params_lcdm)
    k_rll = len(fit_params_rll)

    rows.append(
        dict(
            model="LCDM",
            chi2=chi2_lcdm,
            AIC=aic(chi2_lcdm, k_lcdm),
            BIC=bic(chi2_lcdm, k_lcdm, total_observables),
            N=total_observables,
            k=k_lcdm,
            fit_params=",".join(fit_params_lcdm),
            fixed_params=",".join(fixed_params_lcdm),
            datasets_used=active_datasets,
            run_name=cfg_meta.get("run_name", "unknown"),
            covariance_policy=covariance_policy,
        )
    )
    rows.append(
        dict(
            model="RLL_like+AGN",
            chi2=chi2_rll,
            AIC=aic(chi2_rll, k_rll),
            BIC=bic(chi2_rll, k_rll, total_observables),
            N=total_observables,
            k=k_rll,
            fit_params=",".join(fit_params_rll),
            fixed_params=",".join(fixed_params_rll),
            datasets_used=active_datasets,
            run_name=cfg_meta.get("run_name", "unknown"),
            covariance_policy=covariance_policy,
        )
    )

    out = os.path.join(RESULTS, "model_comparison.csv")
    df = evaluate_model(rows, out)
    return df, out

    expected_blocks = ["SNe", "BAO", "fσ8", "lenses", "Hz"]
    summary_df = covariance_usage_summary(block_reports, diagonal_fallback=True)
    missing = [
        {
            "block": b,
            "dataset_id": "",
            "covariance_mode": "not_used",
            "source": "fallback",
            "covariance_path": "",
            "has_full_covariance": False,
            "has_diagonal_sigma": False,
            "diagonal_fallback": True,
        }
        for b in expected_blocks
        if b not in set(summary_df["block"].tolist())
    ]
    if missing:
        summary_df = pd.concat([summary_df, pd.DataFrame(missing)], ignore_index=True)
    summary_df.insert(0, "covariance_policy", covariance_policy)
    summary_df.insert(1, "active_blocks", ",".join(active_blocks))

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
    evaluate_model(summary_df.to_dict(orient="records"), cov_out)

    out_lcdm, out_rll = _save_model_posteriors(lcdm, rll, chi2_lcdm, chi2_rll)

    bayes_rows = _build_bayes_evidence_rows(rows)
    bayes_out = os.path.join(RESULTS, "bayes_evidence.csv")
    bayes_df = evaluate_model(bayes_rows, bayes_out)

    print(df.to_string(index=False))
    print("\nPosterior convention: loglike = -0.5 * chi2_total; uniform prior -> logpost = loglike (up to additive constant).")
    print(f"\nWrote: {out}")
    print(f"Wrote: {cov_out}")
    print(f"Wrote: {bayes_out}")
    print("\nBayesian evidence summary")
    print(bayes_df.to_string(index=False))


if __name__ == "__main__":
    args = _build_parser().parse_args()
    main(config_path=args.config, covariance_policy=args.covariance_policy, profile_name=args.profile, bayes=args.bayes)
