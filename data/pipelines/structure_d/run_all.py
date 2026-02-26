import os
import numpy as np
import pandas as pd

from .data_access import load_active_datasets
from .likelihood import chi2, chi2_with_covariance, aic, bic, evaluate_model
from .models import (
    model_LCDM_BAO,
    model_LCDM_Hz,
    model_LCDM_SNe,
    model_LCDM_fs8,
    model_LCDM_lenses,
    model_RLL_like_BAO,
    model_RLL_like_Hz,
    model_RLL_like_SNe,
    model_RLL_like_fs8,
    model_RLL_like_lenses,
)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RESULTS = os.path.join(BASE_DIR, "results", "structure_d")
DEFAULT_CONFIG = os.path.join("data", "pipelines", "structure_d", "datasets_config.json")


def _chi2_from_entry(entry, model_values):
    if entry["errors"] is not None:
        return chi2(entry["values"], model_values, entry["errors"])
    return chi2_with_covariance(entry["values"], model_values, entry["covariance"])


def _normalize_for_block(entry, mod, block_name):
    obs = np.asarray(entry["values"], dtype=float)
    mod_arr = np.asarray(mod, dtype=float)
    if obs.shape != mod_arr.shape:
        raise ValueError(f"{block_name}: model shape {mod_arr.shape} must match obs shape {obs.shape}")

    observable = str(entry.get("observable", "")).lower()
    if observable in {"hz", "h(z)"}:
        return obs, mod_arr
    if observable in {"fs8", "fσ8", "f_sigma8"}:
        return obs, mod_arr
    if observable in {"mu", "distance_modulus", "sne"}:
        return obs, mod_arr
    if observable in {"dv_over_rs", "bao", "dm_over_rs", "dh_over_rs"}:
        return obs, mod_arr
    if observable in {"lenses", "lens", "distance_ratio", "dls_over_ds"}:
        return obs, mod_arr
    return obs, mod_arr


def _dataset_block_name(entry):
    observable = str(entry.get("observable", "")).lower()
    if observable in {"mu", "distance_modulus", "sne"}:
        return "SNe"
    if observable in {"dv_over_rs", "bao", "dm_over_rs", "dh_over_rs"}:
        return "BAO"
    if observable in {"lenses", "lens", "distance_ratio", "dls_over_ds"}:
        return "lenses"
    if observable in {"fs8", "fσ8", "f_sigma8"}:
        return "fσ8"
    if observable in {"hz", "h(z)"}:
        return "Hz"
    return entry.get("observable", entry.get("dataset_id", "unknown"))


def covariance_usage_summary(active_blocks, diagonal_fallback=True):
    rows = []
    for block in active_blocks:
        has_full_covariance = block.get("covariance") is not None
        has_diagonal_sigma = block.get("errors") is not None
        if has_full_covariance:
            mode = "full_covariance"
        elif has_diagonal_sigma and diagonal_fallback:
            mode = "diagonal_sigma"
        else:
            mode = "not_used"

        rows.append(
            {
                "block": block.get("block"),
                "observable": block.get("observable"),
                "N": block.get("N", len(block.get("obs", []))),
                "covariance_mode": mode,
                "has_full_covariance": bool(has_full_covariance),
                "has_diagonal_sigma": bool(has_diagonal_sigma),
            }
        )

    return pd.DataFrame(rows)


def chi2_blocks(blocks):
    total = 0.0
    for block in blocks:
        entry = {
            "values": block["obs"],
            "errors": block.get("errors"),
            "covariance": block.get("covariance"),
        }
        total += _chi2_from_entry(entry, block["mod"])
    return total


