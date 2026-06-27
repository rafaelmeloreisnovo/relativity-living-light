#!/usr/bin/env python3
"""Validate migration of historical to_Add content into canonical locations.

This validator does not execute scientific logic. It only checks that the
historical intake directory is mapped to canonical code/docs/results locations
and that compatibility wrappers point to data.pipelines.structure_d.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_CANONICAL_PATHS = [
    "data/pipelines/structure_d/__init__.py",
    "data/pipelines/structure_d/cosmo.py",
    "data/pipelines/structure_d/feedback_agn.py",
    "data/pipelines/structure_d/growth.py",
    "data/pipelines/structure_d/likelihood.py",
    "data/pipelines/structure_d/models.py",
    "data/pipelines/structure_d/run_all.py",
    "data/pipelines/structure_d/make_example_data.py",
    "data/inputs/structure_d/README.md",
    "results/structure_d/README.md",
    "docs/science/structure_d/README.md",
    "docs/science/structure_d/EQUATIONS.md",
    "docs/science/structure_d/AGN_FEEDBACK_BRIDGE.md",
    "docs/science/structure_d/EVIDENCE_TRACEABILITY.md",
    "docs/yml/TO_ADD_MIGRATION_LEDGER.yml",
]

LEGACY_WRAPPERS = [
    "RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/__init__.py",
    "RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/cosmo.py",
    "RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/feedback_agn.py",
    "RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/growth.py",
    "RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/likelihood.py",
    "RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/models.py",
    "RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/run_all.py",
    "RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/make_example_data.py",
]

OPTIONAL_HISTORICAL_WRAPPERS = [
    "to_Add/RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/__init__.py",
    "to_Add/RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/cosmo.py",
    "to_Add/RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/feedback_agn.py",
    "to_Add/RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/growth.py",
    "to_Add/RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/likelihood.py",
    "to_Add/RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/models.py",
    "to_Add/RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/run_all.py",
    "to_Add/RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/make_example_data.py",
]


def exists(rel: str) -> bool:
    return (ROOT / rel).exists()


def wrapper_targets_structure_d(rel: str) -> bool:
    path = ROOT / rel
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8", errors="replace")
    return "data.pipelines.structure_d" in text and "from data.pipelines.structure_d" in text


def main() -> int:
    missing_canonical = [rel for rel in REQUIRED_CANONICAL_PATHS if not exists(rel)]
    invalid_wrappers = [rel for rel in LEGACY_WRAPPERS if not wrapper_targets_structure_d(rel)]
    historical_wrappers_present = [rel for rel in OPTIONAL_HISTORICAL_WRAPPERS if exists(rel)]
    historical_wrappers_invalid = [rel for rel in historical_wrappers_present if not wrapper_targets_structure_d(rel)]

    ok = not missing_canonical and not invalid_wrappers and not historical_wrappers_invalid
    payload = {
        "schema": "rll.to_add_migration_validation.v1",
        "claim_allowed": False,
        "ok": ok,
        "missing_canonical": missing_canonical,
        "invalid_legacy_wrappers": invalid_wrappers,
        "historical_wrappers_present": historical_wrappers_present,
        "historical_wrappers_invalid": historical_wrappers_invalid,
        "safe_conclusion": (
            "to_Add migration validates as controlled legacy intake." if ok else
            "to_Add migration is incomplete; keep claims blocked and inspect missing/invalid paths."
        ),
    }

    out_json = ROOT / "data/results/to_add_migration_validation.json"
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    out_md = ROOT / "docs/TO_ADD_MIGRATION_STATUS.md"
    out_md.write_text(
        "# to_Add Migration Status\n\n"
        f"- ok: `{ok}`\n"
        f"- missing_canonical: `{missing_canonical}`\n"
        f"- invalid_legacy_wrappers: `{invalid_wrappers}`\n"
        f"- historical_wrappers_invalid: `{historical_wrappers_invalid}`\n\n"
        "Claim: `claim_allowed=false`\n",
        encoding="utf-8",
    )

    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0 if ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
