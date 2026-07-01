#!/usr/bin/env python3
"""Validate real-data source manifest structure.

This validator checks source registration metadata only. It does not download data,
compute cosmological metrics, or validate scientific claims.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED_TOP_LEVEL = {
    "schema",
    "status",
    "claim_boundary",
    "promotion_requirements",
    "sources",
}

REQUIRED_SOURCE_FIELDS = {
    "id",
    "domain",
    "source_type",
    "public_reference",
    "public_url",
    "expected_repository_layer",
    "current_state",
    "local_artifact_path",
    "checksum",
    "ingestion_command",
    "claim_allowed",
    "claim_blocked",
}

ALLOWED_STATES = {
    "SOURCE_REGISTERED",
    "INGESTION_READY",
    "INGESTED_UNVERIFIED",
    "INGESTED_VERIFIED",
    "METRIC_READY",
    "BASELINE_COMPARED",
    "REAL_VALIDATED_LIMITED",
    "CLAIM_BLOCKED",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_manifest(path: Path) -> None:
    if not path.exists():
        fail(f"manifest not found: {path}")

    data = json.loads(path.read_text(encoding="utf-8"))

    missing = REQUIRED_TOP_LEVEL - set(data)
    if missing:
        fail(f"missing top-level fields: {sorted(missing)}")

    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        fail("sources must be a non-empty list")

    ids: set[str] = set()
    for index, source in enumerate(sources):
        if not isinstance(source, dict):
            fail(f"source #{index} is not an object")

        missing_fields = REQUIRED_SOURCE_FIELDS - set(source)
        if missing_fields:
            fail(f"source #{index} missing fields: {sorted(missing_fields)}")

        source_id = str(source["id"])
        if source_id in ids:
            fail(f"duplicate source id: {source_id}")
        ids.add(source_id)

        state = source.get("current_state")
        if state not in ALLOWED_STATES:
            fail(f"source {source_id} has invalid state: {state}")

        public_url = str(source.get("public_url", ""))
        if not public_url.startswith(("http://", "https://")):
            fail(f"source {source_id} public_url must be absolute http(s) URL")

        blocked = str(source.get("claim_blocked", "")).strip()
        if not blocked:
            fail(f"source {source_id} must state blocked claims")

    print(f"OK: {path} ({len(sources)} sources)")


def main(argv: list[str]) -> int:
    path = Path(argv[1]) if len(argv) > 1 else Path("data/real/cosmology/observational_sources_manifest.json")
    validate_manifest(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