def main(config_path=DEFAULT_CONFIG):
    os.makedirs(RESULTS, exist_ok=True)
    rows = []

    cfg, datasets = load_active_datasets(config_path)

    lcdm = dict(H0=70.0, Om=0.3, Ol=0.7, sigma8=0.8, gamma=0.55)
    rll = dict(H0=70.0, Om=0.3, Ol=0.7, sigma8=0.8, gamma=0.55, alpha=0.06, z_peak=2.0, width=1.2, beta=0.00)

    fit_params_lcdm = ["H0", "Om", "sigma8", "gamma"]
    fit_params_rll = fit_params_lcdm + ["alpha", "z_peak", "width"]
    fixed_params_lcdm = sorted(set(lcdm) - set(fit_params_lcdm))
    fixed_params_rll = sorted(set(rll) - set(fit_params_rll))

    model_map_lcdm = {
        "hz": model_LCDM_Hz,
        "fsigma8": model_LCDM_fs8,
        "real_hz": model_LCDM_Hz,
        "real_bao": model_LCDM_BAO,
        "sne": model_LCDM_SNe,
        "lenses": model_LCDM_lenses,
    }
    model_map_rll = {
        "hz": model_RLL_like_Hz,
        "fsigma8": model_RLL_like_fs8,
        "real_hz": model_RLL_like_Hz,
        "real_bao": model_RLL_like_BAO,
        "sne": model_RLL_like_SNe,
        "lenses": model_RLL_like_lenses,
    }

    blocks_lcdm_active = []
    blocks_rll_active = []
    total_observables = 0

    for dataset_id in cfg["active_datasets"]:
        entry = datasets[dataset_id]
        z = entry.get("z")
        if z is None:
            continue

        model_fn_lcdm = model_map_lcdm.get(dataset_id)
        model_fn_rll = model_map_rll.get(dataset_id)
        if model_fn_lcdm is None or model_fn_rll is None:
            continue

        mod_lcdm = model_fn_lcdm(z, lcdm)
        mod_rll = model_fn_rll(z, rll)

        obs_lcdm, mod_lcdm = _normalize_for_block(entry, mod_lcdm, dataset_id)
        obs_rll, mod_rll = _normalize_for_block(entry, mod_rll, dataset_id)

        block_name = _dataset_block_name(entry)
        block_common = {
            "block": block_name,
            "observable": entry.get("observable", block_name),
            "N": len(entry["values"]),
            "errors": entry.get("errors"),
            "covariance": entry.get("covariance"),
        }

        blocks_lcdm_active.append({**block_common, "obs": obs_lcdm, "mod": mod_lcdm})
        blocks_rll_active.append({**block_common, "obs": obs_rll, "mod": mod_rll})
        total_observables += len(entry["values"])

    chi2_lcdm = chi2_blocks(blocks_lcdm_active)
    chi2_rll = chi2_blocks(blocks_rll_active)

    active_datasets = ",".join(cfg["active_datasets"])

    k_lcdm = len(fit_params_lcdm)
    k_rll = len(fit_params_rll)

    rows.append(dict(model="LCDM", chi2=chi2_lcdm, AIC=aic(chi2_lcdm, k_lcdm), BIC=bic(chi2_lcdm, k_lcdm, total_observables),
                     N=total_observables, k=k_lcdm, fit_params=",".join(fit_params_lcdm), fixed_params=",".join(fixed_params_lcdm),
                     datasets_used=active_datasets, run_name=cfg.get("run_name", "unknown")))
    rows.append(dict(model="RLL_like+AGN", chi2=chi2_rll, AIC=aic(chi2_rll, k_rll), BIC=bic(chi2_rll, k_rll, total_observables),
                     N=total_observables, k=k_rll, fit_params=",".join(fit_params_rll), fixed_params=",".join(fixed_params_rll),
                     datasets_used=active_datasets, run_name=cfg.get("run_name", "unknown")))

    out = os.path.join(RESULTS, "model_comparison.csv")
    df = evaluate_model(rows, out)

    cov_rows = []
    expected_blocks = ["SNe", "BAO", "fσ8", "lenses", "Hz"]
    for model_name, active_blocks in (("LCDM", blocks_lcdm_active), ("RLL_like+AGN", blocks_rll_active)):
        summary_df = covariance_usage_summary(active_blocks, diagonal_fallback=True)
        missing = [
            {"block": b, "observable": b, "N": 0, "covariance_mode": "not_used", "has_full_covariance": False, "has_diagonal_sigma": False}
            for b in expected_blocks if b not in set(summary_df["block"].tolist())
        ]
        if missing:
            summary_df = pd.concat([summary_df, pd.DataFrame(missing)], ignore_index=True)
        summary_df.insert(0, "model", model_name)
        cov_rows.append(summary_df)
    cov_out = os.path.join(RESULTS, "covariance_usage.csv")
    evaluate_model([r for d in cov_rows for r in d.to_dict(orient="records")], cov_out)

    print(df.to_string(index=False))
    print(f"\nWrote: {out}")
    print(f"Wrote: {cov_out}")


if __name__ == "__main__":
    main()
