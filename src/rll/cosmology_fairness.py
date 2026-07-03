"""Conservative cosmology utilities for fair RLL × LCDM × wCDM × CPL checks.

The functions in this module are intentionally lightweight and deterministic:
they do not download data, do not mutate raw datasets, and keep model equations
separate from any claim about model preference.  They provide the missing
intermediate calculations needed by validation pipelines before AIC/BIC claims
are interpreted.
"""

from __future__ import annotations

from dataclasses import dataclass
from importlib.util import find_spec
from typing import Callable, Mapping

import numpy as np

C_KMS = 299_792.458
DEFAULT_RD_MPC = 147.0


ArrayLike = float | np.ndarray
E2Function = Callable[..., np.ndarray]


@dataclass(frozen=True)
class BaoRatios:
    """BAO distance ratios for a single redshift."""

    dh_over_rd: float
    dm_over_rd: float
    dv_over_rd: float


@dataclass(frozen=True)
class CovarianceReadiness:
    """Failsafe covariance audit result used to gate scientific claims."""

    ready: bool
    claim_allowed: bool
    mode: str
    reason: str
    n: int


def _as_float_array(z: ArrayLike) -> np.ndarray:
    return np.asarray(z, dtype=float)


def _ol_from_closure(om: float, ok: float, orad: float, ol: float | None) -> float:
    if ol is None:
        return 1.0 - float(om) - float(ok) - float(orad)
    return float(ol)


def e2_lcdm(z: ArrayLike, om: float = 0.315, ok: float = 0.0, orad: float = 0.0, ol: float | None = None) -> np.ndarray:
    """Dimensionless Hubble rate squared for ΛCDM with optional curvature."""

    z_arr = _as_float_array(z)
    ol_val = _ol_from_closure(om, ok, orad, ol)
    zp1 = 1.0 + z_arr
    return float(om) * zp1**3 + float(orad) * zp1**4 + float(ok) * zp1**2 + ol_val


def e2_wcdm(
    z: ArrayLike,
    om: float = 0.315,
    w: float = -1.0,
    ok: float = 0.0,
    orad: float = 0.0,
    ode: float | None = None,
) -> np.ndarray:
    """Dimensionless Hubble rate squared for constant-w dark energy."""

    z_arr = _as_float_array(z)
    ode_val = _ol_from_closure(om, ok, orad, ode)
    zp1 = 1.0 + z_arr
    return float(om) * zp1**3 + float(orad) * zp1**4 + float(ok) * zp1**2 + ode_val * zp1 ** (3.0 * (1.0 + float(w)))


def e2_cpl(
    z: ArrayLike,
    om: float = 0.315,
    w0: float = -1.0,
    wa: float = 0.0,
    ok: float = 0.0,
    orad: float = 0.0,
    ode: float | None = None,
) -> np.ndarray:
    """Dimensionless Hubble rate squared for CPL / w0waCDM.

    Uses w(a)=w0+wa(1-a), equivalent to
    ρ_DE(z)/ρ_DE(0)=(1+z)^(3(1+w0+wa)) exp[-3 wa z/(1+z)].
    """

    z_arr = _as_float_array(z)
    ode_val = _ol_from_closure(om, ok, orad, ode)
    zp1 = 1.0 + z_arr
    de = zp1 ** (3.0 * (1.0 + float(w0) + float(wa))) * np.exp(-3.0 * float(wa) * z_arr / zp1)
    return float(om) * zp1**3 + float(orad) * zp1**4 + float(ok) * zp1**2 + ode_val * de


def rll_transition(z: ArrayLike, zt: float, wt: float) -> np.ndarray:
    """Numerically stable RLL logistic transition f(z)."""

    z_arr = _as_float_array(z)
    width = max(float(wt), 1.0e-12)
    return 1.0 / (1.0 + np.exp(np.clip((z_arr - float(zt)) / width, -700.0, 700.0)))


def e2_rll_logistic(
    z: ArrayLike,
    om: float = 0.315,
    os0: float = 0.0,
    zt: float = 1.0,
    wt: float = 0.3,
    ok: float = 0.0,
    orad: float = 0.0,
    ol: float | None = None,
) -> np.ndarray:
    """RLL effective logistic superposition expansion history."""

    z_arr = _as_float_array(z)
    ol_val = _ol_from_closure(om + os0, ok, orad, ol)
    zp1 = 1.0 + z_arr
    fz = rll_transition(z_arr, zt, wt)
    superposition = float(os0) * (fz + (1.0 - fz) * zp1**3)
    return float(om) * zp1**3 + float(orad) * zp1**4 + float(ok) * zp1**2 + ol_val + superposition


