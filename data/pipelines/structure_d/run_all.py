import argparse
import os
import numpy as np

from .data_access import load_active_datasets
from .inference import run_lcdm_bayes, run_rll_like_agn_bayes
from .likelihood import chi2, chi2_with_covariance, aic, bic, evaluate_model
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
    return rows


def _chi2_from_entry(entry, model_values):
    if entry["errors"] is not None:
        return chi2(entry["values"], model_values, entry["errors"])
    return chi2_with_covariance(entry["values"], model_values, entry["covariance"])


def _evaluate_supported_dataset(dataset_id, entry, lcdm, rll):
    if entry.get("z") is None:
        return 0.0, 0.0, 0

    if dataset_id in {"hz", "real_hz"} or str(entry.get("observable", "")).lower() == "hz":
        model_lcdm = model_LCDM_Hz(entry["z"], lcdm)
        model_rll = model_RLL_like_Hz(entry["z"], rll)
    elif dataset_id == "fsigma8" or "fs" in str(entry.get("observable", "")).lower():
        model_lcdm = model_LCDM_fs8(entry["z"], lcdm)
        model_rll = model_RLL_like_fs8(entry["z"], rll)
    else:
        return 0.0, 0.0, 0

    chi2_l = _chi2_from_entry(entry, model_lcdm)
    chi2_r = _chi2_from_entry(entry, model_rll)
    return chi2_l, chi2_r, len(entry["values"])


def _save_bayes_results(datasets, seed, nwalkers, nsteps, nlive):
    hz = datasets.get("hz") or datasets.get("real_hz")
    fs8 = datasets.get("fsigma8")
    if hz is None or fs8 is None:
        raise ValueError("Bayes mode requires both hz and fsigma8 datasets active in profile")

    lcdm_result = run_lcdm_bayes(hz, fs8, seed=seed, nwalkers=nwalkers, nsteps=nsteps, nlive=nlive, output_dir=RESULTS)
    rll_result = run_rll_like_agn_bayes(hz, fs8, seed=seed, nwalkers=nwalkers, nsteps=nsteps, nlive=nlive, output_dir=RESULTS)

    rows = [lcdm_result["row"], rll_result["row"]]
    bayes_out = os.path.join(RESULTS, "bayes_model_comparison.csv")
    evaluate_model(rows, bayes_out)
    print(f"Wrote: {bayes_out}")


def main(config_path=DEFAULT_CONFIG, profile_name=DEFAULT_PROFILE, covariance_policy=None, run_bayes=False,
         seed=42, nwalkers=32, nsteps=2000, nlive=400):
    os.makedirs(RESULTS, exist_ok=True)
    rows = []

    cfg, datasets = load_active_datasets(config_path, profile_name=profile_name)
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

    active_datasets = ",".join(cfg["active_datasets"])

    k_lcdm = len(fit_params_lcdm)
    k_rll = len(fit_params_rll)

    rows.append(dict(model="LCDM", chi2=chi2_lcdm, AIC=aic(chi2_lcdm, k_lcdm), BIC=bic(chi2_lcdm, k_lcdm, total_observables),
                     N=total_observables, k=k_lcdm, fit_params=",".join(fit_params_lcdm), fixed_params=",".join(fixed_params_lcdm),
                     datasets_used=active_datasets, run_name=cfg.get("run_name", "unknown"), covariance_policy=covariance_policy))
    rows.append(dict(model="RLL_like+AGN", chi2=chi2_rll, AIC=aic(chi2_rll, k_rll), BIC=bic(chi2_rll, k_rll, total_observables),
                     N=total_observables, k=k_rll, fit_params=",".join(fit_params_rll), fixed_params=",".join(fixed_params_rll),
                     datasets_used=active_datasets, run_name=cfg.get("run_name", "unknown"), covariance_policy=covariance_policy))

    out = os.path.join(RESULTS, "model_comparison.csv")
    df = evaluate_model(rows, out)

    expected_blocks = ["SNe", "BAO", "fσ8", "lenses", "Hz"]
    summary_rows = covariance_usage_summary(block_reports, diagonal_fallback=True)
    used_blocks = {row["block"] for row in summary_rows}
    for block in expected_blocks:
        if block not in used_blocks:
            summary_rows.append(
                {
                    "block": block,
                    "dataset_id": "",
                    "covariance_mode": "not_used",
                    "source": "fallback",
                    "covariance_path": "",
                    "has_full_covariance": False,
                    "has_diagonal_sigma": False,
                    "diagonal_fallback": True,
                }
            )
    for row in summary_rows:
        row["covariance_policy"] = covariance_policy
        row["active_blocks"] = ",".join(active_blocks)

    cov_out = os.path.join(RESULTS, "covariance_usage.csv")
    evaluate_model(summary_rows, cov_out)

    print(df.to_string(index=False))
    print(f"\nWrote: {out}")
    print(f"Wrote: {cov_out}")

    if run_bayes:
        _save_bayes_results(datasets, seed=seed, nwalkers=nwalkers, nsteps=nsteps, nlive=nlive)


def _parse_args():
    parser = argparse.ArgumentParser(description="Run structure_d model comparison pipeline")
    parser.add_argument("--config", default=DEFAULT_CONFIG)
    parser.add_argument("--profile", default=DEFAULT_PROFILE)
    parser.add_argument("--covariance-policy", default=None)
    parser.add_argument("--bayes", action="store_true")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--nwalkers", type=int, default=32)
    parser.add_argument("--nsteps", type=int, default=2000)
    parser.add_argument("--nlive", type=int, default=400)
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    env_profile = os.environ.get("STRUCTURE_D_PROFILE")
    chosen_profile = args.profile if args.profile is not None else env_profile
    main(
        config_path=args.config,
        profile_name=chosen_profile,
        covariance_policy=args.covariance_policy,
        run_bayes=args.bayes,
        seed=args.seed,
        nwalkers=args.nwalkers,
        nsteps=args.nsteps,
        nlive=args.nlive,
    )
