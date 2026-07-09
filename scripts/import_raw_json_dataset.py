#!/usr/bin/env python3
"""Import a raw JSON dataset into an auditable local artifact directory.

This script is structural infrastructure only. It parses JSON, writes an atomic
copy, emits manifest/checksum files, and records rollback metadata. It does not
validate any scientific model or promote any claim.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

CLAIM_BOUNDARY = (
    "Raw JSON import records structure, checksum and rollback metadata only; "
    "it does not validate RLL or any scientific claim."
)


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def safe_id(value: str) -> str:
    normalized = re.sub(r"[^A-Za-z0-9_.-]+", "_", value.strip())
    normalized = normalized.strip("._-")
    if not normalized:
        raise ValueError("dataset id cannot be empty")
    return normalized[:120]


def detect_json_shape(payload: Any) -> dict[str, Any]:
    if isinstance(payload, list):
        first = payload[0] if payload else None
        return {
            "json_type": "array",
            "row_count": len(payload),
            "first_item_type": type(first).__name__ if first is not None else "TOKEN_VAZIO",
            "first_item_keys": sorted(first.keys()) if isinstance(first, dict) else [],
        }
    if isinstance(payload, dict):
        return {
            "json_type": "object",
            "row_count": 1,
            "top_level_keys": sorted(payload.keys()),
        }
    return {"json_type": type(payload).__name__, "row_count": 1}


def atomic_write_bytes(target: Path, payload: bytes) -> dict[str, Any]:
    target.parent.mkdir(parents=True, exist_ok=True)
    backup_path = None
    rollback_available = False
    if target.exists():
        backup_path = target.with_suffix(target.suffix + ".rollback")
        shutil.copy2(target, backup_path)
        rollback_available = True

    fd, temp_name = tempfile.mkstemp(prefix=target.name + ".", suffix=".tmp", dir=str(target.parent))
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        Path(temp_name).replace(target)
    except Exception:
        Path(temp_name).unlink(missing_ok=True)
        raise

    return {
        "target": str(target),
        "rollback_available": rollback_available,
        "backup_path": str(backup_path) if backup_path else None,
    }


def import_json(input_path: Path, output_dir: Path, dataset_id: str | None = None) -> dict[str, Any]:
    raw = input_path.read_bytes()
    try:
        payload = json.loads(raw.decode("utf-8"))
    except Exception as exc:
        raise SystemExit(f"invalid JSON input: {input_path}: {exc}") from exc

    resolved_id = safe_id(dataset_id or input_path.stem)
    target = output_dir / f"{resolved_id}.raw.json"
    write_result = atomic_write_bytes(target, raw)
    digest = sha256_bytes(raw)
    shape = detect_json_shape(payload)

    manifest = {
        "schema": "rll.raw_json_import.v1",
        "status": "RAW_JSON_IMPORTED_STRUCTURAL_ONLY",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "dataset_id": resolved_id,
        "source_path": str(input_path),
        "target_path": str(target),
        "sha256": digest,
        "bytes": len(raw),
        "autodetected_shape": shape,
        "failsafe": {
            "atomic_write": True,
            "rollback_available": write_result["rollback_available"],
            "backup_path": write_result["backup_path"],
            "invalid_json_blocks_write": True,
        },
        "claim_boundary": CLAIM_BOUNDARY,
    }

    manifest_path = output_dir / f"{resolved_id}.MANIFEST.json"
    checksum_path = output_dir / f"{resolved_id}.CHECKSUMS.sha256"
    atomic_write_bytes(manifest_path, json.dumps(manifest, indent=2, sort_keys=True).encode("utf-8"))
    atomic_write_bytes(checksum_path, f"{digest}  {target.name}\n".encode("utf-8"))
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Import raw JSON with checksum, autodetection and rollback metadata.")
    parser.add_argument("--input", required=True, type=Path, help="Path to a local JSON file")
    parser.add_argument("--output-dir", required=True, type=Path, help="Directory for imported raw JSON artifacts")
    parser.add_argument("--dataset-id", default=None, help="Optional stable dataset id; defaults to input filename stem")
    args = parser.parse_args()

    manifest = import_json(args.input, args.output_dir, args.dataset_id)
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
