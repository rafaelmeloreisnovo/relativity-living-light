from __future__ import annotations

import pytest

from scripts import run_structure_d_joint_likelihood as runner


def test_validate_output_stem_accepts_filename_stem() -> None:
    assert runner.validate_output_stem("joint_real_likelihood_seed_1_maxiter_100") == "joint_real_likelihood_seed_1_maxiter_100"


def test_validate_output_stem_rejects_paths_and_extensions() -> None:
    for invalid in ["", " ", "../escape", "subdir/name", r"subdir\\name", ".", "..", "result.json", "result.csv"]:
        with pytest.raises(ValueError):
            runner.validate_output_stem(invalid)


def test_resolve_output_stem_uses_default_when_unset(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(runner.OUTPUT_STEM_ENV, raising=False)
    assert runner.resolve_output_stem() == runner.DEFAULT_OUTPUT_STEM


def test_resolve_output_stem_reads_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(runner.OUTPUT_STEM_ENV, "joint_real_likelihood_seed_7_maxiter_100")
    assert runner.resolve_output_stem() == "joint_real_likelihood_seed_7_maxiter_100"


def test_cli_output_stem_overrides_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(runner.OUTPUT_STEM_ENV, "joint_real_likelihood_seed_7_maxiter_100")
    assert runner.resolve_output_stem("joint_real_likelihood_seed_8_maxiter_100") == "joint_real_likelihood_seed_8_maxiter_100"
