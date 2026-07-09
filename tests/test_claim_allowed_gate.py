from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "tools" / "validate_claim_allowed_gate.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_claim_allowed_gate", VALIDATOR)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_global_claim_allowed_gate_passes_current_repository() -> None:
    module = load_validator()
    assert module.main() == 0


def test_evidence_group_names_are_declared() -> None:
    module = load_validator()
    assert set(module.EVIDENCE_GROUPS) == {
        "source",
        "checksum",
        "metric",
        "baseline",
        "uncertainty",
        "execution",
        "boundary",
    }


def test_validator_scans_data_results_docs_yml_and_schemas() -> None:
    module = load_validator()
    scan_roots = {path.relative_to(ROOT).as_posix() for path in module.SCAN_ROOTS}
    assert scan_roots == {"data", "results", "docs/yml", "schemas"}
