from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

REGISTRY = Path("data/real_sources/rll_required_data_gap_registry.yml")
DOC = Path("docs/science/RLL_REQUIRED_DATA_GAPS_IMPLEMENTATION.md")
VALIDATOR = Path("tools/validate_required_data_gap_registry.py")


def test_required_data_gap_registry_validator_passes():
    result = subprocess.run(
        [sys.executable, str(VALIDATOR)],
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "OK:" in result.stdout


def test_required_data_gap_registry_is_claim_blocked():
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    assert data["schema"] == "rll.required_data_gap_registry.v1"
    assert data["claim_allowed"] is False
    assert "does not validate" in data["claim_boundary"]
    assert data["promotion_policy"]["default_state"] == "TOKEN_VAZIO"

    gaps = data["gaps"]
    assert len(gaps) >= 8
    assert any(row["priority"] == "P0" for row in gaps)
    ids = {row["id"] for row in gaps}
    assert {
        "GAP-COSMO-ROBUST-FIT",
        "GAP-COSMO-SUPERNOVA",
        "GAP-COSMO-GROWTH",
        "GAP-REMNANT-POSTERIORS",
    }.issubset(ids)

    for row in gaps:
        assert row["state"].startswith("TOKEN_VAZIO")
        assert row["baselines"]
        assert row["metrics"]
        assert len(row["required_evidence"]) >= 3
        assert row["falsifier"]
        assert row["target_path"]


def test_required_data_gap_doc_links_registry_and_priorities():
    text = DOC.read_text(encoding="utf-8")
    assert "data/real_sources/rll_required_data_gap_registry.yml" in text
    assert "GAP-REMNANT-POSTERIORS" in text
    assert "GAP-COSMO-ROBUST-FIT" in text
    assert "claim_allowed=false" in text
