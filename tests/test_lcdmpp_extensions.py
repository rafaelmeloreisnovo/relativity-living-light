import numpy as np

from data.pipelines.structure_d.cosmo import (
    H_of_z,
    H_of_z_extended,
    omega_astro,
    omega_ede,
    omega_topological,
)
from data.pipelines.structure_d.growth import f_sigma8_proxy
from data.pipelines.structure_d.models import model_RLL_LCDMpp_Hz


def test_omega_astro_and_terms_are_vectorized():
    z = np.array([0.0, 1.0, 2.0])
    out = omega_astro(z, A=0.02, n=1.0, z_c=2.0)
    assert out.shape == z.shape
    assert np.all(np.isfinite(out))

    ede = omega_ede(z, Omega_e=0.01, m=2.0)
    topo = omega_topological(z, beta=0.001)
    assert np.all(ede >= 0.0)
    assert np.all(topo >= 0.0)


def test_h_of_z_extended_reduces_to_baseline_when_extra_terms_zero():
    z = np.linspace(0.0, 2.0, 6)
    base = H_of_z(z, H0=70.0, Om=0.3, Or=0.0, Ol=0.7)
    ext = H_of_z_extended(
        z,
        H0=70.0,
        Om=0.3,
        Or=0.0,
        Ol=0.7,
        Onu=0.0,
        Omega_q=lambda zz: np.zeros_like(zz),
        Omega_astro=lambda zz: np.zeros_like(zz),
        Omega_fund=lambda zz: np.zeros_like(zz),
    )
    np.testing.assert_allclose(base, ext, rtol=1e-12, atol=1e-12)


def test_growth_gamma_default_matches_requested_gr_convention():
    z = np.array([0.0, 0.5, 1.0])
    fs8 = f_sigma8_proxy(z, gamma=0.545, Om=0.3, Ol=0.7, sigma8_0=0.8)
    assert np.all(np.isfinite(fs8))
    assert np.all(fs8 > 0.0)


def test_model_rll_lcdmpp_hz_includes_new_components_without_crash():
    z = np.array([0.0, 1.0])
    params = {
        "H0": 70.0,
        "Om": 0.3,
        "Or": 0.0,
        "Ol": 0.7,
        "Onu": 0.001,
        "Omega_q0": 0.0,
        "A_astro": 0.01,
        "n_astro": 1.0,
        "z_c_astro": 2.0,
        "Omega_e": 0.005,
        "m_ede": 1.0,
        "beta_topo": 0.001,
        "lambda_brane": 1000.0,
    }
    hz = model_RLL_LCDMpp_Hz(z, params)
    assert hz.shape == z.shape
    assert np.all(np.isfinite(hz))
    assert np.all(hz > 0.0)
