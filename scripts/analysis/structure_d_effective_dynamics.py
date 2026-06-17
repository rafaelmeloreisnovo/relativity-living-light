#!/usr/bin/env python3
"""Compute effective dynamics diagnostics for Structure-D joint-likelihood outputs.

This script is intentionally post-fit: it reads an existing joint-likelihood JSON
artifact and derives diagnostic functions on a redshift grid. It does not run a
new fit, does not alter raw data, and does not change claim policy.

Outputs are intended for RLL vs LCDM/wCDM/CPL functional comparison:
- E(z), H(z)
- effective dark-energy density proxy
- w_eff(z)
- q(z)
- comoving distance D_C(z)
- RLL transition fraction/logit when available
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
import time
from pathlib import Path
from typing import Any, Callable

import numpy as np

BASE_DIR = Path(__file__).resolve().parents[2]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from data.pipelines.structure_d import joint_real_likelihood as joint

C_KMS = 299792.458
DEFAULT_INPUT = BASE_DIR / "results" / "structure_d" / "joint_real_likelihood.json"
DEFAULT_OUTPUT_DIR = BASE_DIR / "results" / "structure_d" / "effective_dynamics"


MODEL_TO_E2: dict[str, Callable[..., np.ndarray]] = {
    joint.MODEL_LCDM: joint.e2_lcdm,
    joint.MODEL_WCDM: joint.e2_wcdm,
    joint.MODEL_CPL: joint.e2_cpl,
    joint.MODEL_RLL: joint.e2_rll,
}


def _finite_gradient(values: np.ndarray, z: np.ndarray) -> np.ndarray:
    if len(z) < 3:
        raise ValueError("z grid must contain at least three points")
    return np.gradient(values, z, edge_order=2)


def _cumtrapz(y: np.ndarray, x: np.ndarray) -> np.ndarray:
    out = np.zeros_like(x, dtype=float)
    if len(x) > 1:
        out[1:] = np.cumsum(0.5 * (y[1:] + y[:-1]) * np.diff(x))
    return out


def _safe_logit(probability: np.ndarray) -> np.ndarray:
    p = np.asarray(probability, dtype=float)
    clipped = np.clip(p, 1.0e-12, 1.0 - 1.0e-12)
    return np.log((1.0 - clipped) / clipped)


def _row_params(row: dict[str, Any]) -> tuple[Callable[..., np.ndarray], tuple[float, ...], float, float, float]:
    model = str(row["model"])
    h0 = float(row["H0"])
    om = float(row["Om"])
    ol = float(row["OL"])
    ob_h2 = float(row["Ob_h2"])

    if model == joint.MODEL_LCDM:
        return joint.e2_lcdm, (h0, om, ol), h0, om, ob_h2
    if model == joint.MODEL_WCDM:
        return joint.e2_wcdm, (h0, om, ol, float(row["w"])), h0, om, ob_h2
    if model == joint.MODEL_CPL:
        return joint.e2_cpl, (h0, om, ol, float(row["w0"]), float(row["wa"])), h0, om, ob_h2
    if model == joint.MODEL_RLL:
        return (
            joint.e2_rll,
            (h0, om, ol, float(row["Os0"]), float(row["zt"]), float(row["wt"])),
            h0,
            om,
            ob_h2,
        )
    raise ValueError(f"unsupported model row: {model}")


def effective_dark_density(e2: np.ndarray, z: np.ndarray, om: float) -> np.ndarray:
    """Return a background effective dark-sector density proxy.

    This is a diagnostic quantity, not a claim of a fully specified physical
    stress-energy tensor. It subtracts matter and radiation-like terms from E^2.
    Negative or zero values are preserved and handled downstream as undefined
    for logarithmic derivatives.
    """

    zp1 = 1.0 + np.asarray(z, dtype=float)
    return np.asarray(e2, dtype=float) - float(om) * zp1**3 - joint.ORAD * zp1**4


def w_eff_from_density(rho_eff: np.ndarray, z: np.ndarray) -> np.ndarray:
    rho = np.asarray(rho_eff, dtype=float)
    z_arr = np.asarray(z, dtype=float)
    out = np.full_like(z_arr, np.nan, dtype=float)
    valid = rho > 0.0
    if np.count_nonzero(valid) < 3:
        return out
    log_rho = np.full_like(z_arr, np.nan, dtype=float)
    log_rho[valid] = np.log(rho[valid])
    # Interpolate over invalid points only for derivative stability; restore NaN after.
    if not np.all(valid):
        log_rho = np.interp(z_arr, z_arr[valid], log_rho[valid])
    dlogrho_dz = _finite_gradient(log_rho, z_arr)
    out[valid] = -1.0 + (1.0 + z_arr[valid]) * dlogrho_dz[valid] / 3.0
    return out


def q_from_e2(e2: np.ndarray, z: np.ndarray) -> np.ndarray:
    e2_arr = np.asarray(e2, dtype=float)
    z_arr = np.asarray(z, dtype=float)
    de2_dz = _finite_gradient(e2_arr, z_arr)
    return -1.0 + (1.0 + z_arr) * de2_dz / np.maximum(2.0 * e2_arr, 1.0e-30)


def comoving_distance_mpc(e2: np.ndarray, z: np.ndarray, h0: float) -> np.ndarray:
    inv_e = 1.0 / np.sqrt(np.maximum(np.asarray(e2, dtype=float), 1.0e-30))
    return (C_KMS / float(h0)) * _cumtrapz(inv_e, np.asarray(z, dtype=float))


def diagnostics_for_row(row: dict[str, Any], z: np.ndarray) -> list[dict[str, Any]]:
    e2_fn, params, h0, om, _ob_h2 = _row_params(row)
    model = str(row["model"])
    e2 = np.asarray(e2_fn(z, *params), dtype=float)
    e = np.sqrt(np.maximum(e2, 1.0e-30))
    h = float(h0) * e
    rho_eff = effective_dark_density(e2, z, om)
    w_eff = w_eff_from_density(rho_eff, z)
    q = q_from_e2(e2, z)
    dc = comoving_distance_mpc(e2, z, h0)

    rll_f = np.full_like(z, np.nan, dtype=float)
    rll_logit_f = np.full_like(z, np.nan, dtype=float)
    if model == joint.MODEL_RLL:
        _h0, _om, _ol, os0, zt, wt = params
        rll_f = joint.transition_f(z, float(zt), float(wt))
        rll_logit_f = _safe_logit(rll_f)

    rows: list[dict[str, Any]] = []
    for idx, z_value in enumerate(z):
        rows.append(
            {
                "model": model,
                "z": float(z_value),
                "E": float(e[idx]),
                "H": float(h[idx]),
                "rho_de_eff": float(rho_eff[idx]),
                "w_eff": _json_number(w_eff[idx]),
                "q": _json_number(q[idx]),
                "D_C_Mpc": float(dc[idx]),
                "rll_transition_f": _json_number(rll_f[idx]),
                "rll_logit_f": _json_number(rll_logit_f[idx]),
            }
        )
    return rows


def _json_number(value: float) -> float | None:
    if not np.isfinite(value):
        return None
    return float(value)


def load_payload(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_diagnostics(payload: dict[str, Any], z_min: float, z_max: float, n_grid: int) -> list[dict[str, Any]]:
    if n_grid < 3:
        raise ValueError("n-grid must be >= 3")
    z = np.linspace(float(z_min), float(z_max), int(n_grid))
    rows: list[dict[str, Any]] = []
    for row in payload["rows"]:
        rows.extend(diagnostics_for_row(row, z))
    return rows


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_manifest(path: Path, input_path: Path, output_csv: Path, payload: dict[str, Any], z_min: float, z_max: float, n_grid: int) -> None:
    manifest = {
        "schema": "rll.effective_dynamics_manifest.v1",
        "created_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "source_artifact": str(input_path.relative_to(BASE_DIR)),
        "output_csv": str(output_csv.relative_to(BASE_DIR)),
        "z_grid": {"z_min": float(z_min), "z_max": float(z_max), "n_grid": int(n_grid)},
        "source_schema": payload.get("schema"),
        "source_claim_allowed": payload.get("claim_allowed"),
        "claim_allowed": False,
        "interpretation": "Post-fit functional diagnostics only; not a new cosmological fit.",
        "quantities": ["E", "H", "rho_de_eff", "w_eff", "q", "D_C_Mpc", "rll_transition_f", "rll_logit_f"],
        "raw_datasets_modified": False,
        "canonical_results_modified": False,
    }
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compute effective dynamics diagnostics from a Structure-D joint likelihood JSON.")
    parser.add_argument("--input-json", default=str(DEFAULT_INPUT), help="Joint likelihood JSON artifact to analyze.")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR), help="Directory for derived diagnostics.")
    parser.add_argument("--z-min", type=float, default=0.0)
    parser.add_argument("--z-max", type=float, default=3.0)
    parser.add_argument("--n-grid", type=int, default=301)
    return parser


def main(argv: list[str] | None = None) -> dict[str, str]:
    args = build_parser().parse_args(argv)
    input_path = Path(args.input_json).resolve()
    output_dir = Path(args.output_dir).resolve()
    payload = load_payload(input_path)
    rows = build_diagnostics(payload, args.z_min, args.z_max, args.n_grid)

    stem = input_path.stem
    output_csv = output_dir / f"{stem}_effective_dynamics.csv"
    output_manifest = output_dir / f"{stem}_effective_dynamics_manifest.json"
    write_csv(output_csv, rows)
    write_manifest(output_manifest, input_path, output_csv, payload, args.z_min, args.z_max, args.n_grid)
    print(f"Wrote: {output_csv.relative_to(BASE_DIR)}")
    print(f"Wrote: {output_manifest.relative_to(BASE_DIR)}")
    return {"csv": str(output_csv), "manifest": str(output_manifest)}


if __name__ == "__main__":
    main()