def e_of_z(e2_fn: E2Function, z: ArrayLike, *params: object, **kwargs: object) -> np.ndarray:
    e2 = np.asarray(e2_fn(z, *params, **kwargs), dtype=float)
    if np.any(e2 <= 0.0) or np.any(~np.isfinite(e2)):
        return np.full_like(e2, np.nan, dtype=float)
    return np.sqrt(e2)


def h_of_z(h0: float, e2_fn: E2Function, z: ArrayLike, *params: object, **kwargs: object) -> np.ndarray:
    return float(h0) * e_of_z(e2_fn, z, *params, **kwargs)


def comoving_distance_mpc(
    z: float,
    h0: float,
    e2_fn: E2Function,
    *params: object,
    n_steps: int = 2048,
    **kwargs: object,
) -> float:
    """Line-of-sight comoving distance D_C in Mpc."""

    z_val = float(z)
    if not np.isfinite(z_val) or z_val < 0.0:
        return float("nan")
    if z_val == 0.0:
        return 0.0
    grid = np.linspace(0.0, z_val, max(64, int(n_steps)), dtype=float)
    ez = e_of_z(e2_fn, grid, *params, **kwargs)
    if np.any(~np.isfinite(ez)) or np.any(ez <= 0.0):
        return float("nan")
    return float((C_KMS / float(h0)) * np.trapezoid(1.0 / ez, grid))


def transverse_comoving_distance_mpc(
    z: float,
    h0: float,
    ok: float,
    e2_fn: E2Function,
    *params: object,
    n_steps: int = 2048,
    **kwargs: object,
) -> float:
    """Transverse comoving distance D_M with FLRW curvature support."""

    dc = comoving_distance_mpc(z, h0, e2_fn, *params, n_steps=n_steps, **kwargs)
    if not np.isfinite(dc):
        return float("nan")
    ok_val = float(ok)
    if abs(ok_val) < 1.0e-12:
        return dc
    dh = C_KMS / float(h0)
    sqrt_ok = np.sqrt(abs(ok_val))
    arg = sqrt_ok * dc / dh
    if ok_val > 0.0:
        return float(dh / sqrt_ok * np.sinh(arg))
    return float(dh / sqrt_ok * np.sin(arg))


def luminosity_distance_mpc(
    z: float,
    h0: float,
    ok: float,
    e2_fn: E2Function,
    *params: object,
    n_steps: int = 2048,
    **kwargs: object,
) -> float:
    return float((1.0 + float(z)) * transverse_comoving_distance_mpc(z, h0, ok, e2_fn, *params, n_steps=n_steps, **kwargs))


def distance_modulus(
    z: float,
    h0: float,
    ok: float,
    e2_fn: E2Function,
    *params: object,
    absolute_magnitude_offset: float = 0.0,
    n_steps: int = 2048,
    **kwargs: object,
) -> float:
    """Distance modulus μ(z); optional offset covers SN nuisance conventions."""

    dl = luminosity_distance_mpc(z, h0, ok, e2_fn, *params, n_steps=n_steps, **kwargs)
    if not np.isfinite(dl) or dl <= 0.0:
        return float("nan")
    return float(5.0 * np.log10(dl) + 25.0 + float(absolute_magnitude_offset))


def rd_drag_power_law(h0: float, om: float, ob_h2: float = 0.02236) -> float:
    """Fast calibrated drag-horizon approximation used consistently for all models."""

    om_h2 = float(om) * (float(h0) / 100.0) ** 2
    return float(147.78 * (om_h2 / 0.1432) ** (-0.255) * (float(ob_h2) / 0.02236) ** (-0.134))


def bao_distance_ratios(
    z: float,
    h0: float,
    ok: float,
    rd_mpc: float,
    e2_fn: E2Function,
    *params: object,
    n_steps: int = 2048,
    **kwargs: object,
) -> BaoRatios:
    """Return D_H/r_d, D_M/r_d, and D_V/r_d at one redshift."""

    z_val = float(z)
    rd = float(rd_mpc)
    hz = float(h_of_z(h0, e2_fn, z_val, *params, **kwargs))
    dm = transverse_comoving_distance_mpc(z_val, h0, ok, e2_fn, *params, n_steps=n_steps, **kwargs)
    if rd <= 0.0 or hz <= 0.0 or not np.isfinite(dm):
        return BaoRatios(float("nan"), float("nan"), float("nan"))
    dh = C_KMS / hz
    dv = (z_val * dm * dm * dh) ** (1.0 / 3.0) if z_val > 0.0 else 0.0
    return BaoRatios(float(dh / rd), float(dm / rd), float(dv / rd))


