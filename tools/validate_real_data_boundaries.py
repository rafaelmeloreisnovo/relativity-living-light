#!/usr/bin/env python3
"""Validate real-data manifests against the synthetic/real boundary."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from data.pipelines.structure_d.synthetic_real_boundary import validate_real_dataset_manifest_entry

CANONICAL_MANIFEST = Path("data/real/cosmology/observational_sources_manifest.json")
STRUCTURE_D_CONFIG = Path("data/pipelines/structure_d/datasets_config.json")
JOINT_MANIFEST = Path("data/inputs/cosmology_joint/joint_real_inputs_manifest.json")
REAL_PROFILES = ("structure_d_real_validation", "structure_d_partial_real", "structure_d_real_growth_validation")


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _canonical_sources() -> dict[str, dict[str, Any]]:
    manifest = _load_json(CANONICAL_MANIFEST)
    sources = {entry["source_id"]: entry for entry in manifest.get("canonical_local_real_sources", [])}
    if len(sources) != len(manifest.get("canonical_local_real_sources", [])):
        raise SystemExit("duplicate source_id in canonical observational sources manifest")
    for source_id, entry in sources.items():
        result = validate_real_dataset_manifest_entry(entry)
        if not result["valid"]:
            raise SystemExit(f"invalid canonical source {source_id}: {result}")
    return sources


def _assert_same_source_fields(consumer: str, entry: dict[str, Any], canonical: dict[str, Any]) -> None:
    for field in ("source_id", "sha256", "local_path", "dataset_type"):
        if entry.get(field) != canonical.get(field):
            raise SystemExit(f"{consumer} diverges from canonical source {canonical['source_id']} for {field}")
    result = validate_real_dataset_manifest_entry(entry)
    if not result["valid"]:
        raise SystemExit(f"{consumer} has invalid real dataset path for {entry.get('source_id')}: {result}")


def validate_structure_d(sources: dict[str, dict[str, Any]]) -> None:
    config = _load_json(STRUCTURE_D_CONFIG)
    datasets = config.get("datasets", {})
    for profile_name in REAL_PROFILES:
        for dataset_id in config["profiles"][profile_name]["active_datasets"]:
            entry = datasets[dataset_id]
            source_id = entry.get("source_id")
            if source_id not in sources:
                raise SystemExit(f"{profile_name}/{dataset_id} references unknown source_id {source_id!r}")
            _assert_same_source_fields(f"{STRUCTURE_D_CONFIG}:{profile_name}/{dataset_id}", entry, sources[source_id])


def validate_joint_manifest(sources: dict[str, dict[str, Any]]) -> None:
    joint = _load_json(JOINT_MANIFEST)
    if joint.get("canonical_observational_sources_manifest") != CANONICAL_MANIFEST.as_posix():
        raise SystemExit("joint manifest must point at the canonical observational sources manifest")
    source_ids = [entry["source_id"] for entry in joint.get("inputs", [])]
    if source_ids != joint.get("source_ids"):
        raise SystemExit("joint source_ids must exactly mirror inputs[].source_id order")
    forbidden_duplicate_fields = {"sha256", "local_path", "dataset_type"}
    for entry in joint.get("inputs", []):
        source_id = entry.get("source_id")
        if source_id not in sources:
            raise SystemExit(f"joint manifest references unknown source_id {source_id!r}")
        duplicated = sorted(forbidden_duplicate_fields & set(entry))
        if duplicated:
            raise SystemExit(f"joint input {source_id} duplicates canonical fields: {duplicated}")


def main() -> int:
    sources = _canonical_sources()
    validate_structure_d(sources)
    validate_joint_manifest(sources)
    print("real-data boundary validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
