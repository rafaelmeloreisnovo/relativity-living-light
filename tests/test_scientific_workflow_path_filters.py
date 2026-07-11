from __future__ import annotations

from pathlib import Path, PurePosixPath

import pytest
import yaml

WORKFLOW_REQUIREMENTS = {
    ".github/workflows/bayes_analysis.yml": {
        "required_paths": {
            ".github/workflows/bayes_analysis.yml",
            "src/**",
            "data/**",
            "validation/**",
            "requirements*.txt",
            "pyproject.toml",
        },
        "positive_example": "src/run_full_analysis.py",
    },
    ".github/workflows/dha-fisher-ci.yml": {
        "required_paths": {
            ".github/workflows/dha-fisher-ci.yml",
            "src/**",
            "scripts/run_ln1pz_extractor.py",
            "scripts/run_desi_dha_pipeline.py",
            "scripts/export_dha_forecast.py",
            "tests/test_dha_fisher.py",
            "tests/test_ln1pz_extractor.py",
            "tests/test_desi_dha_extractor.py",
            "pyproject.toml",
        },
        "positive_example": "scripts/run_desi_dha_pipeline.py",
    },
    ".github/workflows/RLL_SCIENTIFIC.yml": {
        "required_paths": {
            ".github/workflows/RLL_SCIENTIFIC.yml",
            "validation/**",
            "src/**",
            "data/**",
            "requirements*.txt",
            "pyproject.toml",
        },
        "positive_example": "validation/run_rll.py",
    },
}

NON_SCIENCE_CHANGE_EXAMPLES = (
    "docs/README.md",
    "schemas/contract/example.schema.json",
)


def _workflow(path: str) -> dict:
    return yaml.load(Path(path).read_text(encoding="utf-8"), Loader=yaml.BaseLoader)


def _pull_request_paths(path: str) -> list[str]:
    workflow = _workflow(path)
    pull_request = workflow["on"]["pull_request"]
    assert isinstance(pull_request, dict), f"{path} must define pull_request settings"
    paths = pull_request.get("paths")
    assert isinstance(paths, list) and paths, f"{path} must define pull_request.paths"
    return paths


def _matches_any(changed_path: str, patterns: list[str]) -> bool:
    return any(PurePosixPath(changed_path).match(pattern) for pattern in patterns)


@pytest.mark.parametrize("workflow_path", WORKFLOW_REQUIREMENTS)
def test_scientific_workflows_define_required_pull_request_paths(workflow_path: str):
    patterns = set(_pull_request_paths(workflow_path))
    required = WORKFLOW_REQUIREMENTS[workflow_path]["required_paths"]
    assert required.issubset(patterns)


@pytest.mark.parametrize("workflow_path", WORKFLOW_REQUIREMENTS)
def test_scientific_workflows_ignore_docs_and_schema_only_changes(workflow_path: str):
    patterns = _pull_request_paths(workflow_path)
    for changed_path in NON_SCIENCE_CHANGE_EXAMPLES:
        assert not _matches_any(changed_path, patterns)


@pytest.mark.parametrize("workflow_path", WORKFLOW_REQUIREMENTS)
def test_scientific_workflows_still_trigger_on_representative_science_changes(workflow_path: str):
    patterns = _pull_request_paths(workflow_path)
    changed_path = WORKFLOW_REQUIREMENTS[workflow_path]["positive_example"]
    assert _matches_any(changed_path, patterns)
