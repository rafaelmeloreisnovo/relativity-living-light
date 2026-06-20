#!/usr/bin/env python3
"""Check RLL reports against the machine claim status.

If the evidence scan says CLAIM_BLOCKED, generated reports must not contain
unqualified superiority/proof language. This is deliberately conservative and is
intended for final/generated reports, not for historical documents.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCAN = ROOT / "results" / "audit" / "rll_model_evidence_scan.json"

UNSAFE_WHEN_BLOCKED = [
    r"\bRLL\s+vence\b",
    r"\bRLL\s+é\s+favorecido\b",
    r"\bRLL\s+esta\s+favorecido\b",
    r"\bRLL\s+está\s+favorecido\b",
    r"\bRLL\s+prova\b",
    r"\bRLL\s+comprova\b",
    r"\bRLL\s+faz\s+melhor\b",
    r"\bRLL\s+faz\s+bem\s+aos\s+dados\b",
    r"\bRLL\s+supera\s+CPL\b",
    r"\bRLL\s+supera\s+LCDM\b",
    r"\bRLL\s+confirma\b",
    r"\bRLL\s+is\s+favou?red\b",
    r"\bRLL\s+wins\b",
    r"\bRLL\s+proves\b",
    r"\bRLL\s+outperforms\b",
]


def load_scan(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"FAIL: scan JSON not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"FAIL: invalid scan JSON: {path}: {exc}") from exc


def strip_code_blocks(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


def check_report(scan: dict[str, Any], report_path: Path) -> list[str]:
    text = report_path.read_text(encoding="utf-8")
    text_no_code = strip_code_blocks(text)
    claim_status = scan.get("claim_status")
    hits: list[str] = []
    if claim_status == "CLAIM_BLOCKED":
        for pattern in UNSAFE_WHEN_BLOCKED:
            if re.search(pattern, text_no_code, flags=re.IGNORECASE):
                hits.append(pattern)
    return hits


def main() -> None:
    parser = argparse.ArgumentParser(description="Check RLL report wording against evidence scan claim_status.")
    parser.add_argument("reports", nargs="+", type=Path, help="Markdown reports to check")
    parser.add_argument("--scan", type=Path, default=DEFAULT_SCAN)
    args = parser.parse_args()

    scan = load_scan(args.scan)
    failed = False
    for report in args.reports:
        if not report.exists():
            print(f"FAIL: report not found: {report}", file=sys.stderr)
            failed = True
            continue
        hits = check_report(scan, report)
        if hits:
            failed = True
            print(f"FAIL: unsafe claim wording in {report} while claim_status={scan.get('claim_status')}", file=sys.stderr)
            for hit in hits:
                print(f"  pattern: {hit}", file=sys.stderr)
        else:
            print(f"PASS: {report} respects claim_status={scan.get('claim_status')}")

    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
