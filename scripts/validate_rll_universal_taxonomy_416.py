#!/usr/bin/env python3
"""Strict stdlib-only validator for RLL Universal Taxonomy 416."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

TOKEN = "TOKEN_VAZIO"


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    data = json.loads(path.read_text(encoding="utf-8"))
    modules = data.get("modules", [])
    profiles = data.get("completion_profiles", {})
    audit = data.get("count_audit", {})

    if data.get("source_provenance", {}).get("claim_allowed") is not False:
        errors.append("source_provenance.claim_allowed must be false")
    if len(modules) != 386:
        errors.append(f"expected 386 modules, got {len(modules)}")
    indexes = [m.get("source_index") for m in modules]
    if indexes != list(range(1, 387)):
        errors.append("source_index must be contiguous 1..386")
    ids = [m.get("module_id") for m in modules]
    if len(ids) != len(set(ids)):
        errors.append("module_id values must be unique")
    if any(not isinstance(mid, str) or not re.fullmatch(r"UTM-\d{3}", mid) for mid in ids):
        errors.append("module_id must match UTM-NNN")

    counts: dict[str, int] = {}
    for module in modules:
        cid = module.get("cluster_id")
        counts[cid] = counts.get(cid, 0) + 1
        profile = module.get("completion_profile")
        if profile not in profiles:
            errors.append(f"{module.get('module_id')}: unknown completion_profile {profile}")
        if module.get("claim_allowed") is not False:
            errors.append(f"{module.get('module_id')}: claim_allowed must be false")
        if not str(module.get("completion_state", "")).startswith(TOKEN):
            errors.append(f"{module.get('module_id')}: completion_state must preserve TOKEN_VAZIO")

    expected = {"I": 48, "II": 48, "III": 48, "IV": 48, "V": 48, "VI": 48, "VII": 47, "VIII": 51}
    if counts != expected:
        errors.append(f"cluster counts mismatch: {counts}")
    if audit.get("module_count_computed") != 386:
        errors.append("count_audit.module_count_computed must be 386")
    if audit.get("global_count_consistent") is not True:
        errors.append("global_count_consistent must be true")
    discrepancy_ids = {d.get("cluster_id") for d in audit.get("discrepancies", [])}
    if discrepancy_ids != {"VII", "VIII"}:
        errors.append("count discrepancies must explicitly preserve VII and VIII")
    if data.get("source_provenance", {}).get("baseline_macrothemes", 0) + len(modules) != 416:
        errors.append("30 + 386 must equal 416")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path",
        nargs="?",
        default="data/knowledge_taxonomy/rll_universal_taxonomy_416.v1.json",
    )
    args = parser.parse_args()
    errors = validate(Path(args.path))
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        raise SystemExit(1)
    print("PASS: RLL Universal Taxonomy 416")
    print("modules=386; baseline=30; total=416; claim_allowed=false")


if __name__ == "__main__":
    main()
