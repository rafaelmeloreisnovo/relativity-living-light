import numpy as np
import pandas as pd


BAYES_FACTOR_INTERPRETATION_ROWS = [
    {
        "lnB_min": -np.inf,
        "lnB_max": -5.0,
        "classification": "very_strong_against_model_1",
        "notes": "Jeffreys/Trotta: evidence strongly favors model_0 over model_1.",
    },
    {
        "lnB_min": -5.0,
        "lnB_max": -2.5,
        "classification": "moderate_against_model_1",
        "notes": "Jeffreys/Trotta: moderate evidence against model_1.",
    },
    {
        "lnB_min": -2.5,
        "lnB_max": -1.0,
        "classification": "weak_against_model_1",
        "notes": "Jeffreys/Trotta: weak evidence against model_1.",
    },
    {
        "lnB_min": -1.0,
        "lnB_max": 1.0,
        "classification": "inconclusive",
        "notes": "Jeffreys/Trotta: inconclusive or not worth more than a bare mention.",
    },
    {
        "lnB_min": 1.0,
        "lnB_max": 2.5,
        "classification": "weak_for_model_1",
        "notes": "Jeffreys/Trotta: weak evidence supporting model_1.",
    },
    {
        "lnB_min": 2.5,
        "lnB_max": 5.0,
        "classification": "moderate_for_model_1",
        "notes": "Jeffreys/Trotta: moderate evidence supporting model_1.",
    },
    {
        "lnB_min": 5.0,
        "lnB_max": np.inf,
        "classification": "very_strong_for_model_1",
        "notes": "Jeffreys/Trotta: strong to very strong evidence supporting model_1.",
    },
]


def _as_1d_finite_array(name, values):
    arr = np.asarray(values, dtype=float)
    if arr.ndim != 1:
        raise ValueError(f"{name} must be a 1D finite array")
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


def write_bayes_factor_interpretation(out_csv):
    df = pd.DataFrame(BAYES_FACTOR_INTERPRETATION_ROWS)
    df.to_csv(out_csv, index=False)
    return df
