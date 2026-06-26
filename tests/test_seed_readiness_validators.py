from __future__ import annotations

import json

from scripts.validation import validate_residual_gravity_structures as residual
from scripts.validation import validate_wandering_bh_candidates as wandering


def test_wandering_bh_readiness_fails_closed(tmp_path, monkeypatch):
    out = tmp_path / "wandering.json"
    monkeypatch.setattr(wandering, "OUT", out)

    assert wandering.main() == 0

    payload = json.loads(out.read_text(encoding="utf-8"))
    assert payload["claim_allowed"] is False
    assert payload["status"] == "blocked_missing_observational_data"
    assert all(row["missing_fields"] for row in payload["records"])


def test_residual_gravity_readiness_fails_closed(tmp_path, monkeypatch):
    out = tmp_path / "residual.json"
    monkeypatch.setattr(residual, "OUT", out)

    assert residual.main() == 0

    payload = json.loads(out.read_text(encoding="utf-8"))
    assert payload["claim_allowed"] is False
    assert payload["status"] == "blocked_missing_observational_data"
    assert all(row["missing_fields"] for row in payload["records"])
