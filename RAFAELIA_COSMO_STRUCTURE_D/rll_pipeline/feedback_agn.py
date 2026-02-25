import numpy as np

def gaussian_window(z, z_peak=2.0, width=1.0):
    z = np.asarray(z, dtype=float)
    return np.exp(-0.5*((z - z_peak)/width)**2)

def suppression_factor(z, alpha=0.05, z_peak=2.0, width=1.0):
    """Fenomenológico: S(z)=1 - alpha * window(z)."""
    w = gaussian_window(z, z_peak=z_peak, width=width)
    return np.clip(1.0 - alpha*w, 0.0, 1.0)

def Omega_f_from_feedback(z, beta=0.0, z_peak=2.0, width=1.0):
    """Termo aditivo em H(z). beta=0 -> LCDM."""
    z = np.asarray(z, dtype=float)
    return beta * gaussian_window(z, z_peak=z_peak, width=width)
