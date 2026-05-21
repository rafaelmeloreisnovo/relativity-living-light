import numpy as np

from .cosmo import (
    H_of_z,
    H_of_z_extended,
    omega_astro,
    omega_brane_quadratic,
    omega_ede,
    omega_fundamental,
    omega_neutrino,
    omega_quantum,
    omega_topological,
)
from .feedback_agn import Omega_f_from_feedback
from .growth import f_sigma8_proxy


C_KMS = 299792.458

# Número de parâmetros livres usados na comparação estatística dos modelos.
N_FREE_PARAMS_LCDM = 4
N_FREE_PARAMS_RLL = 7


def _param_float(params, key, default):
    """Retorna parâmetro escalar como float; NaN quando inválido."""
    try:
        value = params.get(key, default)
    except Exception:
        return float("nan")
    try:
        return float(value)
    except (TypeError, ValueError):
        return float("nan")




def _omega_q_constant(_z, params):
    return np.full_like(np.asarray(_z, dtype=float), float(params.get("Omega_q0", 0.0)), dtype=float)


def _omega_astro_term(zz, params):
    return omega_astro(
        zz,
        A=params.get("A_astro", 0.0),
        n=params.get("n_astro", 0.0),
        z_c=params.get("z_c_astro", 1.0),
    )


def _omega_fund_term(zz, params):
    ede = omega_ede(zz, Omega_e=params.get("Omega_e", 0.0), m=params.get("m_ede", 0.0))
    topo = omega_topological(zz, beta=params.get("beta_topo", 0.0))
    brane = omega_brane_quadratic(
        zz,
        lambda_brane=params.get("lambda_brane", np.inf),
        Om=params["Om"],
        Or=params.get("Or", 0.0),
        Ol=params["Ol"],
    )
    return ede + topo + brane

def model_LCDM_Hz(z, params):
    return H_of_z(
        z,
        H0=params["H0"],
        Om=params["Om"],
        Or=params.get("Or", 0.0),
        Ol=params["Ol"],
        Omega_f=None,
    )


def model_RLL_like_Hz(z, params):
    Omega_f = lambda zz: Omega_f_from_feedback(
        zz,
        beta=params.get("beta", 0.0),
        z_peak=params.get("z_peak", 2.0),
        width=params.get("width", 1.0),
    )
    Omega_astro = lambda zz: omega_astro(
        zz,
        A=params.get("A_astro", 0.0),
        n=params.get("n_astro", 0.0),
        z_c=params.get("z_c_astro", 1.0),
    )
    Omega_fund = lambda zz: omega_fundamental(
        zz,
        Omega_e=params.get("Omega_e", 0.0),
        m=params.get("m_ede", 0.0),
        beta_topo=params.get("beta_topo", 0.0),
    )
    Omega_nu = lambda zz: omega_neutrino(zz, Omega_nu=params.get("Omega_nu", 0.0))
    Omega_q = lambda zz: omega_quantum(
        zz,
        Omega_q0=params.get("Omega_q0", 0.0),
        q_power=params.get("q_power", 0.0),
    )
    return H_of_z(
        z,
        H0=params["H0"],
        Om=params["Om"],
        Or=params.get("Or", 0.0),
        Ol=params["Ol"],
        Omega_f=Omega_f,
        Omega_astro=Omega_astro,
        Omega_fund=Omega_fund,
        Omega_nu=Omega_nu,
        Omega_q=Omega_q,
    )


def model_RLL_LCDMpp_Hz(z, params):
    """Extensão ΛCDM++: separa Ω_astro e Ω_fund com neutrinos e Ω_q."""
    return H_of_z_extended(
        z,
        H0=params["H0"],
        Om=params["Om"],
        Or=params.get("Or", 0.0),
        Ol=params["Ol"],
        Onu=params.get("Onu", 0.0),
        Omega_q=lambda zz: _omega_q_constant(zz, params),
        Omega_astro=lambda zz: _omega_astro_term(zz, params),
        Omega_fund=lambda zz: _omega_fund_term(zz, params),
    )


def model_LCDM_fs8(z, params):
    return f_sigma8_proxy(
        z,
        sigma8_0=params.get("sigma8", 0.8),
        gamma=params.get("gamma", 0.55),
        Om=params["Om"],
        Or=params.get("Or", 0.0),
        Ol=params["Ol"],
        use_feedback=False,
    )


def model_RLL_like_fs8(z, params):
    return f_sigma8_proxy(
        z,
        sigma8_0=params.get("sigma8", 0.8),
        gamma=params.get("gamma", 0.55),
        Om=params["Om"],
        Or=params.get("Or", 0.0),
        Ol=params["Ol"],
        use_feedback=True,
        alpha=params.get("alpha", 0.05),
        z_peak=params.get("z_peak", 2.0),
        width=params.get("width", 1.0),
    )


def _comoving_distance_mpc(z, params, hz_fn, n_steps=512):
    z_scalar = float(z)
    if not np.isfinite(z_scalar) or z_scalar < 0.0:
        return np.nan
    grid = np.linspace(0.0, z_scalar, int(max(n_steps, 16)))
    hz = np.asarray(hz_fn(grid, params), dtype=float)
    if np.any(~np.isfinite(hz)) or np.any(hz <= 0.0):
        return np.nan
    return float(np.trapezoid(C_KMS / hz, grid))


