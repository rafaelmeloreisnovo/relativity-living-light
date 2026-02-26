import numpy as np
import pandas as pd


def _as_1d_finite_array(name, values):
    arr = np.asarray(values, dtype=float)
    if arr.ndim != 1:
        raise ValueError(f"{name} must be a 1D array")
    if arr.size == 0:
        raise ValueError(f"{name} cannot be empty")
    if np.any(~np.isfinite(arr)):
        raise ValueError(f"{name} must contain only finite values")
    return arr


def _validated_sigma_array(sigma):
    sigma_arr = _as_1d_finite_array("sigma", sigma)
    if np.any(sigma_arr <= 0):
        raise ValueError("sigma must contain only finite, strictly positive values")
    return sigma_arr


def _validated_residual_vector(r):
    return _as_1d_finite_array("r", r)


def _validate_covariance_matrix(C, n):
    C_arr = np.asarray(C, dtype=float)
    if C_arr.ndim != 2:
        raise ValueError("C must be a 2D matrix")
    if C_arr.shape != (n, n):
        raise ValueError(f"C must have shape ({n}, {n}), got {C_arr.shape}")
    if np.any(~np.isfinite(C_arr)):
        raise ValueError("C must contain only finite values")
    if not np.allclose(C_arr, C_arr.T, rtol=1e-10, atol=1e-12):
        raise ValueError("C must be symmetric within numerical tolerance")
    return C_arr


def _solve_covariance_system(C, r, regularization_eps=1e-12, max_regularization_trials=6):
    reg = 0.0
    identity = np.eye(C.shape[0], dtype=float)
    last_exc = None
    for _ in range(max_regularization_trials + 1):
        try:
            C_eff = C + reg * identity
            y = np.linalg.solve(C_eff, r)
            return y, reg
        except np.linalg.LinAlgError as exc:
            last_exc = exc
            reg = regularization_eps if reg == 0.0 else reg * 10.0
    raise ValueError(
        "C is singular or numerically unstable even after regularization "
        f"up to {reg:.1e}"
    ) from last_exc


def chi2(obs=None, mod=None, sigma=None, r=None, C=None, diagonal_fallback=True):
    if r is None:
        if obs is None or mod is None:
            raise ValueError("Provide either residual vector r, or both obs and mod")
        obs_arr = _as_1d_finite_array("obs", obs)
        mod_arr = _as_1d_finite_array("mod", mod)
        if obs_arr.shape != mod_arr.shape:
            raise ValueError("obs and mod must have the same shape")
        r_arr = obs_arr - mod_arr
    else:
        r_arr = _validated_residual_vector(r)

    n = r_arr.size

    if C is not None:
        C_arr = _validate_covariance_matrix(C, n)
        y, _ = _solve_covariance_system(C_arr, r_arr)
        chi2_val = float(np.dot(r_arr, y))
    elif sigma is not None and diagonal_fallback:
        sigma_arr = _validated_sigma_array(sigma)
        if sigma_arr.size != n:
            raise ValueError("sigma and residual vector must have the same length")
        scaled = r_arr / sigma_arr
        chi2_val = float(np.dot(scaled, scaled))
    else:
        raise ValueError("Missing covariance information: provide C or sigma (with diagonal_fallback=True)")

    if not np.isfinite(chi2_val):
        raise ValueError("Computed chi2 is not finite")
    if chi2_val < -1e-10:
        raise ValueError(f"Computed chi2 is negative beyond tolerance: {chi2_val}")
    return max(chi2_val, 0.0)


def chi2_blocks(blocks, diagonal_fallback=True):
    total = 0.0
    details = []

    for block in blocks:
        name = block.get("name", "unnamed")
        block_chi2 = chi2(
            obs=block.get("obs"),
            mod=block.get("mod"),
            sigma=block.get("sigma"),
            r=block.get("r"),
            C=block.get("C"),
            diagonal_fallback=diagonal_fallback,
        )
        cov_mode = "full" if block.get("C") is not None else "diagonal"
        size = len(_validated_residual_vector(block["r"])) if block.get("r") is not None else len(_as_1d_finite_array("obs", block["obs"]))
        details.append({"block": name, "chi2": block_chi2, "covariance": cov_mode, "N": size})
        total += block_chi2

    return float(total), details


def covariance_usage_summary(blocks, diagonal_fallback=True):
    summary = []
    for block in blocks:
        has_full = block.get("C") is not None
        has_diag = block.get("sigma") is not None
        if has_full:
            mode = "full"
        elif diagonal_fallback and has_diag:
            mode = "diagonal_fallback"
        else:
            mode = "missing"
        summary.append(
            {
                "block": block.get("name", "unnamed"),
                "covariance_mode": mode,
                "has_full_covariance": bool(has_full),
                "has_diagonal_sigma": bool(has_diag),
            }
        )
    return pd.DataFrame(summary)


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
