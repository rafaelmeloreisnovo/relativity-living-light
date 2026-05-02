"""Deterministic DHA extractor for DESI/BOSS-like power spectrum data."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from astropy.timeseries import LombScargle
from scipy.optimize import curve_fit


@dataclass(frozen=True)
class InstantonFit:
    amplitude: float
    omega: float
    phi: float
    err_amplitude: float
    err_omega: float
    err_phi: float


class DESI_DHA_Extractor:
    """Extract discrete scale-invariance signatures from LSS spectra."""

    def __init__(self, k0: float = 0.05):
        self.k0 = k0

    def extract_residuals(self, k: np.ndarray, pk_obs: np.ndarray, pk_smooth: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        mask = (pk_smooth > 1e-10) & (k > 0)
        k_clean = k[mask]
        pk_clean = pk_obs[mask]
        smooth_clean = pk_smooth[mask]

        residuals = (pk_clean - smooth_clean) / smooth_clean
        log_k = np.log(k_clean / self.k0)
        return k_clean, log_k, residuals, smooth_clean, mask

    def compute_lomb_scargle(
        self,
        log_k: np.ndarray,
        residuals: np.ndarray,
        err_residuals: np.ndarray,
        omega_min: float = 0.1,
        omega_max: float = 5.0,
        n_grid: int = 2000,
    ) -> tuple[np.ndarray, np.ndarray, float, float]:
        omega_grid = np.linspace(omega_min, omega_max, n_grid)
        ls = LombScargle(log_k, residuals, err_residuals)
        power = ls.power(omega_grid)
        best_idx = int(np.argmax(power))
        best_omega = float(omega_grid[best_idx])
        fap = float(ls.false_alarm_probability(power[best_idx]))
        return omega_grid, power, best_omega, fap

    def fit_instanton_model(
        self,
        log_k: np.ndarray,
        residuals: np.ndarray,
        err_residuals: np.ndarray,
        omega_guess: float,
    ) -> InstantonFit | None:
        def dha_wave(x: np.ndarray, a0: float, omega: float, phi: float) -> np.ndarray:
            return a0 * np.cos(omega * x + phi)

        p0 = [0.02, omega_guess, 0.0]
        bounds = ([0.0, omega_guess * 0.5, -np.pi], [1.0, omega_guess * 1.5, np.pi])
        try:
            popt, pcov = curve_fit(
                dha_wave,
                log_k,
                residuals,
                sigma=err_residuals,
                absolute_sigma=True,
                p0=p0,
                bounds=bounds,
                maxfev=50_000,
            )
        except RuntimeError:
            return None

        errs = np.sqrt(np.diag(pcov))
        return InstantonFit(
            amplitude=float(popt[0]),
            omega=float(popt[1]),
            phi=float(popt[2]),
            err_amplitude=float(errs[0]),
            err_omega=float(errs[1]),
            err_phi=float(errs[2]),
        )


def run_dha_pipeline(data_path: str | Path | None = None, rng_seed: int = 12345) -> dict[str, float]:
    rng = np.random.default_rng(rng_seed)
    if data_path is None:
        k = np.logspace(-2, 0.5, 150)
        pk_smooth = 10000 * (k / 0.05) ** 1.2 * np.exp(-k / 0.1)
        true_omega = 2 * np.pi / np.log(1000)
        pk_obs = pk_smooth * (1 + 0.03 * np.cos(true_omega * np.log(k / 0.05) + 0.5))
        err_pk = 0.05 * pk_smooth
        pk_obs = pk_obs + rng.normal(0.0, err_pk)
    else:
        data = np.loadtxt(data_path)
        k, pk_obs, err_pk, pk_smooth = data[:, 0], data[:, 1], data[:, 2], data[:, 3]

    extractor = DESI_DHA_Extractor()
    k_clean, log_k, residuals, smooth_clean, mask = extractor.extract_residuals(k, pk_obs, pk_smooth)
    err_residuals = (err_pk[mask] / smooth_clean).astype(float)

    residuals = residuals - np.average(residuals, weights=1.0 / np.maximum(err_residuals, 1e-8) ** 2)
    _, _, best_omega, fap = extractor.compute_lomb_scargle(log_k, residuals, err_residuals, omega_min=0.4, omega_max=2.0)
    fit = extractor.fit_instanton_model(log_k, residuals, err_residuals, best_omega)

    out = {"best_omega": best_omega, "fap": fap}
    if fit is not None:
        out.update(
            {
                "amplitude": fit.amplitude,
                "omega_fit": fit.omega,
                "phi_fit": fit.phi,
                "err_amplitude": fit.err_amplitude,
                "err_omega": fit.err_omega,
                "err_phi": fit.err_phi,
            }
        )
    return out
