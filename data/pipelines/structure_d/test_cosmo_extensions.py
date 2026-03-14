import unittest

import numpy as np

from data.pipelines.structure_d.cosmo import (
    H_of_z_lcdm_pp,
    Omega_astro,
    Omega_ede,
    Omega_topological,
)


class CosmoExtensionsTest(unittest.TestCase):
    def test_omega_astro_profile(self):
        z = np.array([0.0, 1.0, 2.0])
        got = Omega_astro(z, A=0.1, n=2.0, z_c=1.5)
        expected = 0.1 * (1.0 + z) ** 2.0 * np.exp(-z / 1.5)
        self.assertTrue(np.allclose(got, expected))

    def test_omega_ede_profile(self):
        z = np.array([0.0, 1.0, 3.0])
        got = Omega_ede(z, Omega_e=0.02, m=1.0)
        expected = 0.02 * (1.0 + z)
        self.assertTrue(np.allclose(got, expected))

    def test_topological_term(self):
        z = np.array([0.0, 0.5, 1.0])
        got = Omega_topological(z, beta_topo=0.03)
        expected = 0.03 * (1.0 + z) ** 2
        self.assertTrue(np.allclose(got, expected))

    def test_h_of_z_lcdm_pp_reduces_to_lcdm_when_new_terms_are_zero(self):
        z = np.array([0.0, 0.5, 1.0])
        h_base = H_of_z_lcdm_pp(
            z,
            H0=70.0,
            Om=0.3,
            Or=0.0,
            Ol=0.7,
            Omega_nu0=0.0,
            astro_args={"A": 0.0, "n": 0.0, "z_c": 1.0},
            fund_args={"Omega_e": 0.0, "m": 0.0, "beta_topo": 0.0},
            q_args={"q0": 0.0, "p": 0.0},
        )
        expected = 70.0 * np.sqrt(0.3 * (1.0 + z) ** 3 + 0.7)
        self.assertTrue(np.allclose(h_base, expected))


if __name__ == "__main__":
    unittest.main()