def w_eff_rll_density(z: ArrayLike, zt: float, wt: float) -> np.ndarray:
    """Density-consistent effective equation of state for the RLL superposition term.

    For ρ_s(z) ∝ f(z) + [1-f(z)](1+z)^3, this returns
    w_s(z) = -1 + (1+z)/3 d ln ρ_s / dz.
    """

    z_arr = _as_float_array(z)
    width = max(float(wt), 1.0e-12)
    zp1 = 1.0 + z_arr
    fz = rll_transition(z_arr, zt, width)
    fprime = -(fz * (1.0 - fz)) / width
    matter_like = zp1**3
    density_shape = fz + (1.0 - fz) * matter_like
    density_prime = fprime * (1.0 - matter_like) + 3.0 * (1.0 - fz) * zp1**2
    with np.errstate(divide="ignore", invalid="ignore"):
        return -1.0 + zp1 * density_prime / (3.0 * density_shape)


def aic(chi2: float, k: int) -> float:
    return float(float(chi2) + 2.0 * int(k))


def bic(chi2: float, k: int, n_obs: int) -> float:
    n = int(n_obs)
    if n <= 0:
        raise ValueError("n_obs must be positive for BIC")
    return float(float(chi2) + int(k) * np.log(n))


def aicc(chi2: float, k: int, n_obs: int) -> float:
    """Small-sample corrected Akaike information criterion."""

    k_int = int(k)
    n = int(n_obs)
    if n <= k_int + 1:
        raise ValueError("AICc undefined when n_obs <= k + 1")
    return float(aic(chi2, k_int) + (2.0 * k_int * (k_int + 1)) / (n - k_int - 1))


def linear_growth_dplus(
    z: float,
    e2_fn: E2Function,
    om: float,
    *params: object,
    n_steps: int = 2048,
    **kwargs: object,
) -> float:
    """Approximate GR linear growth factor D+(z), normalized to D+(0)=1.

    Uses the standard integral solution for smooth dark energy backgrounds:
    D(a) ∝ E(a) ∫_0^a da' / [a'^3 E(a')^3].
    """

    z_val = float(z)
    if not np.isfinite(z_val) or z_val < 0.0:
        return float("nan")
    a = 1.0 / (1.0 + z_val)

    def raw_growth(a_upper: float) -> float:
        grid = np.linspace(1.0e-4, float(a_upper), max(128, int(n_steps)), dtype=float)
        z_grid = 1.0 / grid - 1.0
        e_grid = e_of_z(e2_fn, z_grid, *params, **kwargs)
        if np.any(~np.isfinite(e_grid)) or np.any(e_grid <= 0.0):
            return float("nan")
        integral = np.trapezoid(1.0 / (grid**3 * e_grid**3), grid)
        e_a = float(e_of_z(e2_fn, 1.0 / float(a_upper) - 1.0, *params, **kwargs))
        return float(2.5 * float(om) * e_a * integral)

    d0 = raw_growth(1.0)
    dz = raw_growth(a)
    if not np.isfinite(d0) or d0 <= 0.0 or not np.isfinite(dz):
        return float("nan")
    return float(dz / d0)


def growth_rate_f(
    z: float,
    e2_fn: E2Function,
    om: float,
    *params: object,
    delta_ln_a: float = 1.0e-3,
    **kwargs: object,
) -> float:
    """Numerical f=dlnD/dlna from the normalized D+(z)."""

    z_val = float(z)
    a = 1.0 / (1.0 + z_val)
    step = float(delta_ln_a)
    a_hi = min(1.0, a * np.exp(step))
    a_lo = max(1.0e-4, a * np.exp(-step))
    z_hi = 1.0 / a_hi - 1.0
    z_lo = 1.0 / a_lo - 1.0
    d_hi = linear_growth_dplus(z_hi, e2_fn, om, *params, **kwargs)
    d_lo = linear_growth_dplus(z_lo, e2_fn, om, *params, **kwargs)
    if d_hi <= 0.0 or d_lo <= 0.0 or not np.isfinite(d_hi + d_lo):
        return float("nan")
    return float((np.log(d_hi) - np.log(d_lo)) / (np.log(a_hi) - np.log(a_lo)))


