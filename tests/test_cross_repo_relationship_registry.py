from __future__ import annotations

import pytest

from tools import validate_cross_repo_relationship_registry as validator


def test_current_cross_repo_relationship_registry_is_valid() -> None:
    text = validator.REGISTRY.read_text(encoding="utf-8")
    validator.validate_text(text)


def test_unknown_state_is_rejected() -> None:
    with pytest.raises(ValueError, match="unknown state"):
        validator.validate_state_field("PRODUCTION_READY")


def test_promotion_language_is_rejected() -> None:
    row = {
        "ID": "X-001",
        "Relationship": "RLL already validated integration",
        "State": "HYPOTHESIS",
        "Safe reading": "candidate",
        "Blocked claim": "none",
        "Next verification": "Verify owning repository",
    }
    with pytest.raises(ValueError, match="forbidden promotion phrase"):
        validator.validate_rows([row])


def test_duplicate_relationship_id_is_rejected() -> None:
    row = {
        "ID": "X-001",
        "Relationship": "Candidate relation",
        "State": "HYPOTHESIS",
        "Safe reading": "candidate",
        "Blocked claim": "working integration without owning-repo evidence",
        "Next verification": "Verify owning repository",
    }
    with pytest.raises(ValueError, match="duplicate"):
        validator.validate_rows([row, dict(row)])
