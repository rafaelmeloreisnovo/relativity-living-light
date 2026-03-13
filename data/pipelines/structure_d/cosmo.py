"""Referência explícita de saídas textuais deste módulo/pipeline."""

TEXTUAL_OUTPUTS = []

import numpy as np

def E_LCDM(z, Om=0.3, Or=0.0, Ol=0.7):
    z = np.asarray(z, dtype=float)
    return np.sqrt(Om*(1+z)**3 + Or*(1+z)**4 + Ol)

def H_of_z(z, H0=70.0, Om=0.3, Or=0.0, Ol=0.7, Omega_f=None):
    """H(z) = H0 * sqrt( Om(1+z)^3 + Or(1+z)^4 + Ol + Omega_f(z) )."""
    z = np.asarray(z, dtype=float)
    add = 0.0
    if Omega_f is not None:
        add = np.asarray(Omega_f(z), dtype=float)
    return H0 * np.sqrt(Om*(1+z)**3 + Or*(1+z)**4 + Ol + add)

def Omega_m_z(z, Om=0.3, Or=0.0, Ol=0.7):
    z = np.asarray(z, dtype=float)
    Ez2 = Om*(1+z)**3 + Or*(1+z)**4 + Ol
    return (Om*(1+z)**3) / Ez2


def omega_astro(z, A=0.0, n=0.0, z_c=1.0):
    """Termo astrofísico fenomenológico: A(1+z)^n exp(-z/z_c)."""
    z = np.asarray(z, dtype=float)
    zc = float(z_c)
    if zc <= 0.0 or not np.isfinite(zc):
        return np.full_like(z, np.nan, dtype=float)
    return A * (1.0 + z) ** n * np.exp(-z / zc)


def omega_ede(z, Omega_e=0.0, m=0.0):
    """Componente simplificada de energia escura precoce."""
    z = np.asarray(z, dtype=float)
    return Omega_e * (1.0 + z) ** m


def omega_topological(z, beta=0.0):
    """Termo topológico β/a² = β(1+z)^2."""
    z = np.asarray(z, dtype=float)
    return beta * (1.0 + z) ** 2


def omega_brane_quadratic(z, lambda_brane=np.inf, Om=0.3, Or=0.0, Ol=0.7):
    """Correção tipo brana: (ρ/ρ_λ)^2 com ρ_λ adimensional=lambda_brane."""
    z = np.asarray(z, dtype=float)
    lam = float(lambda_brane)
    if not np.isfinite(lam) or lam <= 0.0:
        return np.zeros_like(z, dtype=float)
    rho_eff = Om * (1.0 + z) ** 3 + Or * (1.0 + z) ** 4 + Ol
    return (rho_eff**2) / lam


def H_of_z_extended(
    z,
    H0=70.0,
    Om=0.3,
    Or=0.0,
    Ol=0.7,
    Onu=0.0,
    Omega_q=None,
    Omega_astro=None,
    Omega_fund=None,
):
    """H(z) para ΛCDM++ com separação astro/fundamental e termos extras.

    H²/H0² = Ωm(1+z)^3 + (Ωr+Ων)(1+z)^4 + ΩΛ + Ωastro(z) + Ωfund(z) + Ωq(z)
    """
    z = np.asarray(z, dtype=float)
    omega_q = 0.0 if Omega_q is None else np.asarray(Omega_q(z), dtype=float)
    omega_astro_term = 0.0 if Omega_astro is None else np.asarray(Omega_astro(z), dtype=float)
    omega_fund_term = 0.0 if Omega_fund is None else np.asarray(Omega_fund(z), dtype=float)
    Ez2 = (
        Om * (1.0 + z) ** 3
        + (Or + Onu) * (1.0 + z) ** 4
        + Ol
        + omega_astro_term
        + omega_fund_term
        + omega_q
    )
    return H0 * np.sqrt(Ez2)
