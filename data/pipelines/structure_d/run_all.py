import argparse
import os

import numpy as np

from .data_access import load_active_datasets
from .inference import run_lcdm_bayes, run_rll_like_agn_bayes
from .likelihood import chi2, chi2_with_covariance, aic, bic, evaluate_model
from .models import model_LCDM_Hz, model_RLL_like_Hz, model_LCDM_fs8, model_RLL_like_fs8

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RESULTS = os.path.join(BASE_DIR, "results", "structure_d")
INFERENCE_RESULTS = os.path.join(RESULTS, "inference")


def _safe_float(value):
    if value is None:
        return None
    return float(value)


def _save_mcmc_outputs(result, out_dir):
    model_name = result["model_name"]
    model_slug = model_name.replace("+", "_plus_")

    npz_path = os.path.join(out_dir, f"mcmc_{model_slug}.npz")
    np.savez_compressed(
        npz_path,
        chain_flat=result["chain_flat"],
        log_prob_flat=result["log_prob_flat"],
        param_names=np.asarray(result["param_names"], dtype=object),
        acceptance_fraction_mean=np.asarray(result["acceptance_fraction_mean"], dtype=float),
        autocorr_time=np.asarray(result["autocorr_time"], dtype=float)
        if result["autocorr_time"] is not None
        else np.asarray([], dtype=float),
    )

    chain_df = pd.DataFrame(result["chain_flat"], columns=result["param_names"])
    chain_df["log_prob"] = result["log_prob_flat"]
    csv_path = os.path.join(out_dir, f"mcmc_{model_slug}.csv")
    chain_df.to_csv(csv_path, index=False)

    summary = {
        "model_name": model_name,
        "param_names": result["param_names"],
        "n_samples": int(result["chain_flat"].shape[0]),
        "n_dim": int(result["chain_flat"].shape[1]) if result["chain_flat"].ndim == 2 else 0,
        "acceptance_fraction_mean": _safe_float(result["acceptance_fraction_mean"]),
        "autocorr_time": result["autocorr_time"].tolist()
        if result["autocorr_time"] is not None
        else None,
        "burnin": int(result["burnin"]),
        "thin": int(result["thin"]),
        "npz_file": os.path.basename(npz_path),
        "csv_file": os.path.basename(csv_path),
    }
    json_path = os.path.join(out_dir, f"mcmc_{model_slug}.json")
    with open(json_path, "w", encoding="utf-8") as fp:
        json.dump(summary, fp, indent=2)

    return {"npz": npz_path, "csv": csv_path, "json": json_path}


def _save_nested_outputs(result, out_dir):
    model_name = result["model_name"]
    model_slug = model_name.replace("+", "_plus_")

    niter = len(result["results"].logl)
    npz_path = os.path.join(out_dir, f"nested_{model_slug}.npz")
    np.savez_compressed(
        npz_path,
        param_names=np.asarray(result["param_names"], dtype=object),
        logz=np.asarray(result["results"].logz, dtype=float),
        logzerr=np.asarray(result["results"].logzerr, dtype=float),
        logl=np.asarray(result["results"].logl, dtype=float),
        samples=np.asarray(result["results"].samples, dtype=float),
    )

    csv_path = os.path.join(out_dir, f"nested_{model_slug}.csv")
    pd.DataFrame(
        {
            "iteration": np.arange(niter, dtype=int),
            "logz": np.asarray(result["results"].logz, dtype=float),
            "logzerr": np.asarray(result["results"].logzerr, dtype=float),
            "logl": np.asarray(result["results"].logl, dtype=float),
        }
    ).to_csv(csv_path, index=False)

    summary = {
        "model_name": model_name,
        "param_names": result["param_names"],
        "n_samples": int(result["results"].samples.shape[0]),
        "n_dim": int(result["results"].samples.shape[1]) if result["results"].samples.ndim == 2 else 0,
        "logZ": _safe_float(result["logZ"]),
        "logZ_err": _safe_float(result["logZ_err"]),
        "npz_file": os.path.basename(npz_path),
        "csv_file": os.path.basename(csv_path),
    }
    json_path = os.path.join(out_dir, f"nested_{model_slug}.json")
    with open(json_path, "w", encoding="utf-8") as fp:
        json.dump(summary, fp, indent=2)

    return {"npz": npz_path, "csv": csv_path, "json": json_path}


