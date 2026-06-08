from __future__ import annotations

import json
from pathlib import Path

from data.pipelines.structure_d.synthetic_real_boundary import (
    CLAIM_BOUNDARY,
    INTERPRETATION_LABELS,
    classify_dataset_type,
    enforce_claim_boundary,
    enforce_real_validation_input_boundary,
    find_unapproved_synthetic_paths,
    interpret_model_comparison,
    load_legacy_synthetic_manifest,
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


def test_legacy_synthetic_manifest_lists_known_artifacts() -> None:
    manifest = load_legacy_synthetic_manifest()
    entries = {entry["original_path"]: entry for entry in manifest["entries"]}
    known_paths = {
        "data/posterior_unified_synth.csv",
        "data/inputs/structure_d/mock_data_contract.json",
        "results/dha/mock_catalog.csv",
        "figs/paper/mock_SN_fit.png",
        "data/rll_latentes/examples/valid_minimal.yml",
    }
    assert known_paths <= set(entries)
    for original_path in known_paths:
        entry = entries[original_path]
        assert entry["scientific_use_allowed"] is False
        assert entry["dataset_type"] in {"synthetic_sanity_check", "synthetic_regression_test"}
        assert entry["sha256"]


def test_cataloged_legacy_artifacts_do_not_trigger_new_boundary_violation() -> None:
    legacy_paths = [entry["original_path"] for entry in load_legacy_synthetic_manifest()["entries"]]
    assert find_unapproved_synthetic_paths(legacy_paths) == []


def test_new_synthetic_artifact_outside_boundary_is_reported() -> None:
    violations = find_unapproved_synthetic_paths(
        [
            "data/real/cosmology/fsigma8_growth_real.csv",
            "data/inputs/new_mock_catalog.csv",
            "results/real/demo_metric.json",
            "data/synthetic/approved_mock.csv",
            "tests/fixtures/approved_fixture.json",
        ]
    )
    assert violations == ["data/inputs/new_mock_catalog.csv", "results/real/demo_metric.json"]


def test_real_validation_rejects_synthetic_paths_unless_test_fixture() -> None:
    blocked = enforce_real_validation_input_boundary(
        {"dataset_type": "real_observational", "paths": ["data/real/cosmology/pantheon.csv", "results/dha/mock_catalog.csv"]}
    )
    assert blocked["real_validation_input_allowed"] is False
    assert blocked["dataset_type"] == "real_observational"
    assert blocked["violating_paths"] == ["results/dha/mock_catalog.csv"]

    fixture = enforce_real_validation_input_boundary(
        {"paths": ["tests/fixtures/mock_real.csv"], "regression_fixture": True}
    )
    assert fixture["real_validation_input_allowed"] is False
    assert fixture["dataset_type"] == "synthetic_regression_test"


def test_claim_allowed_false_for_non_real_and_incomplete_real_data() -> None:
    non_real_types = ["synthetic_sanity_check", "synthetic_regression_test", "mixed_forbidden", "unknown_forbidden"]
    for dataset_type in non_real_types:
        assert enforce_claim_boundary(dataset_type, {"delta_aic_rll_minus_lcdm": -99, "delta_bic_rll_minus_lcdm": -99})[
            "claim_allowed"
        ] is False

    incomplete_real = enforce_claim_boundary("real_observational", {"delta_aic_rll_minus_lcdm": None})
    assert incomplete_real["claim_allowed"] is False


def test_current_real_artifacts_keep_claim_allowed_false() -> None:
    real_artifact_roots = [Path("results/real"), Path("results/structure_d")]
    checked = []
    for root in real_artifact_roots:
        if not root.exists():
            continue
        for path in root.rglob("*.json"):
            data = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                continue
            if data.get("dataset_type") == "real_observational" or "claim_allowed" in data:
                checked.append(path.as_posix())
                assert data.get("claim_allowed") is False
                gate = data.get("claim_gate")
                if isinstance(gate, dict) and "claim_allowed" in gate:
                    assert gate["claim_allowed"] is False
    assert checked