def fsigma8_linear(
    z: float,
    sigma8_0: float,
    e2_fn: E2Function,
    om: float,
    *params: object,
    **kwargs: object,
) -> float:
    dplus = linear_growth_dplus(z, e2_fn, om, *params, **kwargs)
    fz = growth_rate_f(z, e2_fn, om, *params, **kwargs)
    return float(float(sigma8_0) * dplus * fz)


def s8_parameter(sigma8: float, om: float) -> float:
    return float(float(sigma8) * np.sqrt(float(om) / 0.3))


def covariance_readiness(covariance: ArrayLike, *, mode: str) -> CovarianceReadiness:
    """Validate covariance and gate claims by covariance provenance mode.

    `mode='official_full'` is required for `claim_allowed=True`.  Valid partial
    modes such as `diagonal`, `block_summary`, or `compressed_prior` can be ready
    for exploratory calculations but remain blocked for strong claims.
    """

    cov = np.asarray(covariance, dtype=float)
    mode_text = str(mode)
    if cov.ndim != 2 or cov.shape[0] != cov.shape[1]:
        return CovarianceReadiness(False, False, mode_text, "covariance is not square", 0)
    n = int(cov.shape[0])
    if np.any(~np.isfinite(cov)):
        return CovarianceReadiness(False, False, mode_text, "covariance contains non-finite values", n)
    if not np.allclose(cov, cov.T, atol=1.0e-10, rtol=0.0):
        return CovarianceReadiness(False, False, mode_text, "covariance is not symmetric", n)
    if np.any(np.diag(cov) <= 0.0):
        return CovarianceReadiness(False, False, mode_text, "covariance diagonal is not strictly positive", n)
    evals = np.linalg.eigvalsh(cov)
    if np.min(evals) < -1.0e-10:
        return CovarianceReadiness(False, False, mode_text, "covariance is not positive semidefinite", n)
    if mode_text != "official_full":
        return CovarianceReadiness(True, False, mode_text, "valid covariance, but not an official full covariance", n)
    return CovarianceReadiness(True, True, mode_text, "official full covariance is valid", n)



def growth_backend_benchmark_status(*, require_external: bool = False) -> dict[str, object]:
    """Report whether an external CLASS/CAMB growth benchmark is available.

    The local D+/fσ8 implementation is an approximation.  This function is a
    claim gate: if neither CLASS (``classy``) nor CAMB is installed, strong
    growth claims must remain blocked rather than silently treating the local
    approximation as a Boltzmann-code benchmark.
    """

    backends = {"classy": find_spec("classy") is not None, "camb": find_spec("camb") is not None}
    available = [name for name, present in backends.items() if present]
    status = "available" if available else "skipped_missing_backend"
    claim_allowed = bool(available) and bool(require_external)
    result: dict[str, object] = {
        "status": status,
        "available_backends": available,
        "checked_backends": sorted(backends),
        "claim_allowed": claim_allowed,
        "reason": (
            "External CLASS/CAMB backend is importable; run numerical benchmark before strong claims."
            if available
            else "CLASS/CAMB backend is not installed in this environment; D+/fσ8 remains an internal approximation."
        ),
    }
    if claim_allowed:
        result.update(
            {
                "source": available,
                "metric": "fsigma8_residuals",
                "baseline": ["LCDM_growth", "CPL_growth"],
                "uncertainty_or_covariance_status": "external_backend_benchmark_required",
                "command": "python -m data.pipelines.structure_d.joint_real_likelihood",
                "claim_boundary": (
                    "Backend availability is a technical evidence gate for running an external growth "
                    "benchmark; it does not by itself confirm or validate RLL against LCDM/CPL."
                ),
            }
        )
    return result

def load_parameter_origin_registry(registry: Mapping[str, object]) -> dict[str, object]:
    """Validate the minimal parameter-origin registry contract."""

    required_top = {"schema", "parameters"}
    missing_top = required_top.difference(registry)
    if missing_top:
        raise ValueError(f"parameter registry missing keys: {sorted(missing_top)}")
    params = registry["parameters"]
    if not isinstance(params, list) or not params:
        raise ValueError("parameter registry requires a non-empty parameters list")
    required_param = {"name", "model", "origin", "role", "status", "reference_keys"}
    for idx, item in enumerate(params):
        if not isinstance(item, Mapping):
            raise ValueError(f"parameter entry {idx} is not an object")
        missing = required_param.difference(item)
        if missing:
            raise ValueError(f"parameter entry {idx} missing keys: {sorted(missing)}")
    return dict(registry)