def _run_inference_for_model(model_name, hz, fs8):
    out_dir = os.path.join(INFERENCE_RESULTS, model_name.replace("+", "_plus_"))
    os.makedirs(out_dir, exist_ok=True)

    prior_spec = MODEL_PARAMETER_PRIORS[model_name]
    ndim = len(prior_spec)
    nwalkers = max(2 * ndim + 2, 24)

    metadata = {
        "model_name": model_name,
        "mcmc": {"status": "not_run"},
        "nested": {"status": "not_run"},
    }

    try:
        mcmc = run_mcmc_emcee(
            model_name,
            hz,
            fs8,
            nwalkers=nwalkers,
            nsteps=500,
            burnin=125,
            thin=2,
            random_seed=42,
            progress=False,
        )
        files = _save_mcmc_outputs(mcmc, out_dir)
        metadata["mcmc"] = {
            "status": "ok",
            "acceptance_fraction_mean": _safe_float(mcmc["acceptance_fraction_mean"]),
            "autocorr_time": mcmc["autocorr_time"].tolist() if mcmc["autocorr_time"] is not None else None,
            "files": {k: os.path.basename(v) for k, v in files.items()},
        }
        print(f"Inference MCMC ({model_name}) -> {files['json']}")
    except ImportError as exc:
        metadata["mcmc"] = {"status": "skipped", "reason": str(exc)}
        print(f"Skipping MCMC ({model_name}): {exc}")

    try:
        nested = run_nested_dynesty(
            model_name,
            hz,
            fs8,
            nlive=150,
            bound="multi",
            sample="rwalk",
            random_seed=42,
        )
        files = _save_nested_outputs(nested, out_dir)
        metadata["nested"] = {
            "status": "ok",
            "logZ": _safe_float(nested["logZ"]),
            "logZ_err": _safe_float(nested["logZ_err"]),
            "files": {k: os.path.basename(v) for k, v in files.items()},
        }
        print(f"Inference nested ({model_name}) -> {files['json']}")
    except ImportError as exc:
        metadata["nested"] = {"status": "skipped", "reason": str(exc)}
        print(f"Skipping nested ({model_name}): {exc}")

    meta_path = os.path.join(out_dir, "inference_status.json")
    with open(meta_path, "w", encoding="utf-8") as fp:
        json.dump(metadata, fp, indent=2)

    return metadata

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
    os.makedirs(INFERENCE_RESULTS, exist_ok=True)
    rows = []

    cfg, datasets = load_active_datasets(config_path, profile_name=profile_name)
    covariance_policy, active_blocks, block_reports = _apply_covariance_policy(cfg, datasets, covariance_policy)

    lcdm = dict(H0=h0_seed, Om=0.3, Ol=0.7, sigma8=0.8, gamma=0.55)
    rll = dict(H0=h0_seed, Om=0.3, Ol=0.7, sigma8=0.8, gamma=0.55, alpha=0.06, z_peak=2.0, width=1.2, beta=0.00)

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
                     datasets_used=active_datasets, run_name=cfg_meta.get("run_name", "unknown"), profile_name=cfg_meta.get("profile_name", "unknown")))
    rows.append(dict(model="RLL_like+AGN", chi2=chi2_rll, AIC=aic(chi2_rll, k_rll), BIC=bic(chi2_rll, k_rll, total_observables),
                     N=total_observables, k=k_rll, fit_params=",".join(fit_params_rll), fixed_params=",".join(fixed_params_rll),
                     datasets_used=active_datasets, run_name=cfg_meta.get("run_name", "unknown"), profile_name=cfg_meta.get("profile_name", "unknown")))

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




    inference_manifest = {
        "LCDM": _run_inference_for_model("LCDM", hz, fs8),
        "RLL_like+AGN": _run_inference_for_model("RLL_like+AGN", hz, fs8),
    }
    manifest_path = os.path.join(INFERENCE_RESULTS, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as fp:
        json.dump(inference_manifest, fp, indent=2)
    print(f"Wrote: {manifest_path}")


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