def _rs_drag_mpc(params):
    h0 = float(params["H0"])
    om = float(params["Om"])
    ob_h2 = float(params.get("Ob_h2", 0.02236))
    return 147.78 * (om * (h0 / 100.0) ** 2 / 0.1432) ** (-0.255) * (ob_h2 / 0.02236) ** (-0.134)


def _dv_over_rs(z, params, hz_fn):
    z_arr = np.asarray(z, dtype=float)
    out = np.full_like(z_arr, np.nan, dtype=float)
    rs = _rs_drag_mpc(params)
    if not np.isfinite(rs) or rs <= 0.0:
        return out

    for idx, z_val in np.ndenumerate(z_arr):
        if not np.isfinite(z_val) or z_val <= 0.0:
            continue
        hz_val = float(hz_fn(np.array([z_val], dtype=float), params)[0])
        dc_val = _comoving_distance_mpc(z_val, params, hz_fn)
        if not np.isfinite(hz_val) or hz_val <= 0.0 or not np.isfinite(dc_val) or dc_val <= 0.0:
            continue
        dv_val = (z_val * C_KMS / hz_val * dc_val**2) ** (1.0 / 3.0)
        out[idx] = dv_val / rs
    return out


def model_LCDM_bao_dv_over_rs(z, params):
    return _dv_over_rs(z, params, model_LCDM_Hz)


def model_RLL_like_bao_dv_over_rs(z, params):
    return _dv_over_rs(z, params, model_RLL_like_Hz)


def cs2_toy_eft(z, params):
    """Toy EFT para velocidade de som efetiva.

    Parametrização (vetorizada em NumPy):
      c_s^2(z) = c0 + c1 * z/(1+z) + c_log * log(1+z)

    onde:
      - c0    := params['cs2_0']   (default 1.0)
      - c1    := params['cs2_a']   (default 0.0)
      - c_log := params['cs2_log'] (default 0.0)

    A função é robusta para domínio inválido (z <= -1), parâmetros não numéricos,
    NaN/Inf: retorna arrays contendo NaN nesses pontos/entradas, sem lançar exceção.
    """
    z_arr = np.asarray(z, dtype=float)
    c0 = _param_float(params, "cs2_0", 1.0)
    c1 = _param_float(params, "cs2_a", 0.0)
    c_log = _param_float(params, "cs2_log", 0.0)

    valid = np.isfinite(z_arr) & (z_arr > -1.0)
    out = np.full_like(z_arr, np.nan, dtype=float)
    if not np.isfinite(c0) or not np.isfinite(c1) or not np.isfinite(c_log):
        return out

    with np.errstate(divide="ignore", invalid="ignore", over="ignore"):
        out[valid] = c0 + c1 * (z_arr[valid] / (1.0 + z_arr[valid])) + c_log * np.log1p(
            z_arr[valid]
        )
    return out


def stability_flags_toy_eft(z_grid, params):
    """Diagnóstico central de estabilidade física para o toy EFT."""
    z_arr = np.asarray(z_grid, dtype=float)
    cs2 = cs2_toy_eft(z_arr, params)

    finite_cs2 = np.isfinite(cs2)
    finite_z = np.isfinite(z_arr)
    domain_violation = np.any(~finite_z) or np.any(z_arr <= -1.0)

    if np.any(finite_cs2):
        cs2_min = float(np.min(cs2[finite_cs2]))
        cs2_max = float(np.max(cs2[finite_cs2]))
    else:
        cs2_min = float("nan")
        cs2_max = float("nan")

    has_non_finite = np.any(~finite_cs2)
    has_negative_cs2 = np.any(cs2[finite_cs2] < 0.0)
    has_superluminal_cs2 = np.any(cs2[finite_cs2] > 1.0)

    w0 = _param_float(params, "w0", -1.0)
    wa = _param_float(params, "wa", 0.0)
    with np.errstate(invalid="ignore"):
        w_eff = w0 + wa * (z_arr / (1.0 + z_arr))
    finite_w_eff = np.isfinite(w_eff)
    has_ghost_instability = (
        not np.isfinite(w0)
        or not np.isfinite(wa)
        or np.any(~finite_w_eff)
        or np.any(w_eff[finite_w_eff] < -1.0)
    )

    is_stable = not (
        has_non_finite
        or has_negative_cs2
        or has_superluminal_cs2
        or has_ghost_instability
        or domain_violation
    )

    return {
        "cs2_min": cs2_min,
        "cs2_max": cs2_max,
        "has_negative_cs2": bool(has_negative_cs2),
        "has_non_finite": bool(has_non_finite),
        "has_superluminal_cs2": bool(has_superluminal_cs2),
        "has_ghost_instability": bool(has_ghost_instability),
        "has_domain_violation": bool(domain_violation),
        "is_stable": bool(is_stable),
    }


def is_physically_stable(params, z_grid):
    """Veto único para inferência: True somente para parâmetros estáveis."""
    try:
        flags = stability_flags_toy_eft(z_grid, params)
    except Exception:
        return False
    return bool(flags.get("is_stable", False))
