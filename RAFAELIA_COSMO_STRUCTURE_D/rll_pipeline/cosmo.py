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
