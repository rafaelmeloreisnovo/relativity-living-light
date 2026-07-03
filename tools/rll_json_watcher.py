#!/usr/bin/env python3
"""Phase 1 of the RLL JSON Evolution Watcher: main run.

For each registered real-data source, recomputes the sha256 fingerprint of
its committed local files and compares it against the last recorded
fingerprint. It never fetches from a network and never overwrites a
committed real-data file: the git-tracked file is always the source of
truth. What this script tracks is the *history* of that file (fingerprint,
epistemic state, drift) so uploads/updates are auditable over time.

Actions written to artifacts/EVOLUTION_TRAIL.jsonl (schema:
schemas/evolution_event.schema.json):
  FETCH         first time a source is seen without a prior fingerprint
  SKIP_EXISTING fingerprint unchanged since last run
  UPDATE        fingerprint changed (schema_drift=true)
  FAILSAFE      a registered local file is missing/unreadable
  ROLLBACK      --rollback restored a source's tracked state from data/failsafe/

Claim boundary: this script performs structural provenance bookkeeping only.
It does not validate RLL, does not run any cosmological fit, and does not
confirm any scientific claim. Epistemic states describe data provenance
tracking, not scientific truth.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

_ROOT_DIR = Path(__file__).resolve().parents[1]
if str(_ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(_ROOT_DIR))
from tools.bootstrap_failsafe import (  # noqa: E402
    DEFAULT_CONFIG,
    FAILSAFE_DIR,
    FINGERPRINT_DIR,
    ROOT,
    append_trail_event,
    fingerprint_source,
    load_config,
    load_event_schema,
    load_manifest,
    real_sources,
    utc_now,
    write_manifest,
)

DOWNGRADE_FROM_VERIFIED = "DECLARED_BY_AUTHOR"


def watch_one(source: dict[str, Any], schema: dict[str, Any] | None, manifest: dict[str, Any], *, dry_run: bool) -> dict[str, Any]:
    source_id = str(source["id"])
    fingerprint_path = FINGERPRINT_DIR / f"{source_id}.sha256"
    prior_entry = manifest.get("sources", {}).get(source_id, {})
    prior_fingerprint = str(prior_entry.get("fingerprint", ""))
    if not prior_fingerprint and fingerprint_path.exists():
        prior_fingerprint = fingerprint_path.read_text(encoding="utf-8").strip()

    missing = [p for p in source["local_paths"] if not (ROOT / p).exists()]
    if missing:
        epistemic_before = str(prior_entry.get("epistemic_state", source.get("epistemic_initial", "TOKEN_VAZIO")))
        event = {
            "timestamp_utc": utc_now(),
            "source_id": source_id,
            "action": "FAILSAFE",
            "schema_drift": False,
            "epistemic_before": epistemic_before,
            "epistemic_after": "TOKEN_VAZIO",
            "fingerprint_before": prior_fingerprint,
            "fingerprint_after": "",
            "artifact_path": str((FAILSAFE_DIR / f"{source_id}_FROZEN.json").relative_to(ROOT)),
            "rll_paths_affected": list(source.get("rll_paths_affected", [])),
            "notes": f"missing registered local_paths: {missing}",
        }
        append_trail_event(event, schema, dry_run=dry_run)
        manifest.setdefault("sources", {})[source_id] = {
            "epistemic_state": "TOKEN_VAZIO",
            "fingerprint": prior_fingerprint,
            "last_action": "FAILSAFE",
            "last_run_utc": utc_now(),
        }
        return {"source_id": source_id, "status": "FAILSAFE", "detail": str(missing)}

    fingerprint, _per_file = fingerprint_source(ROOT, source["local_paths"])
    epistemic_before = str(prior_entry.get("epistemic_state", source.get("epistemic_initial", "TOKEN_VAZIO")))

    if not prior_fingerprint:
        action = "FETCH"
        schema_drift = False
        epistemic_after = str(source.get("epistemic_initial", "TOKEN_VAZIO"))
    elif fingerprint == prior_fingerprint:
        action = "SKIP_EXISTING"
        schema_drift = False
        epistemic_after = epistemic_before
    else:
        action = "UPDATE"
        schema_drift = True
        epistemic_after = epistemic_before

    event = {
        "timestamp_utc": utc_now(),
        "source_id": source_id,
        "action": action,
        "schema_drift": schema_drift,
        "epistemic_before": epistemic_before,
        "epistemic_after": epistemic_after,
        "fingerprint_before": prior_fingerprint,
        "fingerprint_after": fingerprint,
        "artifact_path": "",
        "rll_paths_affected": list(source.get("rll_paths_affected", [])),
        "notes": f"local-first fingerprint check; action={action}",
    }
    append_trail_event(event, schema, dry_run=dry_run)

    manifest.setdefault("sources", {})[source_id] = {
        "epistemic_state": epistemic_after,
        "fingerprint": fingerprint,
        "last_action": action,
        "last_run_utc": utc_now(),
    }
    if not dry_run:
        FINGERPRINT_DIR.mkdir(parents=True, exist_ok=True)
        fingerprint_path.write_text(fingerprint + "\n", encoding="utf-8")

    return {"source_id": source_id, "status": action, "schema_drift": schema_drift}


def rollback_one(source: dict[str, Any], schema: dict[str, Any] | None, manifest: dict[str, Any], *, dry_run: bool) -> dict[str, Any]:
    source_id = str(source["id"])
    failsafe_path = FAILSAFE_DIR / f"{source_id}_FROZEN.json"
    if not failsafe_path.exists():
        return {"source_id": source_id, "status": "no_checkpoint_to_rollback_to"}

    snapshot = json.loads(failsafe_path.read_text(encoding="utf-8"))
    frozen_state = str(snapshot.get("epistemic_state", "TOKEN_VAZIO"))
    epistemic_after = DOWNGRADE_FROM_VERIFIED if frozen_state == "VERIFIED" else frozen_state
    prior_entry = manifest.get("sources", {}).get(source_id, {})

    event = {
        "timestamp_utc": utc_now(),
        "source_id": source_id,
        "action": "ROLLBACK",
        "schema_drift": False,
        "epistemic_before": str(prior_entry.get("epistemic_state", frozen_state)),
        "epistemic_after": epistemic_after,
        "fingerprint_before": str(prior_entry.get("fingerprint", "")),
        "fingerprint_after": str(snapshot.get("fingerprint", "")),
        "artifact_path": str(failsafe_path.relative_to(ROOT)),
        "rll_paths_affected": list(source.get("rll_paths_affected", [])),
        "notes": "rollback restores tracked state from failsafe snapshot; never promotes to VERIFIED",
    }
    append_trail_event(event, schema, dry_run=dry_run)

    manifest.setdefault("sources", {})[source_id] = {
        "epistemic_state": epistemic_after,
        "fingerprint": str(snapshot.get("fingerprint", "")),
        "last_action": "ROLLBACK",
        "last_run_utc": utc_now(),
    }
    if not dry_run:
        FINGERPRINT_DIR.mkdir(parents=True, exist_ok=True)
        (FINGERPRINT_DIR / f"{source_id}.sha256").write_text(str(snapshot.get("fingerprint", "")) + "\n", encoding="utf-8")

    return {"source_id": source_id, "status": "ROLLBACK", "epistemic_after": epistemic_after}


def emit_summary(manifest: dict[str, Any]) -> str:
    lines = ["source_id\tepistemic_state\tlast_action\tlast_run_utc"]
    for source_id, entry in sorted(manifest.get("sources", {}).items()):
        lines.append(f"{source_id}\t{entry.get('epistemic_state', 'TOKEN_VAZIO')}\t{entry.get('last_action', 'TOKEN_VAZIO')}\t{entry.get('last_run_utc', '')}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--source", type=str, default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--emit-summary", action="store_true")
    parser.add_argument("--rollback", action="store_true")
    parser.add_argument("--rollback-all", action="store_true")
    parser.add_argument("--checkpoint", type=str, default="latest", help="Only 'latest' is supported (single failsafe snapshot per source).")
    args = parser.parse_args(argv)

    config = load_config(args.config)
    schema = load_event_schema()
    manifest = load_manifest()

    sources = real_sources(config)
    if args.source:
        sources = [s for s in sources if s["id"] == args.source]
        if not sources:
            raise SystemExit(f"unknown source id: {args.source}")
    elif args.rollback and not args.rollback_all and not args.source:
        raise SystemExit("--rollback requires --source or --rollback-all")

    if args.rollback:
        results = [rollback_one(source, schema, manifest, dry_run=args.dry_run) for source in sources]
    else:
        results = [watch_one(source, schema, manifest, dry_run=args.dry_run) for source in sources]

    write_manifest(manifest, dry_run=args.dry_run)

    for result in results:
        print(f"[{result['source_id']}] {result['status']}")

    if args.emit_summary:
        print()
        print(emit_summary(manifest))

    failed_all = bool(results) and all(r["status"] in {"FAILSAFE", "no_checkpoint_to_rollback_to"} for r in results)
    if failed_all and not args.rollback:
        event = {
            "timestamp_utc": utc_now(),
            "source_id": "ALL",
            "action": "ALL_SOURCES_FAILED",
            "schema_drift": False,
            "epistemic_before": "—",
            "epistemic_after": "—",
            "fingerprint_before": "",
            "fingerprint_after": "",
            "artifact_path": "",
            "rll_paths_affected": [],
            "notes": "every requested source resolved to FAILSAFE in this run",
        }
        append_trail_event(event, schema, dry_run=args.dry_run)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
