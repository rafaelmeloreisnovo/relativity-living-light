import os
import numpy as np
import pandas as pd

from .models import model_RLL_like_Hz, model_RLL_like_fs8


def default_redshift_bins():
    return [
        ("low_z", -np.inf, 0.7),
        ("mid_z", 0.7, 1.3),
        ("high_z", 1.3, np.inf),
    ]


def _collect_observable_vectors(hz_df, fs8_df, params):
    return {
        "Hz": {
            "z": hz_df["z"].to_numpy(dtype=float),
            "values": model_RLL_like_Hz(hz_df["z"].to_numpy(dtype=float), params),
        },
        "f_sigma8": {
            "z": fs8_df["z"].to_numpy(dtype=float),
            "values": model_RLL_like_fs8(fs8_df["z"].to_numpy(dtype=float), params),
        },
    }


def _build_jacobian(group_name, z_mask_hz, z_mask_fs8, hz_df, fs8_df, params, fit_params, rel_step=1e-4):
    rows = []
    base = _collect_observable_vectors(hz_df, fs8_df, params)

    if group_name in ("Hz", "combined"):
        rows.append(base["Hz"]["values"][z_mask_hz])
    if group_name in ("f_sigma8", "combined"):
        rows.append(base["f_sigma8"]["values"][z_mask_fs8])

    if not rows:
        return np.zeros((0, len(fit_params)), dtype=float)

    base_vector = np.concatenate(rows)
    n_obs = base_vector.size
    jacobian = np.zeros((n_obs, len(fit_params)), dtype=float)

    for col, p in enumerate(fit_params):
        step = rel_step * max(abs(float(params[p])), 1.0)
        p_up = dict(params)
        p_dn = dict(params)
        p_up[p] = float(params[p]) + step
        p_dn[p] = float(params[p]) - step

        up = _collect_observable_vectors(hz_df, fs8_df, p_up)
        dn = _collect_observable_vectors(hz_df, fs8_df, p_dn)

        up_rows = []
        dn_rows = []
        if group_name in ("Hz", "combined"):
            up_rows.append(up["Hz"]["values"][z_mask_hz])
            dn_rows.append(dn["Hz"]["values"][z_mask_hz])
        if group_name in ("f_sigma8", "combined"):
            up_rows.append(up["f_sigma8"]["values"][z_mask_fs8])
            dn_rows.append(dn["f_sigma8"]["values"][z_mask_fs8])

        up_vec = np.concatenate(up_rows)
        dn_vec = np.concatenate(dn_rows)
        jacobian[:, col] = (up_vec - dn_vec) / (2.0 * step)

    return jacobian


def _safe_corrcoef_columns(jacobian):
    n_params = jacobian.shape[1]
    if jacobian.shape[0] < 2:
        return np.eye(n_params, dtype=float)

    centered = jacobian - jacobian.mean(axis=0, keepdims=True)
    std = jacobian.std(axis=0, ddof=1)
    corr = np.zeros((n_params, n_params), dtype=float)

    for i in range(n_params):
        corr[i, i] = 1.0
        for j in range(i + 1, n_params):
            if std[i] == 0.0 or std[j] == 0.0:
                cij = 0.0
            else:
                cov_ij = float(np.dot(centered[:, i], centered[:, j]) / (jacobian.shape[0] - 1))
                cij = cov_ij / (std[i] * std[j])
            corr[i, j] = cij
            corr[j, i] = cij
    return corr


def analyze_rll_degeneracy(hz_df, fs8_df, params, results_dir, fit_params=None, z_bins=None, high_corr_threshold=0.9):
    if fit_params is None:
        fit_params = ["H0", "Om", "sigma8", "gamma", "alpha", "z_peak", "width"]
    if z_bins is None:
        z_bins = default_redshift_bins()

    os.makedirs(results_dir, exist_ok=True)
    summary_rows = []

    z_hz = hz_df["z"].to_numpy(dtype=float)
    z_fs8 = fs8_df["z"].to_numpy(dtype=float)

    for zbin_name, zmin, zmax in z_bins:
        mask_hz = (z_hz >= zmin) & (z_hz < zmax)
        mask_fs8 = (z_fs8 >= zmin) & (z_fs8 < zmax)

        for group_name in ("Hz", "f_sigma8", "combined"):
            J = _build_jacobian(group_name, mask_hz, mask_fs8, hz_df, fs8_df, params, fit_params)
            if J.shape[0] == 0:
                continue

            corr = _safe_corrcoef_columns(J)
            jtj = J.T @ J
            try:
                cond_jtj = float(np.linalg.cond(jtj))
            except np.linalg.LinAlgError:
                cond_jtj = float("inf")

            corr_df = pd.DataFrame(corr, index=fit_params, columns=fit_params)
            matrix_path = os.path.join(results_dir, f"rll_degeneracy_matrix_{group_name}_{zbin_name}.csv")
            corr_df.to_csv(matrix_path, index=True)

            for i, p_i in enumerate(fit_params):
                for j in range(i + 1, len(fit_params)):
                    p_j = fit_params[j]
                    c = float(corr[i, j])
                    summary_rows.append(
                        {
                            "zbin": zbin_name,
                            "group": group_name,
                            "param_i": p_i,
                            "param_j": p_j,
                            "corr": c,
                            "abs_corr": abs(c),
                            "high_corr_pair": bool(abs(c) >= high_corr_threshold),
                            "cond_jtj": cond_jtj,
                            "n_obs": int(J.shape[0]),
                            "n_params": int(J.shape[1]),
                        }
                    )

    summary_df = pd.DataFrame(summary_rows)
    summary_path = os.path.join(results_dir, "rll_degeneracy_by_zbin.csv")
    summary_df.to_csv(summary_path, index=False)
    return summary_df, summary_path


def top_degenerate_pairs_by_bin(summary_df, top_n=3):
    out = {}
    if summary_df.empty:
        return out

    for zbin, gdf in summary_df.groupby("zbin"):
        top = gdf.sort_values(["abs_corr", "group"], ascending=[False, True]).head(top_n)
        out[zbin] = [
            {
                "group": row["group"],
                "pair": f"{row['param_i']}~{row['param_j']}",
                "corr": float(row["corr"]),
            }
            for _, row in top.iterrows()
        ]
    return out
