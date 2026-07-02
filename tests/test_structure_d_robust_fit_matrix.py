from __future__ import annotations

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
