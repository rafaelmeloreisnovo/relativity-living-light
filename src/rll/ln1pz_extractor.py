"""Extractor for log-periodic DHA signatures in ln(1+z) space."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class Ln1pzFitResult:
    amplitude: float
    omega: float
    phase: float
    offset: float
    rmse: float


def _fit_linear_at_omega(x: np.ndarray, y: np.ndarray, omega: float) -> tuple[float, float, float, float]:
    # y ~ c0 + b*cos(omega*x) + s*sin(omega*x)
    design = np.column_stack([np.ones_like(x), np.cos(omega * x), np.sin(omega * x)])
    coeffs, *_ = np.linalg.lstsq(design, y, rcond=None)
    fit = design @ coeffs
    rmse = float(np.sqrt(np.mean((y - fit) ** 2)))
    return float(coeffs[0]), float(coeffs[1]), float(coeffs[2]), rmse


def fit_log_periodic_signal(ln1pz: np.ndarray, residual: np.ndarray, *, omega_init: float = 0.91) -> Ln1pzFitResult:
    omega_grid = np.linspace(max(0.05, omega_init - 0.35), omega_init + 0.35, 800)
    best = None
    for omega in omega_grid:
        c0, b, s, rmse = _fit_linear_at_omega(ln1pz, residual, float(omega))
        if best is None or rmse < best[-1]:
            best = (c0, b, s, float(omega), rmse)

    assert best is not None
    c0, b, s, omega, rmse = best
    amplitude = float(np.hypot(b, s))
    phase = float(np.arctan2(-s, b))
    return Ln1pzFitResult(amplitude=amplitude, omega=omega, phase=phase, offset=c0, rmse=rmse)


def run_catalog_extraction(input_csv: str | Path, output_csv: str | Path, *, omega_init: float = 0.91) -> Ln1pzFitResult:
    data = pd.read_csv(input_csv)
    required_cols = {"z", "pk_obs", "pk_baseline"}
    missing = required_cols.difference(data.columns)
    if missing:
        raise ValueError(f"missing required columns: {sorted(missing)}")

    z = data["z"].to_numpy(dtype=float)
    ln1pz = np.log1p(z)
    residual = (data["pk_obs"].to_numpy(dtype=float) / data["pk_baseline"].to_numpy(dtype=float)) - 1.0

    fit_result = fit_log_periodic_signal(ln1pz, residual, omega_init=omega_init)
    modeled = fit_result.offset + fit_result.amplitude * np.cos(fit_result.omega * ln1pz + fit_result.phase)

    out = pd.DataFrame({
        "z": z,
        "ln1pz": ln1pz,
        "residual": residual,
        "dha_fit": modeled,
        "fit_residual": residual - modeled,
    })
    out_path = Path(output_csv)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(out_path, index=False)
    return fit_result
