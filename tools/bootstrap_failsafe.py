#!/usr/bin/env python3
"""Phase 0 of the RLL JSON Evolution Watcher: one-time bootstrap.

Reads RLL_JSON_EVOLUTION_WATCHER.yml, and for each registered real-data
source computes a sha256 fingerprint over its committed local files, writes a
failsafe snapshot under data/failsafe/, writes a fingerprint file under
schemas/fingerprints/, and appends a BOOTSTRAP event per source to
artifacts/EVOLUTION_TRAIL.jsonl (validated against
schemas/evolution_event.schema.json). It never fetches from the network and
never modifies the tracked real-data files themselves.

Claim boundary: bootstrapping a source only means its committed file is
present and fingerprinted. It does not validate RLL and does not confirm any
scientific claim.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from pathlib import Path
from typing import Any

import yaml

try:
    import jsonschema
except ImportError:  # pragma: no cover - exercised by environment setup
    jsonschema = None

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "RLL_JSON_EVOLUTION_WATCHER.yml"
TRAIL_PATH = ROOT / "artifacts" / "EVOLUTION_TRAIL.jsonl"
MANIFEST_PATH = ROOT / "results" / "evolution_watcher_manifest.json"
FAILSAFE_DIR = ROOT / "data" / "failsafe"
FINGERPRINT_DIR = ROOT / "schemas" / "fingerprints"
EVENT_SCHEMA_PATH = ROOT / "schemas" / "evolution_event.schema.json"


def utc_now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def load_config(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit(f"config root must be a mapping: {path}")
    required = {"meta", "schema_fingerprints", "sources", "global_failover", "rollback_global", "artifact_evolution_trail"}
    missing = required - set(data)
    if missing:
        raise SystemExit(f"config missing required sections: {sorted(missing)}")
    return data


def real_sources(config: dict[str, Any]) -> list[dict[str, Any]]:
    return [s for s in config["sources"] if not s.get("template_only")]


def fingerprint_source(base: Path, local_paths: list[str]) -> tuple[str, list[dict[str, str]]]:
    per_file: list[dict[str, str]] = []
    digest = hashlib.sha256()
    for rel_path in sorted(local_paths):
        full = base / rel_path
        if not full.exists():
            raise SystemExit(f"registered local_path does not exist: {rel_path}")
        file_digest = hashlib.sha256(full.read_bytes()).hexdigest()
        per_file.append({"path": rel_path, "sha256": file_digest})
        digest.update(rel_path.encode("utf-8"))
        digest.update(file_digest.encode("utf-8"))
    return digest.hexdigest(), per_file


def load_event_schema() -> dict[str, Any] | None:
    if jsonschema is None or not EVENT_SCHEMA_PATH.exists():
        return None
    return json.loads(EVENT_SCHEMA_PATH.read_text(encoding="utf-8"))


def append_trail_event(event: dict[str, Any], schema: dict[str, Any] | None, *, dry_run: bool) -> None:
    if schema is not None:
        jsonschema.validate(event, schema)
    if dry_run:
        return
    TRAIL_PATH.parent.mkdir(parents=True, exist_ok=True)
    with TRAIL_PATH.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(event, ensure_ascii=False) + "\n")


def load_manifest() -> dict[str, Any]:
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return {"schema": "rll.evolution_watcher_manifest.v1", "sources": {}}


def write_manifest(manifest: dict[str, Any], *, dry_run: bool) -> None:
    if dry_run:
        return
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    manifest["updated_utc"] = utc_now()
    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def bootstrap_one(source: dict[str, Any], schema: dict[str, Any] | None, manifest: dict[str, Any], *, force: bool, dry_run: bool) -> dict[str, Any]:
    source_id = str(source["id"])
    failsafe_path = FAILSAFE_DIR / f"{source_id}_FROZEN.json"
    fingerprint_path = FINGERPRINT_DIR / f"{source_id}.sha256"

    if failsafe_path.exists() and not force:
        return {"source_id": source_id, "status": "already_bootstrapped", "failsafe_path": str(failsafe_path.relative_to(ROOT))}

    fingerprint, per_file = fingerprint_source(ROOT, source["local_paths"])
    epistemic_after = str(source.get("epistemic_initial", "TOKEN_VAZIO"))

    snapshot = {
        "schema": "rll.evolution_watcher_failsafe_snapshot.v1",
        "source_id": source_id,
        "label": source.get("label", ""),
        "created_utc": utc_now(),
        "fingerprint": fingerprint,
        "files": per_file,
        "epistemic_state": epistemic_after,
        "primary_source": source.get("primary_source", {}),
    }

    event = {
        "timestamp_utc": utc_now(),
        "source_id": source_id,
        "action": "BOOTSTRAP",
        "schema_drift": False,
        "epistemic_before": "TOKEN_VAZIO",
        "epistemic_after": epistemic_after,
        "fingerprint_before": "",
        "fingerprint_after": fingerprint,
        "artifact_path": str(failsafe_path.relative_to(ROOT)),
        "rll_paths_affected": list(source.get("rll_paths_affected", [])),
        "notes": f"bootstrap: {len(per_file)} file(s) fingerprinted, force={force}",
    }
    append_trail_event(event, schema, dry_run=dry_run)

    if not dry_run:
        FAILSAFE_DIR.mkdir(parents=True, exist_ok=True)
        FINGERPRINT_DIR.mkdir(parents=True, exist_ok=True)
        failsafe_path.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        fingerprint_path.write_text(fingerprint + "\n", encoding="utf-8")

    manifest.setdefault("sources", {})[source_id] = {
        "epistemic_state": epistemic_after,
        "fingerprint": fingerprint,
        "last_action": "BOOTSTRAP",
        "last_run_utc": utc_now(),
    }

    return {"source_id": source_id, "status": "bootstrapped", "failsafe_path": str(failsafe_path.relative_to(ROOT)), "fingerprint": fingerprint}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--source", type=str, default=None, help="Bootstrap a single source id; default is all sources.")
    parser.add_argument("--force", action="store_true", help="Re-bootstrap even if a failsafe snapshot already exists.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    config = load_config(args.config)
    schema = load_event_schema()
    manifest = load_manifest()

    sources = real_sources(config)
    if args.source:
        sources = [s for s in sources if s["id"] == args.source]
        if not sources:
            raise SystemExit(f"unknown source id: {args.source}")

    results = [bootstrap_one(source, schema, manifest, force=args.force, dry_run=args.dry_run) for source in sources]
    write_manifest(manifest, dry_run=args.dry_run)

    for result in results:
        print(f"[{result['source_id']}] {result['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
