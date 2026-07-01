from __future__ import annotations

import json
from pathlib import Path


REGISTRY = Path("data/real/cosmology/real_data_addition_registry_2026_07.json")

REQUIRED_TOP_LEVEL = {
    "schema",
    "generated_utc",
    "purpose",
    "claim_boundary",
    "allowed_states",
    "rows",
}

REQUIRED_ROW_FIELDS = {
    "dataset_id",
    "domain",
    "state",
    "primary_source",
    "source_url",
    "local_expected_paths",
    "existing_repository_support",
    "promotion_requirements",
    "claim_blocked",
}

BLOCKED_PHRASES = [
    "RLL is validated",
    "RLL beats LCDM",
    "RLL beats CPL",
    "DESI confirms RLL",
    "Pantheon+ confirms RLL",
]


def main() -> int:
    if not REGISTRY.exists():
        raise FileNotFoundError(f"missing registry: {REGISTRY}")

    payload = json.loads(REGISTRY.read_text(encoding="utf-8"))
    missing = REQUIRED_TOP_LEVEL - set(payload)
    if missing:
        raise ValueError(f"registry missing top-level fields: {sorted(missing)}")

    if "not scientific validation" not in payload["claim_boundary"]:
        raise ValueError("top-level claim_boundary must state that source registration is not validation")

    allowed_states = set(payload["allowed_states"])
    rows = payload["rows"]
    if not rows:
        raise ValueError("registry rows must not be empty")

    for idx, row in enumerate(rows):
        missing_row = REQUIRED_ROW_FIELDS - set(row)
        if missing_row:
            raise ValueError(f"row {idx} missing fields: {sorted(missing_row)}")

        state = row["state"]
        dataset_id = row["dataset_id"]
        if state not in allowed_states:
            raise ValueError(f"row {dataset_id}: state {state!r} not in allowed_states")

        if state == "REAL_VALIDATED_LIMITED":
            local_paths = row.get("local_expected_paths", [])
            requirements = "\n".join(row.get("promotion_requirements", []))
            if not local_paths:
                raise ValueError(f"row {dataset_id}: REAL_VALIDATED_LIMITED requires local paths")
            if "checksum" not in requirements.lower() and "sha256" not in requirements.lower():
                raise ValueError(f"row {dataset_id}: REAL_VALIDATED_LIMITED requires checksum/sha256 requirement")

        blocked = "\n".join(row.get("claim_blocked", []))
        if state in {"SOURCE_REGISTERED_ONLY", "DOWNLOAD_READY", "REAL_VALIDATED_BLOCKED"} and not blocked:
            raise ValueError(f"row {dataset_id}: non-validated states require claim_blocked entries")

        for phrase in BLOCKED_PHRASES:
            if phrase in row.get("promotion_requirements", []):
                raise ValueError(f"row {dataset_id}: blocked phrase appears as promotion requirement: {phrase}")

    print(f"OK: validated {len(rows)} real-data registry rows from {REGISTRY}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
