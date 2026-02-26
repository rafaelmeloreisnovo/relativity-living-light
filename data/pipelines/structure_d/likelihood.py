"""Referência explícita de saídas textuais deste módulo/pipeline."""

TEXTUAL_OUTPUTS = []

import numpy as np
import pandas as pd


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
