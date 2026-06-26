#!/usr/bin/env python3
"""Scan RLL real-data bootstrap ledgers.

This script does not validate scientific claims.
It checks whether required real-data ledgers exist, whether TOKEN_VAZIO/null
placeholders remain, and whether local paths/checksums are present when required.

Outputs:
- data/results/bootstrap/real_data_bootstrap_summary.json
- data/results/bootstrap/real_data_bootstrap_ledger.tsv
- docs/science/REAL_DATA_BOOTSTRAP_SCAN_REPORT.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

try:
    import yaml
except Exception as exc:  # pragma: no cover
    print(f"ERROR: PyYAML is required: {exc}", file=sys.stderr)
    sys.exit(2)

TOKEN_MARKERS = {"TOKEN_VAZIO", "LACUNA", "BLOQUEADO", "NOT_MEASURED", "UNKNOWN"}


@dataclass
class LedgerStatus:
    module_id: str
    ledger_path: str
    exists: bool
    parse_ok: bool
    token_vazio_count: int
    null_count: int
    local_path_missing_count: int
    checksum_missing_count: int
    status: str
    claim_allowed: bool
    notes: str


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def walk_values(obj: Any):
    if isinstance(obj, dict):
        for value in obj.values():
            yield from walk_values(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from walk_values(value)
    else:
        yield obj


def count_token_vazio(obj: Any) -> int:
    count = 0
    for value in walk_values(obj):
        if isinstance(value, str):
            upper = value.strip().upper()
            if any(marker in upper for marker in TOKEN_MARKERS):
                count += 1
    return count


def count_null(obj: Any) -> int:
    return sum(1 for value in walk_values(obj) if value is None)


def collect_records(obj: Any) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    if isinstance(obj, dict):
        if isinstance(obj.get("source_records"), list):
            records.extend([r for r in obj["source_records"] if isinstance(r, dict)])
        if isinstance(obj.get("modules"), list):
            records.extend([r for r in obj["modules"] if isinstance(r, dict)])
    return records


def scan_ledger(repo: Path, module_id: str, ledger_rel: str) -> LedgerStatus:
    path = repo / ledger_rel
    if not path.exists():
        return LedgerStatus(
            module_id=module_id,
            ledger_path=ledger_rel,
            exists=False,
            parse_ok=False,
            token_vazio_count=0,
            null_count=0,
            local_path_missing_count=0,
            checksum_missing_count=0,
            status="missing_ledger",
            claim_allowed=False,
            notes="required ledger path does not exist",
        )

    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return LedgerStatus(
            module_id=module_id,
            ledger_path=ledger_rel,
            exists=True,
            parse_ok=False,
            token_vazio_count=0,
            null_count=0,
            local_path_missing_count=0,
            checksum_missing_count=0,
            status="schema_error",
            claim_allowed=False,
            notes=f"YAML parse error: {exc}",
        )

    token_count = count_token_vazio(data)
    nulls = count_null(data)
    records = collect_records(data)

    missing_local = 0
    missing_checksum = 0
    for record in records:
        local_path = record.get("local_path")
        checksum = record.get("checksum_sha256")
        raw_available = bool(record.get("raw_data_available"))
        if raw_available and (not local_path or "TOKEN_VAZIO" in str(local_path)):
            missing_local += 1
        if raw_available and (not checksum or "TOKEN_VAZIO" in str(checksum)):
            missing_checksum += 1

    claim_allowed = bool(isinstance(data, dict) and data.get("claim_allowed") is True)
    if token_count or nulls or missing_local or missing_checksum:
        status = "blocked"
        claim_allowed = False
    else:
        status = "metadata_ready"

    return LedgerStatus(
        module_id=module_id,
        ledger_path=ledger_rel,
        exists=True,
        parse_ok=True,
        token_vazio_count=token_count,
        null_count=nulls,
        local_path_missing_count=missing_local,
        checksum_missing_count=missing_checksum,
        status=status,
        claim_allowed=claim_allowed,
        notes="claim remains blocked unless real data, checksum, metric, baseline, and error model are complete",
    )


def write_outputs(repo: Path, statuses: list[LedgerStatus]) -> None:
    out_dir = repo / "data/results/bootstrap"
    out_dir.mkdir(parents=True, exist_ok=True)

    summary = {
        "schema_version": "0.1",
        "claim_allowed": False,
        "total_ledgers": len(statuses),
        "missing_ledgers": sum(1 for s in statuses if not s.exists),
        "blocked_ledgers": sum(1 for s in statuses if s.status == "blocked"),
        "metadata_ready_ledgers": sum(1 for s in statuses if s.status == "metadata_ready"),
        "statuses": [asdict(s) for s in statuses],
        "safe_conclusion": "validation readiness only; no scientific claim allowed from incomplete ledgers",
    }
    (out_dir / "real_data_bootstrap_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    tsv_lines = [
        "module_id\tledger_path\texists\tparse_ok\ttoken_vazio_count\tnull_count\tlocal_path_missing_count\tchecksum_missing_count\tstatus\tclaim_allowed\tnotes"
    ]
    for s in statuses:
        tsv_lines.append(
            "\t".join(
                [
                    s.module_id,
                    s.ledger_path,
                    str(s.exists).lower(),
                    str(s.parse_ok).lower(),
                    str(s.token_vazio_count),
                    str(s.null_count),
                    str(s.local_path_missing_count),
                    str(s.checksum_missing_count),
                    s.status,
                    str(s.claim_allowed).lower(),
                    s.notes.replace("\t", " ").replace("\n", " "),
                ]
            )
        )
    (out_dir / "real_data_bootstrap_ledger.tsv").write_text("\n".join(tsv_lines) + "\n", encoding="utf-8")

    report = [
        "# Real Data Bootstrap Scan Report",
        "",
        "Status: generated validation-readiness report",
        "",
        "> This artifact does not validate any scientific claim. It only reports whether the required real-data ledgers are ready for validation.",
        "",
        "| Module | Ledger | Status | TOKEN_VAZIO | Nulls | Claim allowed |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for s in statuses:
        report.append(
            f"| `{s.module_id}` | `{s.ledger_path}` | `{s.status}` | {s.token_vazio_count} | {s.null_count} | `{str(s.claim_allowed).lower()}` |"
        )
    report.extend(
        [
            "",
            "## Safe conclusion",
            "",
            "No superiority, discovery, or validation claim is allowed while ledgers contain TOKEN_VAZIO, null fields, missing checksums, missing metrics, or missing baselines.",
            "",
        ]
    )
    (repo / "docs/science/REAL_DATA_BOOTSTRAP_SCAN_REPORT.md").write_text("\n".join(report), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".", help="Repository root")
    parser.add_argument(
        "--requirements",
        default="data/real/bootstrap/real_data_requirements_bootstrap.yml",
        help="Bootstrap requirements YAML",
    )
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    req_path = repo / args.requirements
    if not req_path.exists():
        print(f"ERROR: requirements file not found: {req_path}", file=sys.stderr)
        return 1

    req = yaml.safe_load(req_path.read_text(encoding="utf-8"))
    modules = req.get("modules", []) if isinstance(req, dict) else []

    statuses: list[LedgerStatus] = []
    for module in modules:
        if not isinstance(module, dict):
            continue
        module_id = str(module.get("id", "TOKEN_VAZIO_MODULE"))
        for ledger in module.get("required_ledgers", []) or []:
            statuses.append(scan_ledger(repo, module_id, str(ledger)))

    write_outputs(repo, statuses)

    # Fail closed only on parse errors/missing required file; TOKEN_VAZIO is expected in bootstrap.
    hard_fail = any(s.status in {"schema_error", "missing_ledger"} for s in statuses)
    return 1 if hard_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
