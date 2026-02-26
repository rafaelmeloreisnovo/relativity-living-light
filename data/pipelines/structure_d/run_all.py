import json
import os

import numpy as np
import pandas as pd

from .inference import (
    MODEL_PARAMETER_PRIORS,
    run_mcmc_emcee,
    run_nested_dynesty,
)
from .likelihood import aic, bic, chi2, evaluate_model, load_csv
from .models import model_LCDM_Hz, model_LCDM_fs8, model_RLL_like_Hz, model_RLL_like_fs8

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
DATA = os.path.join(BASE_DIR, "data", "inputs", "structure_d")
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


def main():
    os.makedirs(RESULTS, exist_ok=True)
    os.makedirs(INFERENCE_RESULTS, exist_ok=True)
    rows = []

    hz = load_csv(os.path.join(DATA, "Hz.csv"), ["z", "Hz", "sigma"])
    fs8 = load_csv(os.path.join(DATA, "fsigma8.csv"), ["z", "fs8", "sigma"])

    lcdm = dict(H0=70.0, Om=0.3, Ol=0.7, sigma8=0.8, gamma=0.55)
    rll = dict(H0=70.0, Om=0.3, Ol=0.7, sigma8=0.8, gamma=0.55, alpha=0.06, z_peak=2.0, width=1.2, beta=0.00)

    # Fonte única para contagem de parâmetros livres usada em AIC/BIC.
    fit_params_lcdm = ["H0", "Om", "sigma8", "gamma"]
    fit_params_rll = fit_params_lcdm + ["alpha", "z_peak", "width"]
    fixed_params_lcdm = sorted(set(lcdm) - set(fit_params_lcdm))
    fixed_params_rll = sorted(set(rll) - set(fit_params_rll))

    z_hz = hz["z"].to_numpy()
    chi2_lcdm_hz = chi2(hz["Hz"].to_numpy(), model_LCDM_Hz(z_hz, lcdm), hz["sigma"].to_numpy())
    chi2_rll_hz = chi2(hz["Hz"].to_numpy(), model_RLL_like_Hz(z_hz, rll), hz["sigma"].to_numpy())

    z_fs = fs8["z"].to_numpy()
    chi2_lcdm_fs = chi2(fs8["fs8"].to_numpy(), model_LCDM_fs8(z_fs, lcdm), fs8["sigma"].to_numpy())
    chi2_rll_fs = chi2(fs8["fs8"].to_numpy(), model_RLL_like_fs8(z_fs, rll), fs8["sigma"].to_numpy())

    chi2_lcdm = chi2_lcdm_hz + chi2_lcdm_fs
    chi2_rll = chi2_rll_hz + chi2_rll_fs
    N = len(hz) + len(fs8)

    # Convenção: k conta apenas parâmetros efetivamente calibráveis (livres).
    # Parâmetros fixos em cada modelo são documentados abaixo e não entram em k.
    k_lcdm = len(fit_params_lcdm)
    k_rll = len(fit_params_rll)

    rows.append(dict(model="LCDM", chi2=chi2_lcdm, AIC=aic(chi2_lcdm, k_lcdm), BIC=bic(chi2_lcdm, k_lcdm, N), N=N, k=k_lcdm,
                     fit_params=",".join(fit_params_lcdm), fixed_params=",".join(fixed_params_lcdm)))
    rows.append(dict(model="RLL_like+AGN", chi2=chi2_rll, AIC=aic(chi2_rll, k_rll), BIC=bic(chi2_rll, k_rll, N), N=N, k=k_rll,
                     fit_params=",".join(fit_params_rll), fixed_params=",".join(fixed_params_rll)))

    out = os.path.join(RESULTS, "model_comparison.csv")
    df = evaluate_model(rows, out)
    print(df.to_string(index=False))
    print(f"\nWrote: {out}")

    inference_manifest = {
        "LCDM": _run_inference_for_model("LCDM", hz, fs8),
        "RLL_like+AGN": _run_inference_for_model("RLL_like+AGN", hz, fs8),
    }
    manifest_path = os.path.join(INFERENCE_RESULTS, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as fp:
        json.dump(inference_manifest, fp, indent=2)
    print(f"Wrote: {manifest_path}")


if __name__ == "__main__":
    main()
