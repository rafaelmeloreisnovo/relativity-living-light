#!/usr/bin/env python3
"""Structural validator for the RLL latent-theses registry.

This gate checks completeness, falsifiability and claim-boundary hygiene. It
does not validate any physical thesis.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "real_sources" / "rll_latent_theses_registry.yml"

REQUIRED_TOP = {
    "schema", "status", "purpose", "claim_boundary", "allowed_claim",
    "blocked_claims", "validation_policy", "recent_context_policy", "theses",
}
REQUIRED_THESIS = {
    "id", "title", "route", "maturity", "state", "claim_allowed",
    "thesis_statement", "current_evidence", "required_data", "baselines",
    "metrics", "falsifier", "next_action",
}


def fail(msg: str) -> None:
    raise SystemExit(f"ERROR: {msg}")


def require_list(name: str, value: Any, min_items: int = 1) -> list[Any]:
    if not isinstance(value, list) or len(value) < min_items:
        fail(f"{name} must be a list with at least {min_items} item(s)")
    return value


def main() -> int:
    if not REGISTRY.exists():
        fail(f"missing registry: {REGISTRY.relative_to(ROOT)}")
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail("registry root must be a mapping")
    missing = REQUIRED_TOP - set(data)
    if missing:
        fail(f"top-level fields missing: {sorted(missing)}")
    if data.get("schema") != "rll.latent_theses_registry.v1":
        fail(f"unexpected schema: {data.get('schema')!r}")

    boundary = str(data.get("claim_boundary", "")).lower()
    for term in ("does not validate rll", "does not assert", "does not promote"):
        if term not in boundary:
            fail(f"claim_boundary missing required term: {term}")

    blocked_text = "\n".join(str(x).lower() for x in require_list("blocked_claims", data.get("blocked_claims"), 3))
    if "rll" not in blocked_text:
        fail("blocked_claims must explicitly mention RLL")
    if not any(x in blocked_text for x in ("lcdm", "cpl", "desi", "planck", "jwst", "lvk")):
        fail("blocked_claims must name adversary or external-evidence families")

    policy = data.get("validation_policy") or {}
    required_before = require_list("validation_policy.required_before_claim", policy.get("required_before_claim"), 6)
    for item in ("baseline_or_adversary_model", "metric", "falsifier"):
        if item not in required_before:
            fail(f"required_before_claim missing {item}")
    if policy.get("claim_allowed_default") is not False:
        fail("claim_allowed_default must be false")

    theses = require_list("theses", data.get("theses"), 3)
    seen: set[str] = set()
    for row in theses:
        if not isinstance(row, dict):
            fail("each thesis must be a mapping")
        missing_row = REQUIRED_THESIS - set(row)
        if missing_row:
            fail(f"{row.get('id', '<unknown>')}: missing fields {sorted(missing_row)}")
        thesis_id = str(row["id"])
        if thesis_id in seen:
            fail(f"duplicate thesis id: {thesis_id}")
        seen.add(thesis_id)
        if not thesis_id.startswith("LT-"):
            fail(f"{thesis_id}: id must start with LT-")
        if row.get("claim_allowed") is not False:
            fail(f"{thesis_id}: claim_allowed must be false")
        if not str(row.get("state", "")).startswith("TOKEN_VAZIO"):
            fail(f"{thesis_id}: state must remain TOKEN_VAZIO* before evidence gates")
        require_list(f"{thesis_id}.required_data", row.get("required_data"), 1)
        require_list(f"{thesis_id}.baselines", row.get("baselines"), 1)
        require_list(f"{thesis_id}.metrics", row.get("metrics"), 1)
        if len(str(row.get("falsifier", "")).strip()) < 40:
            fail(f"{thesis_id}: falsifier too short")
        evidence = row.get("current_evidence")
        if not isinstance(evidence, dict):
            fail(f"{thesis_id}: current_evidence must be a mapping")
        for key in ("repo_artifact", "current_diagnostic", "current_limit"):
            if not str(evidence.get(key, "")).strip():
                fail(f"{thesis_id}: current_evidence.{key} required")

    print(f"OK: {REGISTRY.relative_to(ROOT)} ({len(theses)} latent theses)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
