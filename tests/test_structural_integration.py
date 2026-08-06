import json
import math
from pathlib import Path

import pytest

from rll.structural_integration import (
    EpistemicStatus,
    ExecutionDecision,
    TransitionParameters,
    alcock_paczynski_ratio,
    bulk_viscous_pressure,
    distance_duality_eta,
    evaluate_branch_readiness,
    frb_delay_residual,
    interaction_source,
    logistic_transition_z,
    stable_payload_hash,
    transition_density_factor_z,
    transition_density_fraction_z,
    transition_w_eff_z,
    validate_integration_registry,
    validate_source_registry,
)

ROOT = Path(__file__).resolve().parents[1]


def test_logistic_transition_is_bounded_and_centered():
    assert logistic_transition_z(1.0, 1.0, 0.2) == pytest.approx(0.5)
    assert 0.0 < logistic_transition_z(50.0, 1.0, 0.2) < 1e-10
    assert 0.999 < logistic_transition_z(0.0, 5.0, 0.2) <= 1.0


def test_transition_density_has_expected_limits():
    params = TransitionParameters(omega_s0=0.02, z_t=1.0, w_t=0.1)
    assert transition_density_fraction_z(0.0, params) == pytest.approx(0.02)
    z = 5.0
    assert transition_density_factor_z(z, 1.0, 0.1) == pytest.approx((1 + z) ** 3, rel=1e-8)


def test_effective_eos_is_finite():
    for z in (0.0, 0.5, 1.0, 2.0, 10.0):
        assert math.isfinite(transition_w_eff_z(z, 1.0, 0.3))


def test_dissipative_and_interaction_operators():
    assert bulk_viscous_pressure(2.0, 3.0, 0.5) == pytest.approx(-2.5)
    assert interaction_source(-0.1, 70.0, 0.3) == pytest.approx(-2.1)


def test_distance_operators():
    z = 1.0
    d_a = 1000.0
    d_l = (1 + z) ** 2 * d_a
    assert distance_duality_eta(d_l, d_a, z) == pytest.approx(1.0)
    assert alcock_paczynski_ratio(20.0, 10.0) == pytest.approx(2.0)


def test_frb_residual_does_not_assume_new_physics():
    assert frb_delay_residual(12.0, 2.0, 1.0, 5.0) == pytest.approx(2.0)


def test_hash_is_order_invariant():
    assert stable_payload_hash({"a": 1, "b": 2}) == stable_payload_hash({"b": 2, "a": 1})


def test_source_registry_is_claim_bounded():
    payload = json.loads((ROOT / "data/registries/rll_recent_primary_sources_2026.json").read_text())
    assert validate_source_registry(payload) == []
    assert payload["claim_allowed"] is False


def test_integration_registry_preserves_raw_data():
    payload = json.loads((ROOT / "data/registries/rll_operational_integration_registry.json").read_text())
    assert validate_integration_registry(payload) == []
    assert payload["raw_data_policy"] == "immutable"
    assert payload["claim_allowed"] is False


def test_branch_readiness_reports_missing_artifacts():
    branch = {
        "status": EpistemicStatus.HYPOTHESIS.value,
        "required_artifacts": ["a", "b"],
    }
    decision, missing = evaluate_branch_readiness(branch, ["a"])
    assert decision is ExecutionDecision.BLOCKED
    assert missing == ["b"]


def test_token_vazio_branch_stays_token_vazio():
    branch = {
        "status": EpistemicStatus.TOKEN_VAZIO.value,
        "required_artifacts": [],
    }
    decision, reasons = evaluate_branch_readiness(branch, [])
    assert decision is ExecutionDecision.TOKEN_VAZIO
    assert reasons


@pytest.mark.parametrize(
    "call",
    [
        lambda: logistic_transition_z(-1, 1, 1),
        lambda: logistic_transition_z(1, 1, 0),
        lambda: distance_duality_eta(0, 1, 1),
        lambda: alcock_paczynski_ratio(1, 0),
        lambda: frb_delay_residual(1, -1, 1, 1),
    ],
)
def test_invalid_inputs_fail_closed(call):
    with pytest.raises(ValueError):
        call()
