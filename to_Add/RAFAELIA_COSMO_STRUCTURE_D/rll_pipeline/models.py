from .cosmo import H_of_z
from .growth import f_sigma8_proxy
from .feedback_agn import Omega_f_from_feedback

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
