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

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RESULTS = os.path.join(BASE_DIR, "results", "structure_d")
DEFAULT_CONFIG = os.path.join("data", "pipelines", "structure_d", "datasets_config.json")
DEFAULT_PROFILE = None

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
    return candidate_paths[-1] if candidate_paths else None


def _apply_covariance_policy(cfg, datasets, covariance_policy):
    policy = covariance_policy or cfg.get("covariance_policy", "prefer_full")
    if policy not in {"prefer_full", "diagonal_only", "full_required"}:
        raise ValueError(f"unsupported covariance_policy: {policy}")

    required_blocks = set(cfg.get("full_required_blocks", []))
    if policy == "full_required" and not required_blocks:
        required_blocks = {_dataset_block_name(dataset_id, entry) for dataset_id, entry in datasets.items()}

    block_reports = []
    active_blocks = []

    for dataset_id, entry in datasets.items():
        block_name = _dataset_block_name(dataset_id, entry)
        active_blocks.append(block_name)

        desc = cfg["datasets"][dataset_id]
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
            if has_cov_file:
                cov = np.loadtxt(cov_path, delimiter=",")
                cov = _validate_covariance_shape(cov, obs_size, dataset_id, cov_path)
                entry["covariance"] = cov
                entry["errors"] = None
                mode = "full_covariance"
                source = "file"
            elif has_cov_in_entry and policy == "prefer_full":
                cov = _validate_covariance_shape(entry["covariance"], obs_size, dataset_id, "config_entry")
                entry["covariance"] = cov
                entry["errors"] = None
                mode = "full_covariance"
                source = "file"
            elif has_sigma:
                entry["covariance"] = None
                mode = "diagonal_sigma"
                source = "fallback"
            else:
                message = f"covariance required but missing sigma fallback for dataset {dataset_id}"
                if policy == "full_required" and block_name in required_blocks:
                    raise ValueError(f"full_required policy failed: missing covariance for block {block_name} ({dataset_id})")
                raise ValueError(message)

            if policy == "full_required" and block_name in required_blocks and mode != "full_covariance":
                raise ValueError(f"full_required policy failed: missing covariance file for block {block_name} ({dataset_id})")

        block_reports.append(
            {
                "dataset_id": dataset_id,
                "block": block_name,
                "covariance_mode": mode,
                "source": source,
                "covariance_path": cov_path if source == "file" else "",
                "has_full_covariance": mode == "full_covariance",
                "has_diagonal_sigma": entry.get("errors") is not None,
            }
        )

    return policy, active_blocks, block_reports


def covariance_usage_summary(block_reports, diagonal_fallback=True):
    rows = []
    for report in block_reports:
        rows.append(
            {
                "block": report["block"],
                "dataset_id": report["dataset_id"],
                "covariance_mode": report["covariance_mode"],
                "source": report["source"],
                "covariance_path": report["covariance_path"],
                "has_full_covariance": bool(report["has_full_covariance"]),
                "has_diagonal_sigma": bool(report["has_diagonal_sigma"]),
                "diagonal_fallback": bool(diagonal_fallback),
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

    chi2_lcdm = 0.0
    chi2_rll = 0.0
    total_observables = 0

    for dataset_id, entry in datasets.items():
        c2_l, c2_r, n_obs = _evaluate_supported_dataset(dataset_id, entry, lcdm, rll)
        chi2_lcdm += c2_l
        chi2_rll += c2_r
        total_observables += n_obs

    if total_observables <= 0:
        raise ValueError("no supported observables were evaluated; check profile active_datasets")

    active_datasets = ",".join(cfg_meta["active_datasets"])

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

    cov_rows = []
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
    cov_rows.append(summary_df)

    cov_out = os.path.join(RESULTS, "covariance_usage.csv")
    evaluate_model([r for d in cov_rows for r in d.to_dict(orient="records")], cov_out)

    bayes_rows = _build_bayes_evidence_rows(rows)
    bayes_out = os.path.join(RESULTS, "bayes_evidence.csv")
    bayes_df = evaluate_model(bayes_rows, bayes_out)

    print(df.to_string(index=False))
    print(f"\nWrote: {out}")
    print(f"Wrote: {cov_out}")
    print(f"Wrote: {bayes_out}")
    print("\nBayesian evidence summary")
    print(bayes_df.to_string(index=False))


if __name__ == "__main__":
    env_profile = os.environ.get("STRUCTURE_D_PROFILE")
    main(profile_name=env_profile)
