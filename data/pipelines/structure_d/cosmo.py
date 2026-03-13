"""Referência explícita de saídas textuais deste módulo/pipeline."""

TEXTUAL_OUTPUTS = []

import numpy as np


def omega_astro(z, A=0.0, n=0.0, z_c=1.0):
    """Componente astrofísica efetiva: A(1+z)^n exp(-z/z_c)."""
    z = np.asarray(z, dtype=float)
    zc = float(z_c)
    if not np.isfinite(zc) or zc <= 0.0:
        return np.full_like(z, np.nan, dtype=float)
    return float(A) * (1.0 + z) ** float(n) * np.exp(-z / zc)


def omega_fundamental(z, Omega_e=0.0, m=0.0, beta_topo=0.0):
    """Componente fundamental simplificada: EDE + termo topológico β/a²."""
    z = np.asarray(z, dtype=float)
    return float(Omega_e) * (1.0 + z) ** float(m) + float(beta_topo) * (1.0 + z) ** 2


def omega_neutrino(z, Omega_nu=0.0):
    """Aproximação mínima para neutrinos não-relativísticos: Ων(1+z)^3."""
    z = np.asarray(z, dtype=float)
    return float(Omega_nu) * (1.0 + z) ** 3


def omega_quantum(z, Omega_q0=0.0, q_power=0.0):
    """Termo quântico efetivo fenomenológico: Ωq0(1+z)^q_power."""
    z = np.asarray(z, dtype=float)
    return float(Omega_q0) * (1.0 + z) ** float(q_power)


def E2_total(
    z,
    Om=0.3,
    Or=0.0,
    Ol=0.7,
    Omega_f=None,
    Omega_astro=None,
    Omega_fund=None,
    Omega_nu=None,
    Omega_q=None,
):
    """E(z)^2 com extensão ΛCDM++ (soma de componentes opcionais)."""
    z = np.asarray(z, dtype=float)
    total = Om * (1 + z) ** 3 + Or * (1 + z) ** 4 + Ol
    optional_components = (Omega_f, Omega_astro, Omega_fund, Omega_nu, Omega_q)
    for component in optional_components:
        if component is None:
            continue
        total = total + np.asarray(component(z), dtype=float)
    return total

def E_LCDM(z, Om=0.3, Or=0.0, Ol=0.7):
    z = np.asarray(z, dtype=float)
    return np.sqrt(Om*(1+z)**3 + Or*(1+z)**4 + Ol)

def H_of_z(
    z,
    H0=70.0,
    Om=0.3,
    Or=0.0,
    Ol=0.7,
    Omega_f=None,
    Omega_astro=None,
    Omega_fund=None,
    Omega_nu=None,
    Omega_q=None,
):
    """H(z)=H0*sqrt(E2_total), com extensões opcionais ΛCDM++."""
    return float(H0) * np.sqrt(
        E2_total(
            z,
            Om=Om,
            Or=Or,
            Ol=Ol,
            Omega_f=Omega_f,
            Omega_astro=Omega_astro,
            Omega_fund=Omega_fund,
            Omega_nu=Omega_nu,
            Omega_q=Omega_q,
        )
    )

def Omega_m_z(
    z,
    Om=0.3,
    Or=0.0,
    Ol=0.7,
    Omega_f=None,
    Omega_astro=None,
    Omega_fund=None,
    Omega_nu=None,
    Omega_q=None,
):
    z = np.asarray(z, dtype=float)
    Ez2 = E2_total(
        z,
        Om=Om,
        Or=Or,
        Ol=Ol,
        Omega_f=Omega_f,
        Omega_astro=Omega_astro,
        Omega_fund=Omega_fund,
        Omega_nu=Omega_nu,
        Omega_q=Omega_q,
    )
    return (Om*(1+z)**3) / Ez2
