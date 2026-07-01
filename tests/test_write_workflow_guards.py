from __future__ import annotations

from pathlib import Path

import yaml


def _workflow(path: str) -> dict:
    return yaml.load(Path(path).read_text(encoding="utf-8"), Loader=yaml.BaseLoader)


def _steps(path: str) -> list[dict]:
    jobs = _workflow(path)["jobs"]
    return [step for job in jobs.values() for step in job.get("steps", [])]


def test_repo_inventory_is_artifact_only_and_checksumed():
    workflow = _workflow(".github/workflows/repo-real-inventory.yml")
    assert workflow.get("permissions", {}).get("contents") == "read"

    workflow_text = Path(".github/workflows/repo-real-inventory.yml").read_text(encoding="utf-8")
    assert "git push" not in workflow_text
    assert "contents: write" not in workflow_text
    assert "commit_inventory" not in workflow_text

    steps = _steps(".github/workflows/repo-real-inventory.yml")
    checksum = next(step for step in steps if step.get("name") == "Build inventory checksums and commit policy note")
    upload = next(step for step in steps if step.get("name") == "Upload generated inventory artifact without committing")

    assert "sha256sum" in checksum["run"]
    assert "repo_inventory_checksums.sha256" in checksum["run"]
    assert "artifact-only" in checksum["run"]
    assert "repo-real-inventory" in upload["with"]["name"]


def test_validacao_real_commit_is_manual_opt_in_and_checksumed():
    workflow = _workflow(".github/workflows/validacao_real.yml")
    inputs = workflow["on"]["workflow_dispatch"]["inputs"]
    assert inputs["commit_results"]["default"] == "false"
    assert workflow.get("permissions", {}).get("contents") == "read"

    jobs = workflow["jobs"]
    assert jobs["commit-results"]["permissions"]["contents"] == "write"
    assert "inputs.commit_results" in jobs["commit-results"]["if"]

    steps = _steps(".github/workflows/validacao_real.yml")
    checksum = next(step for step in steps if step.get("name") == "Build artifact checksums")
    commit = next(step for step in steps if "Commit results back to repo" in step.get("name", ""))

    assert "sha256sum" in checksum["run"]
    assert "CHECKSUMS.sha256" in checksum["run"]
    assert "git push" in commit["run"]
