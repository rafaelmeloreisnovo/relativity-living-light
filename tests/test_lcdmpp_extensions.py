import numpy as np

from data.pipelines.structure_d.cosmo import (
    H_of_z,
    Omega_m_z,
    omega_astro,
    omega_fundamental,
    omega_neutrino,
    omega_quantum,
)
from data.pipelines.structure_d.likelihood import is_physically_stable, log_prior


def test_component_terms_are_finite_on_physical_grid():
    z = np.linspace(0.0, 5.0, 20)
    assert np.all(np.isfinite(omega_astro(z, A=0.01, n=1.2, z_c=2.0)))
    assert np.all(np.isfinite(omega_fundamental(z, Omega_e=0.02, m=2.0, beta_topo=1e-4)))
    assert np.all(np.isfinite(omega_neutrino(z, Omega_nu=0.001)))
    assert np.all(np.isfinite(omega_quantum(z, Omega_q0=1e-6, q_power=0.5)))


def test_hz_extension_reduces_to_lcdm_when_terms_off():
    z = np.array([0.0, 0.5, 1.0, 2.0])
    base = H_of_z(z, H0=70.0, Om=0.3, Or=0.0, Ol=0.7)
    ext = H_of_z(
        z,
        H0=70.0,
        Om=0.3,
        Or=0.0,
        Ol=0.7,
        Omega_astro=lambda zz: omega_astro(zz, A=0.0, n=0.0, z_c=1.0),
        Omega_fund=lambda zz: omega_fundamental(zz, Omega_e=0.0, m=0.0, beta_topo=0.0),
        Omega_nu=lambda zz: omega_neutrino(zz, Omega_nu=0.0),
        Omega_q=lambda zz: omega_quantum(zz, Omega_q0=0.0, q_power=0.0),
    )
    np.testing.assert_allclose(base, ext, rtol=1e-12, atol=1e-12)


def test_omega_m_z_accepts_extended_components():
    z = np.array([0.0, 1.0])
    out = Omega_m_z(
        z,
        Om=0.3,
        Or=0.0,
        Ol=0.7,
        Omega_fund=lambda zz: omega_fundamental(zz, Omega_e=0.01, m=1.0, beta_topo=0.001),
        Omega_nu=lambda zz: omega_neutrino(zz, Omega_nu=0.001),
    )
    assert np.all(np.isfinite(out))
    assert np.all(out > 0.0)


def test_likelihood_stability_rejects_negative_lcdmpp_e2():
    params = {
        "H0": 70.0,
        "Om": 0.3,
        "Or": 0.0,
        "Ol": 0.7,
        "Omega_e": -2.0,
        "m_ede": 0.0,
    }

    assert not is_physically_stable(params)
    assert log_prior(params) == -np.inf


def test_likelihood_stability_accepts_positive_lcdmpp_e2_grid():
    params = {
        "H0": 70.0,
        "Om": 0.3,
        "Or": 0.0,
        "Ol": 0.7,
        "Omega_e": 0.02,
        "m_ede": 1.0,
        "Omega_nu": 0.001,
    }

    assert is_physically_stable(
        params, data={"stability_z_grid": np.linspace(0.0, 3.0, 16)}
    )
