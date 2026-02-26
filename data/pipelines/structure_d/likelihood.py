"""Referência explícita de saídas textuais deste módulo/pipeline."""

TEXTUAL_OUTPUTS = []

import numpy as np
import pandas as pd


def _as_1d_finite_array(name, values):
    arr = np.asarray(values, dtype=float)
    if arr.ndim != 1:
        raise ValueError(f"{name} must be a 1D array")
    if np.any(~np.isfinite(arr)):
        raise ValueError(f"{name} must contain only finite values")
    return arr


def _validated_sigma_array(sigma):
    sigma_arr = _as_1d_finite_array("sigma", sigma)
    if np.any(sigma_arr <= 0):
        raise ValueError("sigma must contain only finite, strictly positive values")
    return sigma_arr


def _validated_covariance_matrix(cov, expected_size=None):
    cov_arr = np.asarray(cov, dtype=float)
    if cov_arr.ndim != 2 or cov_arr.shape[0] != cov_arr.shape[1]:
        raise ValueError("covariance must be a finite square matrix")
    if expected_size is not None and cov_arr.shape[0] != expected_size:
        raise ValueError("covariance size must match observations size")
    if np.any(~np.isfinite(cov_arr)):
        raise ValueError("covariance must contain only finite values")
    if np.any(np.diag(cov_arr) <= 0):
        raise ValueError("covariance diagonal must be strictly positive")
    return cov_arr


def chi2(obs, mod, sigma):
    sigma = _validated_sigma_array(sigma)
    r = (obs - mod) / sigma
    return float(np.sum(r * r))


def chi2_with_covariance(obs, mod, covariance):
    obs_arr = np.asarray(obs, dtype=float)
    mod_arr = np.asarray(mod, dtype=float)
    if obs_arr.shape != mod_arr.shape:
        raise ValueError("obs and mod must have the same shape")
    cov = _validated_covariance_matrix(covariance, expected_size=obs_arr.shape[0])
    residual = obs_arr - mod_arr
    solved = np.linalg.solve(cov, residual)
    return float(residual @ solved)


def aic(chi2_val, k):
    return float(chi2_val + 2 * k)


def bic(chi2_val, k, N):
    return float(chi2_val + k * np.log(N))


def load_csv(path, required_cols):
    df = pd.read_csv(path)
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"CSV {path} missing columns: {missing}")
    return df


def evaluate_model(results_rows, out_csv):
    df = pd.DataFrame(results_rows)
    df.to_csv(out_csv, index=False)
    return df


def _estimate_tau_fallback_1d(samples_1d):
    x = np.asarray(samples_1d, dtype=float)
    x = x[np.isfinite(x)]
    n = x.size
    if n < 20:
        return np.nan

    x = x - np.mean(x)
    var = np.var(x)
    if not np.isfinite(var) or var <= 0:
        return np.nan

    acf = np.correlate(x, x, mode="full")[n - 1:] / (var * n)
    if acf.size < 3:
        return np.nan

    negative = np.where(acf[1:] <= 0)[0]
    max_lag = int(negative[0] + 1) if negative.size else int(min(n // 2, 2000))
    if max_lag <= 1:
        return np.nan

    tau = 1.0 + 2.0 * np.sum(acf[1:max_lag])
    if not np.isfinite(tau) or tau <= 0:
        return np.nan
    return float(tau)


def run_mcmc_emcee(
    log_prob_fn,
    initial_state,
    n_steps,
    output_dir,
    model_name,
    param_names=None,
    burn_in=0,
    thin=1,
    progress=False,
):
    if emcee is None:
        raise ImportError("run_mcmc_emcee requires the 'emcee' package")

    initial_state = np.asarray(initial_state, dtype=float)
    if initial_state.ndim != 2:
        raise ValueError("initial_state must have shape (n_walkers, n_dim)")

    n_walkers, n_dim = initial_state.shape
    if n_steps <= 0:
        raise ValueError("n_steps must be > 0")
    if thin <= 0:
        raise ValueError("thin must be > 0")
    if burn_in < 0 or burn_in >= n_steps:
        raise ValueError("burn_in must satisfy 0 <= burn_in < n_steps")

    if param_names is None:
        param_names = [f"param_{i}" for i in range(n_dim)]
    if len(param_names) != n_dim:
        raise ValueError("param_names length must match initial_state dimension")

    sampler = emcee.EnsembleSampler(n_walkers, n_dim, log_prob_fn)
    sampler.run_mcmc(initial_state, n_steps, progress=progress)

    chain = sampler.get_chain(discard=burn_in, thin=thin, flat=False)
    flat_samples = sampler.get_chain(discard=burn_in, thin=thin, flat=True)

    acceptance_mean = float(np.mean(sampler.acceptance_fraction))
    tau_values = np.full(n_dim, np.nan, dtype=float)
    tau_method = ["fallback"] * n_dim
    warnings = []

    try:
        tau_est = np.asarray(sampler.get_autocorr_time(discard=burn_in, thin=thin, tol=0), dtype=float)
        if tau_est.shape == (n_dim,):
            tau_values = tau_est
            tau_method = ["emcee.integrated_time"] * n_dim
    except Exception as exc:
        warnings.append(f"Autocorrelation by emcee failed ({type(exc).__name__}); using fallback estimator.")

    for i in range(n_dim):
        if not np.isfinite(tau_values[i]) or tau_values[i] <= 0:
            fallback_tau = _estimate_tau_fallback_1d(chain[:, :, i].reshape(-1))
            tau_values[i] = fallback_tau
            tau_method[i] = "fallback"
            if not np.isfinite(fallback_tau):
                warnings.append(f"Tau unavailable for parameter '{param_names[i]}' (chain too short or ill-conditioned).")

    total_samples = flat_samples.shape[0]
    ess_values = np.where(np.isfinite(tau_values) & (tau_values > 0), total_samples / tau_values, np.nan)

    if acceptance_mean < 0.15 or acceptance_mean > 0.70:
        warnings.append(
            f"Acceptance fraction mean {acceptance_mean:.3f} outside recommended range [0.15, 0.70]."
        )

    for i, tau in enumerate(tau_values):
        if np.isfinite(tau) and chain.shape[0] < 50.0 * tau:
            warnings.append(
                f"Autocorrelation criterion not met for '{param_names[i]}': effective chain length {chain.shape[0]} < 50*tau ({50.0*tau:.1f})."
            )

    warning_msg = " | ".join(dict.fromkeys(warnings)) if warnings else ""
    rows = []
    for i, name in enumerate(param_names):
        q16, q50, q84 = np.quantile(flat_samples[:, i], [0.16, 0.5, 0.84])
        rows.append(
            {
                "model": model_name,
                "parameter": name,
                "acceptance_fraction_mean": acceptance_mean,
                "tau_integrated": tau_values[i],
                "tau_method": tau_method[i],
                "ess_approx": ess_values[i],
                "q16": float(q16),
                "q50": float(q50),
                "q84": float(q84),
                "warning": warning_msg,
            }
        )

    import os

    os.makedirs(output_dir, exist_ok=True)
    diagnostics_path = os.path.join(output_dir, f"mcmc_diagnostics_{model_name}.csv")
    pd.DataFrame(rows).to_csv(diagnostics_path, index=False)

    return {
        "sampler": sampler,
        "chain": chain,
        "flat_samples": flat_samples,
        "diagnostics_path": diagnostics_path,
        "diagnostics": rows,
    }
