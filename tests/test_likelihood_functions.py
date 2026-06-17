import math

import numpy as np
import pytest

from data.pipelines.structure_d.likelihood import aic, aicc, bic, chi2, chi2_with_covariance


def test_chi2_matches_manual_sum() -> None:
    obs = np.array([10.0, 20.0, 30.0])
    mod = np.array([9.0, 19.0, 29.0])
    sigma = np.array([1.0, 2.0, 1.0])
    expected = ((1.0 / 1.0) ** 2) + ((1.0 / 2.0) ** 2) + ((1.0 / 1.0) ** 2)
    assert chi2(obs, mod, sigma) == pytest.approx(expected)


def test_chi2_with_covariance_matches_identity_case() -> None:
    obs = np.array([1.0, 2.0, 3.0])
    mod = np.array([1.2, 2.1, 2.9])
    cov = np.eye(3)
    expected = float(np.sum((obs - mod) ** 2))
    assert chi2_with_covariance(obs, mod, cov) == pytest.approx(expected)


def test_information_criteria_are_consistent() -> None:
    chi2_val = 12.5
    k = 4
    n = 30
    assert aic(chi2_val, k) == pytest.approx(20.5)
    assert aicc(chi2_val, k, n) == pytest.approx(20.5 + (2 * k * (k + 1)) / (n - k - 1))
    assert bic(chi2_val, k, n) == pytest.approx(chi2_val + k * math.log(n))

