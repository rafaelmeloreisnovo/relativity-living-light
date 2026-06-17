#!/usr/bin/env python3
"""Check that validation artifacts stay claim-bound.

Seed-stage artifacts in this repository must keep claim_allowed set to false.
This guard is intentionally small and standard-library only.
"""

from __future__ import annotations

import json
from pathlib import Path

CHECK_ROOTS = [Path("data/results"), Path("data/real"), Path("docs/science")]


def contains_true_claim(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "claim_allowed" and value is True:
                return True
            if contains_true_claim(value):
                return True
    if isinstance(obj, list):
        return any(contains_true_claim(item) for item in obj)
    return False


def text_contains_true_claim(text: str) -> bool:
    lowered = text.lower()
    return "claim_allowed: true" in lowered or '"claim_allowed": true' in lowered


def main() -> int:
    violations = []
    for root in CHECK_ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in {".json", ".yml", ".yaml", ".md"}:
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            found = False
            if path.suffix.lower() == ".json":
                try:
                    found = contains_true_claim(json.loads(text))
                except json.JSONDecodeError:
                    found = text_contains_true_claim(text)
            else:
                found = text_contains_true_claim(text)
            if found:
                violations.append(path.as_posix())

    if violations:
        print("Unsupported claim_allowed=true found:")
        for item in violations:
            print(f"- {item}")
        return 1

    print("Claim boundary check passed: all seed-stage claims remain blocked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
