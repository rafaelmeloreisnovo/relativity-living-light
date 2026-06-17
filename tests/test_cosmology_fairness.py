import json
import math
from pathlib import Path

import numpy as np
import pytest

from rll.cosmology_fairness import (
    aicc,
    bao_distance_ratios,
    comoving_distance_mpc,
    covariance_readiness,
    distance_modulus,
    e2_cpl,
    e2_lcdm,
    e2_wcdm,
    fsigma8_linear,
    growth_backend_benchmark_status,
    linear_growth_dplus,
    load_parameter_origin_registry,
    rd_drag_power_law,
    s8_parameter,
    transverse_comoving_distance_mpc,
    w_eff_rll_density,
)


def test_lcdm_wcdm_cpl_reduce_to_same_background_for_w_minus_one() -> None:
    z = np.array([0.0, 0.5, 1.0, 2.0])
    lcdm = e2_lcdm(z, om=0.3, ok=0.0, orad=0.0)
    wcdm = e2_wcdm(z, om=0.3, w=-1.0, ok=0.0, orad=0.0)
    cpl = e2_cpl(z, om=0.3, w0=-1.0, wa=0.0, ok=0.0, orad=0.0)

    assert np.allclose(wcdm, lcdm)
    assert np.allclose(cpl, lcdm)


def test_curved_transverse_distance_has_flat_limit_and_curvature_effect() -> None:
    dc = comoving_distance_mpc(0.7, 70.0, e2_lcdm, 0.3, 0.0, 0.0, None)
    dm_flat = transverse_comoving_distance_mpc(0.7, 70.0, 0.0, e2_lcdm, 0.3, 0.0, 0.0, None)
    dm_open = transverse_comoving_distance_mpc(0.7, 70.0, 0.05, e2_lcdm, 0.3, 0.0, 0.0, None)

    assert dm_flat == pytest.approx(dc)
    assert dm_open > dm_flat


def test_distance_modulus_and_bao_ratios_are_finite_and_ordered() -> None:
    rd = rd_drag_power_law(67.7, 0.31, 0.02236)
    mu = distance_modulus(0.2, 67.7, 0.0, e2_lcdm, 0.31, 0.0, 0.0, None)
    ratios = bao_distance_ratios(0.51, 67.7, 0.0, rd, e2_lcdm, 0.31, 0.0, 0.0, None)

    assert math.isfinite(mu)
    assert ratios.dh_over_rd > 0.0
    assert ratios.dm_over_rd > 0.0
    assert ratios.dv_over_rd > 0.0


def test_aicc_matches_formula_and_rejects_undefined_case() -> None:
    chi2 = 20.0
    k = 3
    n = 30
    assert aicc(chi2, k, n) == pytest.approx(chi2 + 2 * k + 2 * k * (k + 1) / (n - k - 1))
    with pytest.raises(ValueError, match="AICc undefined"):
        aicc(chi2, k, 4)


def test_rll_effective_w_and_growth_diagnostics_are_physical_sanity_checks() -> None:
    z = np.array([0.0, 1.0, 8.0])
    w_eff = w_eff_rll_density(z, zt=1.0, wt=0.3)
    d0 = linear_growth_dplus(0.0, e2_lcdm, 0.3, 0.3, 0.0, 0.0, None)
    d1 = linear_growth_dplus(1.0, e2_lcdm, 0.3, 0.3, 0.0, 0.0, None)
    fs8 = fsigma8_linear(0.5, 0.8, e2_lcdm, 0.3, 0.3, 0.0, 0.0, None)
    s8 = s8_parameter(0.8, 0.3)

    assert np.all(np.isfinite(w_eff))
    assert w_eff[0] < 0.0
    assert w_eff[-1] == pytest.approx(0.0, abs=1.0e-6)
    assert np.all(w_eff < 1.0)
    assert d0 == pytest.approx(1.0)
    assert 0.0 < d1 < d0
    assert fs8 > 0.0
    assert s8 == pytest.approx(0.8)


def test_covariance_readiness_gates_partial_covariance_claims() -> None:
    cov = np.array([[4.0, 0.2], [0.2, 9.0]])
    partial = covariance_readiness(cov, mode="block_summary")
    full = covariance_readiness(cov, mode="official_full")

    assert partial.ready is True
    assert partial.claim_allowed is False
    assert full.ready is True
    assert full.claim_allowed is True


def test_growth_backend_benchmark_status_is_claim_gate() -> None:
    status = growth_backend_benchmark_status(require_external=True)

    assert set(status) == {"status", "available_backends", "checked_backends", "claim_allowed", "reason"}
    assert status["claim_allowed"] is (status["status"] == "available")


def test_parameter_origin_registry_contract() -> None:
    registry = json.loads(Path("data/inputs/cosmology_joint/parameter_origin_registry.json").read_text(encoding="utf-8"))
    normalized = load_parameter_origin_registry(registry)
    names = {row["name"] for row in normalized["parameters"]}

    assert "H0" in names
    assert "Os0" in names
    assert "w0" in names
    assert "wa" in names
