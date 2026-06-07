from __future__ import annotations

from data.pipelines.structure_d.synthetic_real_boundary import (
    CLAIM_BOUNDARY,
    INTERPRETATION_LABELS,
    classify_dataset_type,
    enforce_claim_boundary,
    interpret_model_comparison,
)


def test_synthetic_dataset_blocks_claim() -> None:
    dataset_type = classify_dataset_type({"path": "data/synthetic/example.csv", "synthetic": True})
    policy = enforce_claim_boundary(dataset_type, {"delta_aic_rll_minus_lcdm": -99, "delta_bic_rll_minus_lcdm": -99})
    assert dataset_type == "synthetic_sanity_check"
    assert policy["claim_allowed"] is False
    assert policy["claim_boundary"] == CLAIM_BOUNDARY


def test_regression_fixture_is_not_real_observational() -> None:
    assert classify_dataset_type({"path": "tests/fixtures/mock_real.csv", "regression_fixture": True}) == "synthetic_regression_test"


def test_mixed_real_and_synthetic_is_forbidden() -> None:
    assert classify_dataset_type({"paths": ["data/real/Hz.csv", "data/synthetic/mock.csv"]}) == "mixed_forbidden"


def test_unknown_dataset_is_forbidden() -> None:
    assert classify_dataset_type({"path": "data/unlabeled/file.csv"}) == "unknown_forbidden"


def test_real_dataset_still_requires_thresholds() -> None:
    policy = enforce_claim_boundary(
        "real_observational",
        {"delta_chi2_rll_minus_lcdm": 1.0, "delta_aic_rll_minus_lcdm": 2.0, "delta_bic_rll_minus_lcdm": 3.0},
    )
    assert policy["claim_allowed"] is False


def test_interpretation_labels_are_allowed_and_deltas_are_rll_minus_lcdm() -> None:
    delta = {"delta_chi2_rll_minus_lcdm": -7.0, "delta_aic_rll_minus_lcdm": -6.0, "delta_bic_rll_minus_lcdm": -6.0}
    interpreted = interpret_model_comparison(delta, "real_observational")
    assert interpreted["interpretation_label"] == "rll_preferred_strong"
    assert interpreted["interpretation_label"] in INTERPRETATION_LABELS
    assert enforce_claim_boundary("real_observational", delta)["claim_allowed"] is True


def test_non_real_interpretation_is_blocked_even_with_good_metrics() -> None:
    interpreted = interpret_model_comparison(
        {"delta_chi2_rll_minus_lcdm": -7.0, "delta_aic_rll_minus_lcdm": -6.0, "delta_bic_rll_minus_lcdm": -6.0},
        "synthetic_regression_test",
    )
    assert interpreted["interpretation_label"] == "blocked_non_real_dataset"
