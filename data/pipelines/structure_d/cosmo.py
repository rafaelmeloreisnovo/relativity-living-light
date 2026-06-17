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
    Ez2 = E2_total(z, Om=Om, Or=Or, Ol=Ol)
    return (Om * (1.0 + z) ** 3) / Ez2


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
