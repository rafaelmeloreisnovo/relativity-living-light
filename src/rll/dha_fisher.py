"""Deterministic DHA Fisher forecast utilities.

Implements a compact Fisher information calculation for an oscillatory
modulation in the matter power spectrum,

P_obs(k) = P_LCDM(k) * (1 + A0 * cos(omega * ln(k/k0))).
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from scipy.integrate import simpson


@dataclass(frozen=True)
class DHAConfig:
    k_min: float = 0.01
    k_max: float = 0.30
    n_k: int = 500
    v_survey_mpc3_h3: float = 1.0e10
    n_gal_h3_mpc3: float = 3.0e-4
    k0: float = 0.05


def base_frequency_from_tensor_grid(n_states: int) -> float:
    """Return omega = 2*pi/ln(N), with N > 1."""
    if n_states <= 1:
        raise ValueError("n_states must be > 1")
    return (2.0 * math.pi) / math.log(n_states)


def spiral_modulated_frequency(omega_base: float, spiral_factor: float = math.sqrt(3.0) / 2.0) -> float:
    """Secondary harmonic induced by spiral contraction factor."""
    return omega_base * spiral_factor


def _p_lcdm_proxy(k: np.ndarray) -> np.ndarray:
    """Smooth LCDM-like proxy used for fast deterministic forecasts."""
    return 10000.0 * (k / 0.05) ** 1.2 * np.exp(-k / 0.1)


def fisher_matrix_dha(amplitude_a0: float, omega: float, config: DHAConfig | None = None) -> tuple[np.ndarray, np.ndarray]:
    """Compute Fisher( A0, omega ) and covariance matrix."""
    cfg = config or DHAConfig()
    k = np.logspace(np.log10(cfg.k_min), np.log10(cfg.k_max), cfg.n_k)
    p_lcdm = _p_lcdm_proxy(k)

    ln_k = np.log(k / cfg.k0)
    dP_dA0 = p_lcdm * np.cos(omega * ln_k)
    dP_dw = p_lcdm * amplitude_a0 * (-np.sin(omega * ln_k)) * ln_k

    density_states = (k**2) / (2.0 * math.pi**2) * cfg.v_survey_mpc3_h3
    sigma_p_sq = 2.0 * (p_lcdm + 1.0 / cfg.n_gal_h3_mpc3) ** 2 / density_states

    f_a0_a0 = simpson((dP_dA0 * dP_dA0) / sigma_p_sq, x=k)
    f_w_w = simpson((dP_dw * dP_dw) / sigma_p_sq, x=k)
    f_a0_w = simpson((dP_dA0 * dP_dw) / sigma_p_sq, x=k)

    fisher = np.array([[f_a0_a0, f_a0_w], [f_a0_w, f_w_w]], dtype=float)
    covariance = np.linalg.inv(fisher)
    return fisher, covariance


def run_reference_forecast(n_vectors: int = 1000, amplitude_a0: float = 0.02) -> dict[str, float]:
    """Reference forecast for Sigma_RAFAELIA-like 10x10x10 grid."""
    omega = base_frequency_from_tensor_grid(n_vectors)
    omega_secondary = spiral_modulated_frequency(omega)

    _, cov = fisher_matrix_dha(amplitude_a0=amplitude_a0, omega=omega)
    err_a0 = float(np.sqrt(cov[0, 0]))
    err_omega = float(np.sqrt(cov[1, 1]))

    return {
        "omega_base": omega,
        "omega_secondary": omega_secondary,
        "A0": amplitude_a0,
        "err_A0": err_a0,
        "err_omega": err_omega,
        "snr_A0": amplitude_a0 / err_a0,
    }
