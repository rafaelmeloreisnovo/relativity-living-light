"""Referência explícita de saídas textuais deste módulo/pipeline."""

TEXTUAL_OUTPUTS = []

import numpy as np
import pandas as pd
import hashlib
import json


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
    obs_arr = _as_1d_finite_array("obs", obs)
    mod_arr = _as_1d_finite_array("mod", mod)
    sigma_arr = _validated_sigma_array(sigma)

    obs_size = obs_arr.size
    mod_size = mod_arr.size
    sigma_size = sigma_arr.size
    if obs_size != mod_size or obs_size != sigma_size:
        raise ValueError(
            "obs, mod e sigma devem ter o mesmo tamanho em chi2 "
            f"(obs={obs_size}, mod={mod_size}, sigma={sigma_size})"
        )

    r = (obs_arr - mod_arr) / sigma_arr
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


def _theta_to_dict(theta, data):
    if isinstance(theta, dict):
        return theta
    theta_arr = np.asarray(theta, dtype=float)
    if theta_arr.ndim != 1:
        raise ValueError("theta must be a dict or a 1D array")
    param_names = data.get("param_names")
    if param_names is None:
        raise ValueError("data['param_names'] is required when theta is not a dict")
    if len(param_names) != theta_arr.size:
        raise ValueError("len(param_names) must match theta length")
    return dict(zip(param_names, theta_arr))


def is_physically_stable(theta, data=None):
    data = data or {}
    params = _theta_to_dict(theta, data)

    base_constraints = (
        ("H0", lambda v: np.isfinite(v) and v > 0.0),
        ("Om", lambda v: np.isfinite(v) and 0.0 <= v <= 1.0),
        ("Or", lambda v: np.isfinite(v) and 0.0 <= v <= 1.0),
        ("Ol", lambda v: np.isfinite(v) and 0.0 <= v <= 2.0),
        ("sigma8", lambda v: np.isfinite(v) and v > 0.0),
        ("gamma", lambda v: np.isfinite(v) and 0.0 <= v <= 1.5),
        ("alpha", lambda v: np.isfinite(v) and 0.0 <= v <= 1.0),
        ("z_peak", lambda v: np.isfinite(v) and v >= 0.0),
        ("width", lambda v: np.isfinite(v) and v > 0.0),
        ("beta", lambda v: np.isfinite(v) and -2.0 <= v <= 2.0),
    )

    for name, predicate in base_constraints:
        if name in params and not predicate(float(params[name])):
            return False

    om = float(params.get("Om", 0.0))
    orad = float(params.get("Or", 0.0))
    ol = float(params.get("Ol", 0.0))
    if om + orad + ol <= 0.0:
        return False

    veto = data.get("is_physically_stable")
    if veto is not None:
        return bool(veto(params, data))
    return True


def log_prior(theta, data=None):
    data = data or {}
    params = _theta_to_dict(theta, data)

    if not is_physically_stable(params, data=data):
        return -np.inf

    prior_bounds = data.get("prior_bounds", {})
    for name, bounds in prior_bounds.items():
        if name not in params:
            continue
        lo, hi = bounds
        val = float(params[name])
        if (lo is not None and val < lo) or (hi is not None and val > hi):
            return -np.inf

    return 0.0


def _build_blocks(theta, data):
    blocks_builder = data.get("build_blocks")
    if blocks_builder is None:
        raise ValueError("data['build_blocks'] callable is required")
    blocks = blocks_builder(theta, data)
    if blocks is None:
        raise ValueError("build_blocks returned None")
    return blocks


def log_likelihood(theta, data):
    params = _theta_to_dict(theta, data)

    if not is_physically_stable(params, data=data):
        return -np.inf

    blocks = _build_blocks(params, data)
    chi2_val, _ = chi2_blocks(blocks, diagonal_fallback=data.get("diagonal_fallback", True))
    return -0.5 * chi2_val


def evaluate_posterior(theta, data, diag_accumulator=None):
    lp = log_prior(theta, data=data)
    if not np.isfinite(lp):
        if diag_accumulator is not None:
            diag_accumulator["prior_veto"] = int(diag_accumulator.get("prior_veto", 0)) + 1
        return -np.inf

    ll = log_likelihood(theta, data=data)
    if not np.isfinite(ll):
        if diag_accumulator is not None:
            diag_accumulator["physical_veto"] = int(diag_accumulator.get("physical_veto", 0)) + 1
        return -np.inf

    if diag_accumulator is not None:
        diag_accumulator["accepted"] = int(diag_accumulator.get("accepted", 0)) + 1
        diag_accumulator["last_log_prior"] = float(lp)
        diag_accumulator["last_log_likelihood"] = float(ll)

    return float(lp + ll)


def aic(chi2_val, k):
    return float(chi2_val + 2 * k)


def bic(chi2_val, k, N):
    return float(chi2_val + k * np.log(N))


def estimate_log_evidence(chi2_val=None, k=None, n_obs=None, bic_value=None):
    if bic_value is None:
        if chi2_val is None or k is None or n_obs is None:
            raise ValueError("estimate_log_evidence requires bic_value or (chi2_val, k, n_obs)")
        bic_value = bic(chi2_val, k, n_obs)

    logz = float(-0.5 * float(bic_value))
    logz_err = float("nan")
    return logz, logz_err


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


def bayes_factor_interpretation_contract():
    normalized_rows = []
    for row in BAYES_FACTOR_INTERPRETATION_ROWS:
        normalized_rows.append(
            {
                "lnB_min": "-inf" if np.isneginf(row["lnB_min"]) else float(row["lnB_min"]),
                "lnB_max": "inf" if np.isposinf(row["lnB_max"]) else float(row["lnB_max"]),
                "classification": str(row["classification"]),
                "notes": str(row["notes"]),
            }
        )

    payload = {
        "table_version": "2026-03-04",
        "classification_rule": "row interval where lnB_min <= lnB < lnB_max",
        "rows": normalized_rows,
    }
    canonical_payload = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    payload["table_sha256"] = hashlib.sha256(canonical_payload.encode("utf-8")).hexdigest()
    return payload
