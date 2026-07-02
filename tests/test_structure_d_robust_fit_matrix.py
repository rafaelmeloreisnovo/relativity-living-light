from __future__ import annotations

import json

import pytest

from scripts import run_structure_d_robust_fit_matrix as matrix


def test_build_output_stem_is_versioned_and_safe() -> None:
    assert matrix.build_output_stem(1, 100) == "joint_real_likelihood_seed_1_maxiter_100"


def test_build_plan_is_dry_run_metadata_only() -> None:
    plan = matrix.build_plan([1, 2], 100)
    assert [item["output_stem"] for item in plan] == [
        "joint_real_likelihood_seed_1_maxiter_100",
        "joint_real_likelihood_seed_2_maxiter_100",
    ]
    assert all("run_structure_d_joint_likelihood.py" in str(item["command"]) for item in plan)


def test_parse_seeds_rejects_empty_or_nonpositive() -> None:
    with pytest.raises(ValueError):
        matrix.parse_seeds("")
    with pytest.raises(ValueError):
        matrix.parse_seeds("0")


def test_prefix_reuses_stem_guard() -> None:
    with pytest.raises(ValueError):
        matrix.build_output_stem(1, 100, "../escape")


def test_validate_plan_rejects_duplicate_stems() -> None:
    item = {"seed": 1, "maxiter": 100, "output_stem": "joint_real_likelihood_seed_1_maxiter_100"}
    with pytest.raises(ValueError, match="unique"):
        matrix.validate_plan([item, dict(item)])


def test_validate_plan_rejects_canonical_smoke_stem() -> None:
    with pytest.raises(ValueError, match="canonical"):
        matrix.validate_plan([{"seed": 1, "maxiter": 100, "output_stem": matrix.CANONICAL_STEM}])


def test_watchdog_marks_dry_run_and_safe_stems() -> None:
    plan = matrix.build_plan([1, 2], 100)
    watchdog = matrix.build_watchdog(plan, "dry_run")
    assert watchdog["overall_status"] == "pass"
    assert watchdog["dry_run_default"] is True
    assert watchdog["unique_output_stems"] is True
    assert watchdog["canonical_stem_blocked"] is True
    assert watchdog["planned_runs"] == 2


def test_plan_output_uses_rollback_backup(tmp_path) -> None:
    output = tmp_path / "robust_fit_plan.json"
    output.write_text('{"old": true}\n', encoding="utf-8")

    assert matrix.main(["--seeds", "1", "--maxiter", "100", "--plan-output", str(output)]) == 0

    payload = json.loads(output.read_text(encoding="utf-8"))
    backup = output.with_suffix(output.suffix + ".bak")
    assert backup.exists()
    assert json.loads(backup.read_text(encoding="utf-8"))["old"] is True
    assert payload["mode"] == "dry_run"
    assert payload["failsafe"]["atomic_plan_output"] is True
    assert payload["watchdog"]["overall_status"] == "pass"
