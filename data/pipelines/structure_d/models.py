from .cosmo import H_of_z
from .growth import f_sigma8_proxy
from .feedback_agn import Omega_f_from_feedback
import numpy as np

_C_KM_S = 299792.458

def model_LCDM_Hz(z, params):
    return H_of_z(z, H0=params['H0'], Om=params['Om'], Or=params.get('Or',0.0), Ol=params['Ol'], Omega_f=None)

def model_RLL_like_Hz(z, params):
    Omega_f = lambda zz: Omega_f_from_feedback(zz, beta=params.get('beta',0.0),
                                               z_peak=params.get('z_peak',2.0),
                                               width=params.get('width',1.0))
    return H_of_z(z, H0=params['H0'], Om=params['Om'], Or=params.get('Or',0.0), Ol=params['Ol'], Omega_f=Omega_f)

def model_LCDM_fs8(z, params):
    return f_sigma8_proxy(z, sigma8_0=params.get('sigma8',0.8),
                          gamma=params.get('gamma',0.55),
                          Om=params['Om'], Or=params.get('Or',0.0), Ol=params['Ol'],
                          use_feedback=False)

def model_RLL_like_fs8(z, params):
    return f_sigma8_proxy(z, sigma8_0=params.get('sigma8',0.8),
                          gamma=params.get('gamma',0.55),
                          Om=params['Om'], Or=params.get('Or',0.0), Ol=params['Ol'],
                          use_feedback=True,
                          alpha=params.get('alpha',0.05),
                          z_peak=params.get('z_peak',2.0),
                          width=params.get('width',1.0))


def _omega_f_feedback(params):
    return lambda zz: Omega_f_from_feedback(
        zz,
        beta=params.get('beta', 0.0),
        z_peak=params.get('z_peak', 2.0),
        width=params.get('width', 1.0),
    )


def _hubble(z, params, use_feedback=False):
    return H_of_z(
        z,
        H0=params['H0'],
        Om=params['Om'],
        Or=params.get('Or', 0.0),
        Ol=params['Ol'],
        Omega_f=_omega_f_feedback(params) if use_feedback else None,
    )


def _comoving_distance_mpc(z, params, use_feedback=False):
    z_arr = np.asarray(z, dtype=float)
    if z_arr.ndim != 1:
        raise ValueError('z must be 1D')
    if np.any(z_arr < 0):
        raise ValueError('z must be non-negative')

    order = np.argsort(z_arr)
    z_sorted = z_arr[order]
    inv_h = _C_KM_S / _hubble(z_sorted, params, use_feedback=use_feedback)

    dc = np.zeros_like(z_sorted)
    if len(z_sorted) > 1:
        dz = np.diff(z_sorted)
        dc[1:] = np.cumsum(0.5 * (inv_h[1:] + inv_h[:-1]) * dz)

    dc_out = np.empty_like(dc)
    dc_out[order] = dc
    return dc_out


def _distance_modulus(z, params, use_feedback=False):
    z_arr = np.asarray(z, dtype=float)
    dl_mpc = (1.0 + z_arr) * _comoving_distance_mpc(z_arr, params, use_feedback=use_feedback)
    dl_mpc = np.clip(dl_mpc, 1e-12, None)
    return 5.0 * np.log10(dl_mpc) + 25.0 + params.get('M_offset', 0.0)


def _dv_over_rs(z, params, use_feedback=False):
    z_arr = np.asarray(z, dtype=float)
    hz = _hubble(z_arr, params, use_feedback=use_feedback)
    dm = _comoving_distance_mpc(z_arr, params, use_feedback=use_feedback)
    dv = np.cbrt((_C_KM_S * z_arr / hz) * (dm ** 2))
    rs_drag = params.get('rs_drag', 147.78)
    return dv / rs_drag


def _lens_distance_ratio(z_source, params, use_feedback=False):
    z_source_arr = np.asarray(z_source, dtype=float)
    zl = np.asarray(params.get('z_lens', 0.5), dtype=float)
    if zl.ndim == 0:
        zl = np.full_like(z_source_arr, float(zl))
    if zl.shape != z_source_arr.shape:
        raise ValueError('z_lens must be scalar or have same shape as z')
    if np.any(zl >= z_source_arr):
        raise ValueError('z_source must be larger than z_lens for lensing observable')

    dc_source = _comoving_distance_mpc(z_source_arr, params, use_feedback=use_feedback)
    dc_lens = _comoving_distance_mpc(zl, params, use_feedback=use_feedback)
    dls = (dc_source - dc_lens) / (1.0 + z_source_arr)
    ds = dc_source / (1.0 + z_source_arr)
    return dls / ds


def model_LCDM_SNe(z, params):
    return _distance_modulus(z, params, use_feedback=False)


def model_RLL_like_SNe(z, params):
    return _distance_modulus(z, params, use_feedback=True)


def model_LCDM_BAO(z, params):
    return _dv_over_rs(z, params, use_feedback=False)


def model_RLL_like_BAO(z, params):
    return _dv_over_rs(z, params, use_feedback=True)


def model_LCDM_lenses(z, params):
    return _lens_distance_ratio(z, params, use_feedback=False)


def model_RLL_like_lenses(z, params):
    return _lens_distance_ratio(z, params, use_feedback=True)
