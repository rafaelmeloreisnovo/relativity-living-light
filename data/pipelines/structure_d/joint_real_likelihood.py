"""Joint real-data likelihood for the RLL cosmology validation stack.

This module intentionally keeps the current repository data local-first: it uses
materialized H(z), DESI DR2 BAO primary points, the fσ8 table, and the Planck
CMB-shift summary already committed under ``data/``.  It does not download or
invent missing data; when only a published covariance summary is present, the
BAO covariance is built from the committed diagonal errors plus the committed
same-tracer DM/DH correlations.
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
import time
from pathlib import Path
from typing import Callable

import numpy as np
import pandas as pd

try:
    from scipy.integrate import quad
    from scipy.optimize import differential_evolution
except ImportError as exc:  # pragma: no cover - exercised by environment setup
    raise ImportError(
        "joint_real_likelihood requires SciPy. Install with `pip install -r requirements.txt`."
    ) from exc

from .likelihood import aic, bic, chi2_with_covariance

TEXTUAL_OUTPUTS = [
    "results/structure_d/joint_real_likelihood.csv",
    "results/structure_d/joint_real_likelihood.json",
    "results/structure_d/joint_real_likelihood_covariance_manifest.json",
]

BASE_DIR = Path(__file__).resolve().parents[3]
RESULTS = BASE_DIR / "results" / "structure_d"

HZ_PATH = BASE_DIR / "data" / "real" / "Hz_data_real.csv"
DESI_POINTS_PATH = BASE_DIR / "data" / "real" / "cosmology" / "desi_dr2_bao_primary_points.csv"
DESI_COV_SUMMARY_PATH = BASE_DIR / "data" / "real" / "cosmology" / "desi_dr2_bao_covariance_summary.csv"
FSIGMA8_PATH = BASE_DIR / "data" / "inputs" / "structure_d" / "fsigma8.csv"
CMB_SHIFT_PATH = BASE_DIR / "data" / "real" / "CMB_shift_real.json"

C_KMS = 299792.458
ORAD = 9.0e-5
Z_CMB_DEFAULT = 1089.92
MODEL_LCDM = "LCDM_joint_real"
MODEL_RLL = "RLL_joint_real"


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fp:
        for chunk in iter(lambda: fp.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _atomic_write_text(path: Path, text: str) -> dict[str, str | bool]:
    """Write with rollback marker: previous file is preserved as ``.bak`` first."""

    path.parent.mkdir(parents=True, exist_ok=True)
    backup = path.with_suffix(path.suffix + ".bak")
    tmp = path.with_suffix(path.suffix + f".tmp-{os.getpid()}")
    rollback_available = False
    if path.exists():
        backup.write_bytes(path.read_bytes())
        rollback_available = True
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)
    return {
        "path": str(path.relative_to(BASE_DIR)),
        "backup_path": str(backup.relative_to(BASE_DIR)) if rollback_available else "",
        "rollback_available": rollback_available,
    }


def transition_f(z: np.ndarray | float, zt: float, wt: float) -> np.ndarray:
    z_arr = np.asarray(z, dtype=float)
    width = max(float(wt), 1.0e-6)
    return 1.0 / (1.0 + np.exp(np.clip((z_arr - float(zt)) / width, -500.0, 500.0)))


def e2_lcdm(z: np.ndarray | float, h0: float, om: float, ol: float) -> np.ndarray:
    del h0  # kept in the signature to match the RLL callable interface
    z_arr = np.asarray(z, dtype=float)
    return om * (1.0 + z_arr) ** 3 + ORAD * (1.0 + z_arr) ** 4 + ol


def e2_rll(z: np.ndarray | float, h0: float, om: float, ol: float, os0: float, zt: float, wt: float) -> np.ndarray:
    del h0
    z_arr = np.asarray(z, dtype=float)
    fz = transition_f(z_arr, zt, wt)
    superposition = os0 * (fz + (1.0 - fz) * (1.0 + z_arr) ** 3)
    return om * (1.0 + z_arr) ** 3 + ORAD * (1.0 + z_arr) ** 4 + ol + superposition


def hz_from_e2(z: np.ndarray | float, e2_fn: Callable, params: tuple[float, ...]) -> np.ndarray:
    h0 = float(params[0])
    return h0 * np.sqrt(np.maximum(e2_fn(z, *params), 1.0e-12))


def rd_drag_mpc(h0: float, om: float, ob_h2: float) -> float:
    """Aubourg/Eisenstein-Hu style calibrated power-law r_d approximation.

    The repository previously fixed r_d.  This function derives it from the
    fitted physical matter and baryon densities, keeping a lightweight formula
    suitable for fast validation and explicit AIC/BIC comparisons.
    """

    om_h2 = float(om) * (float(h0) / 100.0) ** 2
    return float(147.78 * (om_h2 / 0.1432) ** (-0.255) * (float(ob_h2) / 0.02236) ** (-0.134))


def comoving_distance_mpc(z: float, e2_fn: Callable, params: tuple[float, ...], cache: dict | None = None) -> float:
    z_val = float(z)
    key = (e2_fn.__name__, z_val, tuple(float(x) for x in params))
    if cache is not None and key in cache:
        return float(cache[key])

    integrand = lambda zz: C_KMS / float(hz_from_e2(zz, e2_fn, params))
    value, _ = quad(integrand, 0.0, z_val, epsrel=1.0e-5, limit=200)
    if cache is not None:
        cache[key] = float(value)
    return float(value)


def bao_prediction(row: pd.Series, e2_fn: Callable, params: tuple[float, ...], ob_h2: float, cache: dict | None = None) -> float:
    z = float(row["z_eff"])
    dc = comoving_distance_mpc(z, e2_fn, params, cache=cache)
    hz = float(hz_from_e2(z, e2_fn, params))
    rd = rd_drag_mpc(params[0], params[1], ob_h2)
    observable = str(row["observable"])
    if observable == "DV_over_rd":
        dv = (z * C_KMS * dc * dc / hz) ** (1.0 / 3.0)
        return float(dv / rd)
    if observable == "DM_over_rd":
        return float(dc / rd)
    if observable == "DH_over_rd":
        return float((C_KMS / hz) / rd)
    raise ValueError(f"unsupported DESI BAO observable: {observable}")


def build_desi_covariance(points: pd.DataFrame, summary: pd.DataFrame) -> np.ndarray:
    cov = np.diag(points["sigma"].astype(float).to_numpy() ** 2)
    for _, block in summary.iterrows():
        block_name = str(block["covariance_block"])
        idx = points.index[points["covariance_block"] == block_name].tolist()
        if len(idx) != 2:
            raise ValueError(f"DESI covariance block {block_name} must map to exactly two rows")
        i, j = idx
        covariance = float(block["covariance"])
        cov[i, j] = covariance
        cov[j, i] = covariance
    return cov


def omega_m_z_from_e2(z: np.ndarray, e2_fn: Callable, params: tuple[float, ...]) -> np.ndarray:
    z_arr = np.asarray(z, dtype=float)
    om = float(params[1])
    return om * (1.0 + z_arr) ** 3 / np.maximum(e2_fn(z_arr, *params), 1.0e-12)


def fsigma8_prediction(z: np.ndarray, e2_fn: Callable, params: tuple[float, ...], sigma8: float) -> np.ndarray:
    return float(sigma8) * omega_m_z_from_e2(np.asarray(z, dtype=float), e2_fn, params) ** 0.55


def cmb_shift_prediction(e2_fn: Callable, params: tuple[float, ...], ob_h2: float, z_cmb: float, cache: dict | None = None) -> np.ndarray:
    dc = comoving_distance_mpc(z_cmb, e2_fn, params, cache=cache)
    r_shift = np.sqrt(float(params[1])) * float(params[0]) * dc / C_KMS
    acoustic_scale = np.pi * dc / rd_drag_mpc(params[0], params[1], ob_h2)
    return np.array([r_shift, acoustic_scale], dtype=float)


def _chi2_diag(obs: np.ndarray, pred: np.ndarray, sigma: np.ndarray) -> float:
    return float(np.sum(((np.asarray(obs, dtype=float) - np.asarray(pred, dtype=float)) / np.asarray(sigma, dtype=float)) ** 2))


def load_joint_inputs() -> dict:
    hz = pd.read_csv(HZ_PATH)
    desi = pd.read_csv(DESI_POINTS_PATH)
    desi_summary = pd.read_csv(DESI_COV_SUMMARY_PATH)
    fs8 = pd.read_csv(FSIGMA8_PATH)
    cmb = json.loads(CMB_SHIFT_PATH.read_text(encoding="utf-8"))
    desi_cov = build_desi_covariance(desi, desi_summary)
    return {"hz": hz, "desi": desi, "desi_summary": desi_summary, "desi_cov": desi_cov, "fs8": fs8, "cmb": cmb}


def evaluate_components(model: str, vector: np.ndarray, inputs: dict) -> dict[str, float]:
    vector = np.asarray(vector, dtype=float)
    if model == MODEL_LCDM:
        h0, om, ol, ob_h2, sigma8 = vector
        e2_fn = e2_lcdm
        params = (h0, om, ol)
    elif model == MODEL_RLL:
        h0, om, ol, os0, zt, wt, ob_h2, sigma8 = vector
        e2_fn = e2_rll
        params = (h0, om, ol, os0, zt, wt)
    else:
        raise ValueError(f"unknown model: {model}")

    if h0 <= 0.0 or om <= 0.0 or ol <= 0.0 or ob_h2 <= 0.0 or sigma8 <= 0.0:
        return {"total": float("inf")}
    if np.any(e2_fn(np.array([0.0, 2.5, Z_CMB_DEFAULT]), *params) <= 0.0):
        return {"total": float("inf")}

    cache: dict = {}
    hz_df = inputs["hz"]
    hz_pred = hz_from_e2(hz_df["z"].to_numpy(dtype=float), e2_fn, params)
    chi2_hz = _chi2_diag(hz_df["H_obs"].to_numpy(dtype=float), hz_pred, hz_df["sigma_H"].to_numpy(dtype=float))

    desi_df = inputs["desi"]
    bao_pred = np.array([bao_prediction(row, e2_fn, params, ob_h2, cache=cache) for _, row in desi_df.iterrows()])
    chi2_bao = chi2_with_covariance(desi_df["value"].to_numpy(dtype=float), bao_pred, inputs["desi_cov"])

    fs8_df = inputs["fs8"]
    fs8_pred = fsigma8_prediction(fs8_df["z"].to_numpy(dtype=float), e2_fn, params, sigma8)
    chi2_fs8 = _chi2_diag(fs8_df["fs8"].to_numpy(dtype=float), fs8_pred, fs8_df["sigma"].to_numpy(dtype=float))

    cmb = inputs["cmb"]
    cmb_obs = np.array([float(cmb["R_obs"]), float(cmb["la_obs"])], dtype=float)
    cmb_sig = np.array([float(cmb["R_sig"]), float(cmb["la_sig"])], dtype=float)
    cmb_pred = cmb_shift_prediction(e2_fn, params, ob_h2, float(cmb.get("z_CMB", Z_CMB_DEFAULT)), cache=cache)
    chi2_cmb = _chi2_diag(cmb_obs, cmb_pred, cmb_sig)

    total = chi2_hz + chi2_bao + chi2_fs8 + chi2_cmb
    return {
        "Hz": float(chi2_hz),
        "DESI_DR2_BAO": float(chi2_bao),
        "fsigma8": float(chi2_fs8),
        "CMB_shift": float(chi2_cmb),
        "total": float(total),
    }


def fit_model(model: str, inputs: dict, seed: int, maxiter: int, tol: float) -> tuple[np.ndarray, dict[str, float]]:
    if model == MODEL_LCDM:
        bounds = [(60.0, 80.0), (0.10, 0.60), (0.40, 1.10), (0.018, 0.026), (0.50, 1.10)]
    elif model == MODEL_RLL:
        bounds = [(60.0, 80.0), (0.10, 0.60), (0.40, 1.10), (0.0, 0.25), (0.1, 10.0), (0.05, 2.0), (0.018, 0.026), (0.50, 1.10)]
    else:
        raise ValueError(f"unknown model: {model}")

    result = differential_evolution(
        lambda values: evaluate_components(model, values, inputs)["total"],
        bounds,
        seed=seed,
        maxiter=maxiter,
        tol=tol,
        workers=1,
        polish=True,
    )
    return np.asarray(result.x, dtype=float), evaluate_components(model, result.x, inputs)


def _json_safe(value):
    if isinstance(value, dict):
        return {key: _json_safe(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_json_safe(item) for item in value]
    if isinstance(value, tuple):
        return [_json_safe(item) for item in value]
    if isinstance(value, np.generic):
        value = value.item()
    if isinstance(value, float) and not np.isfinite(value):
        return None
    return value


def _rows_to_csv(rows: list[dict]) -> str:
    fieldnames = list(rows[0].keys())
    from io import StringIO

    buf = StringIO()
    writer = csv.DictWriter(buf, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buf.getvalue()


def run_joint_likelihood(output_stem: str = "joint_real_likelihood") -> dict:
    start = time.perf_counter()
    inputs = load_joint_inputs()
    seed = int(os.environ.get("STRUCTURE_D_JOINT_SEED", "42"))
    tol = float(os.environ.get("STRUCTURE_D_JOINT_TOL", "1e-6"))
    maxiter_lcdm = int(os.environ.get("STRUCTURE_D_JOINT_MAXITER_LCDM", "120"))
    maxiter_rll = int(os.environ.get("STRUCTURE_D_JOINT_MAXITER_RLL", "180"))

    lcdm_vector, lcdm_components = fit_model(MODEL_LCDM, inputs, seed, maxiter_lcdm, tol)
    rll_vector, rll_components = fit_model(MODEL_RLL, inputs, seed, maxiter_rll, tol)

    n_obs = int(len(inputs["hz"]) + len(inputs["desi"]) + len(inputs["fs8"]) + 2)
    k_lcdm = 5
    k_rll = 8
    rows = [
        {
            "model": MODEL_LCDM,
            "chi2": lcdm_components["total"],
            "AIC": aic(lcdm_components["total"], k_lcdm),
            "BIC": bic(lcdm_components["total"], k_lcdm, n_obs),
            "N": n_obs,
            "k": k_lcdm,
            "dof": n_obs - k_lcdm,
            "chi2_Hz": lcdm_components["Hz"],
            "chi2_DESI_DR2_BAO": lcdm_components["DESI_DR2_BAO"],
            "chi2_fsigma8": lcdm_components["fsigma8"],
            "chi2_CMB_shift": lcdm_components["CMB_shift"],
            "H0": lcdm_vector[0],
            "Om": lcdm_vector[1],
            "OL": lcdm_vector[2],
            "Os0": np.nan,
            "zt": np.nan,
            "wt": np.nan,
            "Ob_h2": lcdm_vector[3],
            "sigma8": lcdm_vector[4],
        },
        {
            "model": MODEL_RLL,
            "chi2": rll_components["total"],
            "AIC": aic(rll_components["total"], k_rll),
            "BIC": bic(rll_components["total"], k_rll, n_obs),
            "N": n_obs,
            "k": k_rll,
            "dof": n_obs - k_rll,
            "chi2_Hz": rll_components["Hz"],
            "chi2_DESI_DR2_BAO": rll_components["DESI_DR2_BAO"],
            "chi2_fsigma8": rll_components["fsigma8"],
            "chi2_CMB_shift": rll_components["CMB_shift"],
            "H0": rll_vector[0],
            "Om": rll_vector[1],
            "OL": rll_vector[2],
            "Os0": rll_vector[3],
            "zt": rll_vector[4],
            "wt": rll_vector[5],
            "Ob_h2": rll_vector[6],
            "sigma8": rll_vector[7],
        },
    ]

    outputs = []
    outputs.append(_atomic_write_text(RESULTS / f"{output_stem}.csv", _rows_to_csv(rows)))

    payload = {
        "schema": "rll.joint_real_likelihood.v1",
        "created_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "runtime_seconds": time.perf_counter() - start,
        "optimizer": {
            "name": "scipy.optimize.differential_evolution",
            "seed": seed,
            "tol": tol,
            "maxiter_lcdm": maxiter_lcdm,
            "maxiter_rll": maxiter_rll,
        },
        "datasets": {
            "Hz": str(HZ_PATH.relative_to(BASE_DIR)),
            "DESI_DR2_BAO_primary": str(DESI_POINTS_PATH.relative_to(BASE_DIR)),
            "DESI_DR2_BAO_covariance_summary": str(DESI_COV_SUMMARY_PATH.relative_to(BASE_DIR)),
            "fsigma8": str(FSIGMA8_PATH.relative_to(BASE_DIR)),
            "CMB_shift": str(CMB_SHIFT_PATH.relative_to(BASE_DIR)),
        },
        "rd_policy": "derived_power_law_from_H0_Om_Ob_h2",
        "bao_covariance_policy": "block_covariance_from_committed_DESI_DR2_DM_DH_correlations; diagonal for unpaired BGS DV",
        "claim_boundary": "AIC/BIC comparison only; no superiority claim is implied by this artifact.",
        "rows": _json_safe(rows),
    }
    outputs.append(_atomic_write_text(RESULTS / f"{output_stem}.json", json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n"))

    manifest = {
        "schema": "rll.joint_real_likelihood.covariance_manifest.v1",
        "desi_covariance_shape": list(inputs["desi_cov"].shape),
        "desi_covariance_sha256": hashlib.sha256(inputs["desi_cov"].astype("<f8").tobytes()).hexdigest(),
        "input_sha256": {
            str(path.relative_to(BASE_DIR)): _sha256_file(path)
            for path in [HZ_PATH, DESI_POINTS_PATH, DESI_COV_SUMMARY_PATH, FSIGMA8_PATH, CMB_SHIFT_PATH]
        },
        "failsafe": {
            "atomic_write": True,
            "backup_before_replace": True,
            "rollback_instruction": "copy any non-empty *.bak file over the corresponding output if a downstream check fails",
        },
    }
    outputs.append(
        _atomic_write_text(
            RESULTS / f"{output_stem}_covariance_manifest.json",
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        )
    )
    payload["outputs"] = outputs
    return payload


def main() -> dict:
    payload = run_joint_likelihood()
    print(pd.DataFrame(payload["rows"]).to_string(index=False))
    for output in payload["outputs"]:
        print(f"Wrote: {output['path']}")
    return payload


if __name__ == "__main__":
    main()
