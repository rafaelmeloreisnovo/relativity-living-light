import os
import numpy as np
import pandas as pd

from .likelihood import load_csv
from .models import model_RLL_like_Hz, model_RLL_like_fs8

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
DATA = os.path.join(BASE_DIR, "data", "inputs", "structure_d")
RESULTS = os.path.join(BASE_DIR, "results", "structure_d")

RLL_PARAMS = {
    "H0": 70.0,
    "Om": 0.3,
    "Ol": 0.7,
    "sigma8": 0.8,
    "gamma": 0.55,
    "alpha": 0.06,
    "z_peak": 2.0,
    "width": 1.2,
    "beta": 0.0,
}


def adaptive_step(value, rel_step=1e-2, min_step=1e-4):
    base = abs(float(value))
    step = rel_step * base
    if step < min_step:
        step = min_step
    return step


def central_finite_difference(model_fn, z, params, param_name, step):
    p_plus = dict(params)
    p_minus = dict(params)
    p_plus[param_name] = float(params[param_name]) + step
    p_minus[param_name] = float(params[param_name]) - step

    out_plus = np.asarray(model_fn(z, p_plus), dtype=float)
    out_minus = np.asarray(model_fn(z, p_minus), dtype=float)
    return (out_plus - out_minus) / (2.0 * step)


def derivative_metrics(nominal_output, derivative, param_value, sigma=None):
    nominal_output = np.asarray(nominal_output, dtype=float)
    derivative = np.asarray(derivative, dtype=float)

    elasticity = np.full_like(derivative, np.nan, dtype=float)
    if param_value != 0.0:
        valid = nominal_output != 0.0
        elasticity[valid] = (param_value / nominal_output[valid]) * derivative[valid]

    normalized_score = np.full_like(derivative, np.nan, dtype=float)
    if sigma is not None:
        sigma_arr = np.asarray(sigma, dtype=float)
        valid_sigma = sigma_arr > 0.0
        normalized_score[valid_sigma] = np.abs(derivative[valid_sigma]) / sigma_arr[valid_sigma]

    return np.abs(derivative), elasticity, normalized_score


def stability_check(derivative_step, derivative_half_step, rtol=5e-2, atol=1e-10):
    derivative_step = np.asarray(derivative_step, dtype=float)
    derivative_half_step = np.asarray(derivative_half_step, dtype=float)

    delta = np.abs(derivative_half_step - derivative_step)
    scale = np.maximum(np.abs(derivative_half_step), atol)
    rel_diff = delta / scale
    stable = rel_diff <= rtol
    return stable, rel_diff


def sensitivity_table_by_redshift(params=None):
    params = dict(RLL_PARAMS if params is None else params)

    hz = load_csv(os.path.join(DATA, "Hz.csv"), ["z", "Hz", "sigma"])
    fs8 = load_csv(os.path.join(DATA, "fsigma8.csv"), ["z", "fs8", "sigma"])

    z_hz = hz["z"].to_numpy(dtype=float)
    z_fs = fs8["z"].to_numpy(dtype=float)

    nominal_hz = np.asarray(model_RLL_like_Hz(z_hz, params), dtype=float)
    nominal_fs = np.asarray(model_RLL_like_fs8(z_fs, params), dtype=float)

    rows = []
    for p_name in params:
        p_value = float(params[p_name])
        dp = adaptive_step(p_value)
        dp_half = dp / 2.0

        deriv_hz = central_finite_difference(model_RLL_like_Hz, z_hz, params, p_name, dp)
        deriv_hz_half = central_finite_difference(model_RLL_like_Hz, z_hz, params, p_name, dp_half)
        stable_hz, rel_diff_hz = stability_check(deriv_hz, deriv_hz_half)
        abs_hz, elas_hz, norm_hz = derivative_metrics(nominal_hz, deriv_hz, p_value, sigma=hz["sigma"].to_numpy(dtype=float))

        for idx, z_val in enumerate(z_hz):
            rows.append(
                {
                    "observable": "Hz",
                    "z": float(z_val),
                    "parameter": p_name,
                    "param_nominal": p_value,
                    "dp": dp,
                    "dO_dp": float(deriv_hz[idx]),
                    "abs_dO_dp": float(abs_hz[idx]),
                    "dlnO_dlnp": float(elas_hz[idx]) if np.isfinite(elas_hz[idx]) else np.nan,
                    "sigma_obs": float(hz["sigma"].iloc[idx]),
                    "normalized_score": float(norm_hz[idx]) if np.isfinite(norm_hz[idx]) else np.nan,
                    "stable": bool(stable_hz[idx]),
                    "stability_rel_diff": float(rel_diff_hz[idx]),
                    "step_reference": dp,
                    "step_validation": dp_half,
                }
            )

        deriv_fs = central_finite_difference(model_RLL_like_fs8, z_fs, params, p_name, dp)
        deriv_fs_half = central_finite_difference(model_RLL_like_fs8, z_fs, params, p_name, dp_half)
        stable_fs, rel_diff_fs = stability_check(deriv_fs, deriv_fs_half)
        abs_fs, elas_fs, norm_fs = derivative_metrics(nominal_fs, deriv_fs, p_value, sigma=fs8["sigma"].to_numpy(dtype=float))

        for idx, z_val in enumerate(z_fs):
            rows.append(
                {
                    "observable": "fσ8",
                    "z": float(z_val),
                    "parameter": p_name,
                    "param_nominal": p_value,
                    "dp": dp,
                    "dO_dp": float(deriv_fs[idx]),
                    "abs_dO_dp": float(abs_fs[idx]),
                    "dlnO_dlnp": float(elas_fs[idx]) if np.isfinite(elas_fs[idx]) else np.nan,
                    "sigma_obs": float(fs8["sigma"].iloc[idx]),
                    "normalized_score": float(norm_fs[idx]) if np.isfinite(norm_fs[idx]) else np.nan,
                    "stable": bool(stable_fs[idx]),
                    "stability_rel_diff": float(rel_diff_fs[idx]),
                    "step_reference": dp,
                    "step_validation": dp_half,
                }
            )

    return pd.DataFrame(rows)


def main():
    os.makedirs(RESULTS, exist_ok=True)
    out = os.path.join(RESULTS, "rll_sensitivity_derivatives.csv")
    df = sensitivity_table_by_redshift()
    df.to_csv(out, index=False)
    print(f"Wrote: {out}")


if __name__ == "__main__":
    main()
