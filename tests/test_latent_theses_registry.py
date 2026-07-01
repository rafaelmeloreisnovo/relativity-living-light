from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

REGISTRY = Path("data/real_sources/rll_latent_theses_registry.yml")
DOC = Path("docs/science/RLL_LATENT_THESES_AND_RECENT_DATA_CROSSWALK.md")
VALIDATOR = Path("tools/validate_latent_theses_registry.py")


def test_latent_theses_registry_validator_passes():
    result = subprocess.run(
        [sys.executable, str(VALIDATOR)],
        check=False,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "OK:" in result.stdout


def test_latent_theses_are_claim_blocked_and_falsifiable():
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    assert data["schema"] == "rll.latent_theses_registry.v1"
    assert data["validation_policy"]["claim_allowed_default"] is False
    assert "does not validate RLL" in data["claim_boundary"]

    theses = data["theses"]
    assert len(theses) >= 6
    ids = {row["id"] for row in theses}
    assert {"LT-001", "LT-002", "LT-003", "LT-004", "LT-005", "LT-006"}.issubset(ids)

    for row in theses:
        assert row["claim_allowed"] is False
        assert row["state"].startswith("TOKEN_VAZIO")
        assert row["required_data"]
        assert row["baselines"]
        assert row["metrics"]
        assert len(row["falsifier"]) >= 40
        assert row["current_evidence"]["repo_artifact"]
        assert row["current_evidence"]["current_diagnostic"]
        assert row["current_evidence"]["current_limit"]


def test_latent_theses_crosswalk_links_registry_and_blocks_claims():
    text = DOC.read_text(encoding="utf-8")
    assert "data/real_sources/rll_latent_theses_registry.yml" in text
    assert "claim_allowed=false" in text
    assert "RLL is a falsifiable candidate program" in text
    assert "RLL is confirmed" in text
    assert "RLL beats LCDM/CPL" in text
