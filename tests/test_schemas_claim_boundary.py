from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "tools" / "validate_schemas_claim_boundary.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_schemas_claim_boundary", VALIDATOR)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_schema_claim_boundary_validator_passes() -> None:
    module = load_validator()
    assert module.main() == 0


def test_schema_readme_declares_parse_success_is_not_validation() -> None:
    readme = (ROOT / "schemas" / "README.md").read_text(encoding="utf-8")
    assert "schema_parse_success != scientific_validation" in readme
    assert "claim_allowed=false" in readme
