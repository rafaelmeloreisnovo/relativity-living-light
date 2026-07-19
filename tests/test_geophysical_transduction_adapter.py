from rll.geophysical_transduction_adapter import (
    classify_rll_use,
    validate_external_result,
)

PIN = "97f0b96ade391f746125144ce4cc936d76dd2ff7"


def token_vazio_payload():
    return {
        "producer_repo": "rafaelmeloreisnovo/Fisica",
        "producer_commit": PIN,
        "claim_allowed": False,
        "local_geophysics_is_cosmological_evidence": False,
        "mechanisms": {"piezoelectric_quartz": {"decision": "TOKEN_VAZIO"}},
        "winner": "TOKEN_VAZIO",
    }


def test_token_vazio_artifact_is_valid_context_only():
    payload = token_vazio_payload()
    assert validate_external_result(payload, expected_commit=PIN) == []
    assert classify_rll_use(payload) == "CONTEXT_ONLY"


def test_wrong_producer_is_blocked():
    payload = token_vazio_payload()
    payload["producer_repo"] = "other/repo"
    assert classify_rll_use(payload) == "BLOCKED"


def test_local_signal_cannot_be_cosmological_evidence():
    payload = token_vazio_payload()
    payload["local_geophysics_is_cosmological_evidence"] = True
    assert any("cosmological evidence" in error for error in validate_external_result(payload))


def test_nonempty_winner_requires_evidence_chain():
    payload = token_vazio_payload()
    payload["winner"] = "piezoelectric_quartz"
    errors = validate_external_result(payload)
    assert any("preregistration_id" in error for error in errors)
    assert any("raw_data_hashes" in error for error in errors)


def test_residual_test_ready_requires_standard_rejection_and_registered_model():
    payload = token_vazio_payload()
    payload.update({
        "winner": "piezoelectric_quartz",
        "preregistration_id": "PRE-001",
        "uncertainty_model": "covariance.json",
        "baseline_results": "baseline.json",
        "falsifier_results": "falsifiers.json",
        "raw_data_hashes": ["a" * 64],
    })
    assert classify_rll_use(payload) == "CONTEXT_ONLY"
    payload["standard_mechanisms_rejected"] = True
    payload["registered_rll_residual_model"] = "RLL-B10-RES-001"
    assert classify_rll_use(payload) == "RESIDUAL_TEST_READY"
