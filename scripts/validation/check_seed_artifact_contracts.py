#!/usr/bin/env python3
"""Lightweight contract checks for canonical seed artifacts.

No external jsonschema dependency is required; this checks only the stable
contract fields used by the current CI artifacts.
"""

from __future__ import annotations

import json
from pathlib import Path

CHECKS = [
    {
        "path": Path("data/results/bootstrap/real_seed_ingestion_plan.json"),
        "required": ["schema_version", "status", "claim_allowed", "total_items", "routes", "items", "safe_conclusion"],
        "claim_allowed": False,
    },
    {
        "path": Path("data/results/orbital_dynamics/angular_momentum_shape_validation.json"),
        "required": ["schema_version", "module", "input_file", "data_status", "claim_allowed", "items", "status"],
        "claim_allowed": False,
    },
    {
        "path": Path("data/results/negative_results_ledger.json"),
        "required": ["schema_version", "status", "claim_allowed", "items", "safe_conclusion"],
        "claim_allowed": False,
    },
    {
        "path": Path("data/results/bootstrap/token_vazio_priority_ledger.json"),
        "required": ["schema_version", "status", "claim_allowed", "items", "safe_conclusion"],
        "claim_allowed": False,
    },
]


def main() -> int:
    errors: list[str] = []
    for check in CHECKS:
        path = check["path"]
        if not path.exists():
            errors.append(f"missing artifact: {path}")
            continue
        payload = json.loads(path.read_text(encoding="utf-8"))
        for key in check["required"]:
            if key not in payload:
                errors.append(f"{path}: missing key {key}")
        if payload.get("claim_allowed") is not check["claim_allowed"]:
            errors.append(f"{path}: claim_allowed must be {check['claim_allowed']}")
        if isinstance(payload.get("items"), list) and not payload["items"]:
            errors.append(f"{path}: items must not be empty")

    if errors:
        print("artifact contract check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("artifact contract check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
