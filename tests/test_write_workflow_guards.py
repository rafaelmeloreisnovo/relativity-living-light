from __future__ import annotations

from pathlib import Path

import yaml


def _workflow(path: str) -> dict:
    return yaml.load(Path(path).read_text(encoding="utf-8"), Loader=yaml.BaseLoader)


def _steps(path: str) -> list[dict]:
    jobs = _workflow(path)["jobs"]
    return [step for job in jobs.values() for step in job.get("steps", [])]


def test_repo_inventory_commit_is_manual_opt_in_and_checksumed():
    workflow = _workflow(".github/workflows/repo-real-inventory.yml")
    inputs = workflow["on"]["workflow_dispatch"]["inputs"]
    assert inputs["commit_inventory"]["default"] == "false"

    steps = _steps(".github/workflows/repo-real-inventory.yml")
    commit = next(step for step in steps if step.get("name") == "Commit generated real inventory")
    checksum = next(step for step in steps if step.get("name") == "Build inventory checksums")

    assert "inputs.commit_inventory" in commit["if"]
    assert "sha256sum" in checksum["run"]
    assert "repo_inventory_checksums.sha256" in checksum["run"]


def test_validacao_real_commit_is_manual_opt_in_and_checksumed():
    workflow = _workflow(".github/workflows/validacao_real.yml")
    inputs = workflow["on"]["workflow_dispatch"]["inputs"]
    assert inputs["commit_results"]["default"] == "false"

    steps = _steps(".github/workflows/validacao_real.yml")
    commit = next(step for step in steps if step.get("name") == "Commit results back to repo")
    checksum = next(step for step in steps if step.get("name") == "Build artifact checksums")

    assert "inputs.commit_results" in commit["if"]
    assert "sha256sum" in checksum["run"]
    assert "CHECKSUMS.sha256" in checksum["run"]
