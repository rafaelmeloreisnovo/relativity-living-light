#!/usr/bin/env python3
"""Validate the RLL required-data gap registry.

This is a structural gate for route-level absences. It does not validate RLL or
materialize data.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "real_sources" / "rll_required_data_gap_registry.yml"

REQUIRED_TOP = {
    "schema",
    "status",
    "purpose",
    "claim_boundary",
    "claim_allowed",
    "promotion_policy",
    "gaps",
}
REQUIRED_GAP = {
    "id",
    "route",
    "priority",
    "state",
    "linked_theses",
    "needed_data_or_artifact",
    "target_path",
    "baselines",
    "metrics",
    "required_evidence",
    "falsifier",
    "next_action",
}
ALLOWED_PRIORITIES = {"P0", "P1", "P2", "P3"}


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


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
    if data.get("schema") != "rll.required_data_gap_registry.v1":
        fail(f"unexpected schema: {data.get('schema')!r}")
    if data.get("claim_allowed") is not False:
        fail("claim_allowed must be false")
    boundary = str(data.get("claim_boundary", "")).lower()
    for term in ("does not validate", "does not approve"):
        if term not in boundary:
            fail(f"claim_boundary missing term: {term}")

    policy = data.get("promotion_policy") or {}
    if policy.get("default_state") != "TOKEN_VAZIO":
        fail("promotion_policy.default_state must be TOKEN_VAZIO")
    required_ready = require_list(
        "promotion_policy.required_for_test_ready",
        policy.get("required_for_test_ready"),
        5,
    )
    for item in ("baseline", "metric", "falsifier"):
        if item not in required_ready:
            fail(f"required_for_test_ready missing {item}")

    gaps = require_list("gaps", data.get("gaps"), 3)
    ids: set[str] = set()
    p0_count = 0
    for row in gaps:
        if not isinstance(row, dict):
            fail("each gap must be a mapping")
        missing_gap = REQUIRED_GAP - set(row)
        if missing_gap:
            fail(f"{row.get('id', '<unknown>')}: missing fields {sorted(missing_gap)}")
        gap_id = str(row["id"])
        if gap_id in ids:
            fail(f"duplicate gap id: {gap_id}")
        ids.add(gap_id)
        if not gap_id.startswith("GAP-"):
            fail(f"{gap_id}: id must start with GAP-")
        if row["priority"] not in ALLOWED_PRIORITIES:
            fail(f"{gap_id}: invalid priority {row['priority']!r}")
        if row["priority"] == "P0":
            p0_count += 1
        if not str(row["state"]).startswith("TOKEN_VAZIO"):
            fail(f"{gap_id}: state must remain TOKEN_VAZIO* until evidence is materialized")
        require_list(f"{gap_id}.linked_theses", row.get("linked_theses"), 1)
        require_list(f"{gap_id}.baselines", row.get("baselines"), 1)
        require_list(f"{gap_id}.metrics", row.get("metrics"), 1)
        require_list(f"{gap_id}.required_evidence", row.get("required_evidence"), 3)
        if len(str(row.get("falsifier", "")).strip()) < 25:
            fail(f"{gap_id}: falsifier too short")
        if not str(row.get("target_path", "")).strip():
            fail(f"{gap_id}: target_path required")
    if p0_count < 2:
        fail("registry must contain at least two P0 gaps")

    print(f"OK: {REGISTRY.relative_to(ROOT)} ({len(gaps)} gaps)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
