import unittest

import numpy as np

from data.pipelines.structure_d.run_all_real import _f_log


class FLogStabilityTest(unittest.TestCase):
    def test_f_log_handles_limits_without_overflow_or_underflow(self):
        zt_limits = (0.1, 10.0)
        wt_limits = (0.1, 1.0)
        z_grid = np.array([-1e6, -1e3, -100.0, 0.0, 0.1, 1.0, 10.0, 100.0, 1e3, 1e6], dtype=float)

        with np.errstate(over="raise", under="raise", invalid="raise", divide="raise"):
            for zt in zt_limits:
                for wt in wt_limits:
                    vals = _f_log(z_grid, zt, wt)
                    self.assertTrue(np.all(np.isfinite(vals)))
                    self.assertTrue(np.all(vals >= 0.0))
                    self.assertTrue(np.all(vals <= 1.0))

    def test_f_log_is_continuous_around_transition_for_bound_values(self):
        dz = 1e-8
        for zt in (0.1, 10.0):
            for wt in (0.1, 1.0):
                left = float(_f_log(zt - dz, zt, wt))
                center = float(_f_log(zt, zt, wt))
                right = float(_f_log(zt + dz, zt, wt))

                self.assertAlmostEqual(center, 0.5, places=12)
                self.assertGreater(left, center)
                self.assertGreater(center, right)
                self.assertLess(abs(left - center), 1e-6)
                self.assertLess(abs(center - right), 1e-6)


if __name__ == "__main__":
    unittest.main()
