"""
[COD] Modelos de H(z) e distancia de luminosidade para fit contra Pantheon+ real
Todos em unidades: H0 em km/s/Mpc, c em km/s
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize

C_LIGHT = 299792.458  # km/s

def E_lcdm(z, Om):
    return np.sqrt(Om * (1 + z)**3 + (1 - Om))

def E_cpl(z, Om, w0, wa):
    """w0waCDM (Chevallier-Polarski-Linder) - adversario correto do RLL"""
    Ode = 1 - Om
    de_term = (1 + z)**(3 * (1 + w0 + wa)) * np.exp(-3 * wa * z / (1 + z))
    return np.sqrt(Om * (1 + z)**3 + Ode * de_term)

def f_transition_original(z, z_t=0.5, sharpness=5.0):
    """[HIP] Funcao de transicao RLL original -> produz wa_eff=+0.32 (jah calculado em sessao anterior)"""
    return 1.0 / (1.0 + np.exp(-sharpness * (z - z_t)))

def f_transition_optionA(z, z_t=0.5, sharpness=5.0):
    """[HIP] Opcao A: g(z) = 1 - f(z), transicao invertida"""
    return 1.0 - f_transition_original(z, z_t, sharpness)

_ZGRID = np.linspace(0, 3.0, 4000)  # cobre z ate 3.0, dataset vai ate 2.26

def _rho_de_grid(w0, wa, transition_fn, z_t, sharpness):
    """[COD] Pre-computa rho_de em grade fina via integracao cumulativa (trapezio), O(N) em vez de O(N) quads."""
    g = transition_fn(_ZGRID, z_t, sharpness)
    w = w0 + wa * g
    integrand = 3 * (1 + w) / (1 + _ZGRID)
    cumint = np.concatenate(([0.0], np.cumsum(
        (integrand[1:] + integrand[:-1]) / 2 * np.diff(_ZGRID)
    )))
    return np.exp(cumint)

def E_rll(z, Om, w0, wa, transition_fn, z_t=0.5, sharpness=5.0):
    """
    [HIP] Modelo RLL: interpola entre w0 (z baixo) e w0+wa (z alto)
    via funcao de transicao, ao inves da parametrizacao CPL analitica pura.
    Vetorizado: interpola rho_de(z) a partir de grade pre-computada (trapezio),
    equivalente numericamente ao quad aninhado mas ~100x mais rapido.
    """
    rho_de_grid = _rho_de_grid(w0, wa, transition_fn, z_t, sharpness)
    z_arr = np.atleast_1d(z)
    rho_de = np.interp(z_arr, _ZGRID, rho_de_grid)
    Ode = 1 - Om
    result = np.sqrt(Om * (1 + z_arr)**3 + Ode * rho_de)
    return result[0] if np.isscalar(z) else result

_ZGRID_DL = np.linspace(0, 3.0, 4000)

def dL(z, H0, E_func, **kwargs):
    """
    Distancia de luminosidade via integracao cumulativa vetorizada (trapezio)
    de 1/E(z) numa grade comum, depois interpolada nos pontos z pedidos.
    Equivalente numericamente ao quad ponto-a-ponto, ordens de magnitude mais rapido.
    """
    inv_E = 1.0 / E_func(_ZGRID_DL, **kwargs)
    cumint = np.concatenate(([0.0], np.cumsum(
        (inv_E[1:] + inv_E[:-1]) / 2 * np.diff(_ZGRID_DL)
    )))
    z_arr = np.atleast_1d(z)
    integral = np.interp(z_arr, _ZGRID_DL, cumint)
    result = (C_LIGHT / H0) * (1 + z_arr) * integral
    return result[0] if np.isscalar(z) else result

def mu_theory(z, H0, E_func, **kwargs):
    d_L = dL(z, H0, E_func, **kwargs)
    return 5 * np.log10(d_L) + 25

def chi2(params, z, mu_obs, mu_err, model="lcdm", **fixed_kwargs):
    if model == "lcdm":
        H0, Om = params
        mu_th = mu_theory(z, H0, E_lcdm, Om=Om)
    elif model == "cpl":
        H0, Om, w0, wa = params
        mu_th = mu_theory(z, H0, E_cpl, Om=Om, w0=w0, wa=wa)
    elif model == "rll_original":
        H0, Om, w0, wa = params
        mu_th = mu_theory(z, H0, E_rll, Om=Om, w0=w0, wa=wa,
                           transition_fn=f_transition_original, **fixed_kwargs)
    elif model == "rll_optionA":
        H0, Om, w0, wa = params
        mu_th = mu_theory(z, H0, E_rll, Om=Om, w0=w0, wa=wa,
                           transition_fn=f_transition_optionA, **fixed_kwargs)
    else:
        raise ValueError(model)
    return np.sum(((mu_obs - mu_th) / mu_err)**2)

def fit_model(z, mu_obs, mu_err, model, x0, **fixed_kwargs):
    res = minimize(chi2, x0, args=(z, mu_obs, mu_err, model), method="Nelder-Mead",
                    options={"xatol": 1e-6, "fatol": 1e-6, "maxiter": 5000},
                    kwargs=fixed_kwargs if False else None) if False else \
          minimize(lambda p: chi2(p, z, mu_obs, mu_err, model, **fixed_kwargs), x0,
                    method="Nelder-Mead", options={"xatol": 1e-6, "fatol": 1e-6, "maxiter": 5000})
    return res
