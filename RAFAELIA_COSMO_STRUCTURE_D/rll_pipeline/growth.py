import numpy as np
from .cosmo import Omega_m_z
from .feedback_agn import suppression_factor

def f_sigma8_proxy(z, sigma8_0=0.8, gamma=0.55, Om=0.3, Or=0.0, Ol=0.7,
                   use_feedback=False, alpha=0.05, z_peak=2.0, width=1.0):
    """Proxy rápido: f(z)≈Ωm(z)^γ, σ8_eff(z)=σ8_0*S(z)"""
    z = np.asarray(z, dtype=float)
    fz = Omega_m_z(z, Om=Om, Or=Or, Ol=Ol)**gamma
    s8 = np.full_like(z, float(sigma8_0))
    if use_feedback:
        s8 = s8 * suppression_factor(z, alpha=alpha, z_peak=z_peak, width=width)
    return fz * s8
