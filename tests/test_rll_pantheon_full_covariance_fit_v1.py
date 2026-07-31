from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
PRODUCT = ROOT / "products/rll-evidence-runner"
sys.path.insert(0, str(PRODUCT / "src"))

from rll_evidence.pantheon_fit import LCDM, RLL, build_result, distance_modulus, e2, fit_model, prepare_data, profiled_likelihood


class PantheonFullCovarianceFitV1Tests(unittest.TestCase):
    def synthetic_data(self):
        z_hd = np.array([0.005, 0.007, 0.02, 0.04, 0.08, 0.15, 0.3, 0.5, 0.8, 1.1])
        z_hel = z_hd + 0.0002
        calibrator = np.array([True, True] + [False] * 8)
        ceph = np.array([31.0, 32.0] + [-9.0] * 8)
        covariance = np.diag(np.full(10, 0.03**2))
        empty = prepare_data(z_hd, z_hel, np.zeros(10), ceph, calibrator, covariance, integration_points=512)
        mu = distance_modulus(empty, LCDM, [70.0, 0.3])
        return prepare_data(z_hd, z_hel, mu - 19.25, ceph, calibrator, covariance, integration_points=512)

    def test_flat_closure_at_z_zero(self) -> None:
        self.assertAlmostEqual(float(e2(LCDM, np.array([0.0]), [70.0, 0.3])[0]), 1.0, places=12)
        self.assertAlmostEqual(float(e2(RLL, np.array([0.0]), [70.0, 0.3, 0.05, 1.0, 0.3])[0]), 1.0, places=12)

    def test_profiled_absolute_magnitude(self) -> None:
        data = self.synthetic_data()
        chi2, m_b_hat, _ = profiled_likelihood(data, LCDM, [70.0, 0.3])
        self.assertLess(chi2, 1.0e-8)
        self.assertAlmostEqual(m_b_hat, -19.25, places=7)

    def test_multiseed_fit_is_deterministic(self) -> None:
        data = self.synthetic_data()
        first = fit_model(data, LCDM, [11, 23], maxiter=80, ftol=1.0e-12)
        second = fit_model(data, LCDM, [11, 23], maxiter=80, ftol=1.0e-12)
        self.assertAlmostEqual(first["best"]["chi2"], second["best"]["chi2"], places=10)
        self.assertAlmostEqual(first["best"]["H0"], 70.0, places=2)
        self.assertAlmostEqual(first["best"]["Omega_m"], 0.3, places=2)

    def test_build_result_from_files(self) -> None:
        data = self.synthetic_data()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            catalog = root / "Pantheon.dat"
            covariance = root / "Pantheon.cov"
            output = root / "result.json"
            with catalog.open("w", encoding="utf-8") as handle:
                handle.write("zHD zHEL m_b_corr CEPH_DIST IS_CALIBRATOR\n")
                for row in zip(data.z_hd, data.z_hel, data.m_b_corr, data.ceph_dist, data.is_calibrator):
                    handle.write("{} {} {} {} {}\n".format(row[0], row[1], row[2], row[3], int(row[4])))
            with covariance.open("w", encoding="utf-8") as handle:
                handle.write(str(data.n) + "\n")
                for value in data.covariance.ravel():
                    handle.write("{:.17g}\n".format(value))
            payload = build_result(catalog, covariance, output, seeds=[11, 23], maxiter=60, integration_points=512)
            self.assertFalse(payload["claim_allowed"])
            self.assertEqual(len(payload["rows"]), 2)
            disk = json.loads(output.read_text())
            self.assertEqual(disk["schema"], "rll_pantheon_full_covariance_fit_v1")
            self.assertIn("candidate_minus_baseline", disk["comparison"])


if __name__ == "__main__":
    unittest.main()
