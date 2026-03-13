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


def Omega_astro(z, A=0.0, n=0.0, z_c=1.0):
    """Componente astrofísico fenomenológico: A (1+z)^n exp(-z/z_c)."""
    z = np.asarray(z, dtype=float)
    if z_c <= 0.0:
        return np.full_like(z, np.nan, dtype=float)
    with np.errstate(over="ignore", invalid="ignore"):
        return A * (1.0 + z) ** n * np.exp(-z / z_c)


def Omega_ede(z, Omega_e=0.0, m=0.0):
    """Componente de energia escura precoce simples: Ωe (1+z)^m."""
    z = np.asarray(z, dtype=float)
    with np.errstate(over="ignore", invalid="ignore"):
        return Omega_e * (1.0 + z) ** m


def Omega_topological(z, beta_topo=0.0):
    """Termo topológico efetivo β/a² = β(1+z)²."""
    z = np.asarray(z, dtype=float)
    return beta_topo * (1.0 + z) ** 2


def Omega_quantum(z, q0=0.0, p=0.0):
    """Termo quântico efetivo genérico: q0 (1+z)^p."""
    z = np.asarray(z, dtype=float)
    with np.errstate(over="ignore", invalid="ignore"):
        return q0 * (1.0 + z) ** p


def H_of_z_lcdm_pp(
    z,
    H0=70.0,
    Om=0.3,
    Or=0.0,
    Ol=0.7,
    Omega_nu0=0.0,
    astro_args=None,
    fund_args=None,
    q_args=None,
):
    """Extensão formal ΛCDM++ com decomposição Ωf = Ωastro + Ωfund.

    Ωfund é construído por padrão como ΩEDE + Ωtopológico.
    """
    z = np.asarray(z, dtype=float)
    aargs = astro_args or {}
    fargs = fund_args or {}
    qv = q_args or {}

    omega_astro = Omega_astro(
        z,
        A=float(aargs.get("A", 0.0)),
        n=float(aargs.get("n", 0.0)),
        z_c=float(aargs.get("z_c", 1.0)),
    )
    omega_fund = Omega_ede(
        z,
        Omega_e=float(fargs.get("Omega_e", 0.0)),
        m=float(fargs.get("m", 0.0)),
    ) + Omega_topological(z, beta_topo=float(fargs.get("beta_topo", 0.0)))
    omega_q = Omega_quantum(
        z,
        q0=float(qv.get("q0", 0.0)),
        p=float(qv.get("p", 0.0)),
    )
    inside = (
        Om * (1.0 + z) ** 3
        + Or * (1.0 + z) ** 4
        + Ol
        + Omega_nu0 * (1.0 + z) ** 3
        + omega_astro
        + omega_fund
        + omega_q
    )
    return H0 * np.sqrt(inside)

def Omega_m_z(z, Om=0.3, Or=0.0, Ol=0.7):
    z = np.asarray(z, dtype=float)
    Ez2 = Om*(1+z)**3 + Or*(1+z)**4 + Ol
    return (Om*(1+z)**3) / Ez2
