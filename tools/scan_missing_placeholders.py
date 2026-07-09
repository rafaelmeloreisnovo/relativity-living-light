#!/usr/bin/env python3
"""Scan tracked text files for placeholders, stubs, gaps, aborted work and forgotten markers.

The scanner is intentionally conservative: it does not modify source files and it
never treats a marker as proof of a bug. It emits a ledger so humans and CI can
see which gaps are explicit, which are claim-blocking, and which need a concrete
artifact before being resolved.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path

TEXT_EXTENSIONS = {
    ".md", ".txt", ".py", ".sh", ".yml", ".yaml", ".json", ".csv", ".tsv",
    ".toml", ".ini", ".cfg", ".c", ".h", ".cpp", ".hpp", ".rs", ".js", ".ts",
}

DEFAULT_EXCLUDE_PARTS = {
    ".git", "node_modules", ".venv", "venv", "__pycache__", ".pytest_cache",
    "data/raw", "data/cache", "artifacts",
}

PATTERNS: dict[str, re.Pattern[str]] = {
    "token_vazio": re.compile(r"\bTOKEN[_ -]?VAZIO\b", re.IGNORECASE),
    "placeholder": re.compile(r"\bplaceholder\b|\bmock\b|\bdummy\b", re.IGNORECASE),
    "stub": re.compile(r"\bstub\b|\bpass\s*(#.*)?$|NotImplemented", re.IGNORECASE),
    "todo_fixme": re.compile(r"\bTODO\b|\bFIXME\b|\bXXX\b", re.IGNORECASE),
    "missing_absence": re.compile(r"\bmissing\b|\baus[eê]ncia\b|\bfalta\b|\bsem\s+", re.IGNORECASE),
    "aborted_forgotten": re.compile(r"\babortad[oa]s?\b|\besquecid[oa]s?\b|\bdeixad[oa]s?\b|\bskipped\b", re.IGNORECASE),
    "claim_block": re.compile(r"claim_allowed\s*[:=]\s*false|claim[_ -]?blocked|\bBLOQUEADO\b", re.IGNORECASE),
}

CLAIM_BLOCKING_HINTS = re.compile(
    r"claim_allowed\s*[:=]\s*false|checksum|sha256|raw_data|baseline|uncertainty|covariance|CLASS|CAMB|MCMC|nested|Pantheon|DESI|Planck|f_sigma8|fσ8",
    re.IGNORECASE,
)


@dataclass
class Finding:
    path: str
    line: int
    kind: str
    severity: str
    text: str
    next_action: str


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def tracked_files(root: Path) -> list[str]:
    raw = subprocess.check_output(["git", "ls-files", "-z"], cwd=root)
    return [p.decode("utf-8", errors="surrogateescape") for p in raw.split(b"\0") if p]


def excluded(rel: str) -> bool:
    parts = rel.split("/")
    prefixes = {"/".join(parts[:i]) for i in range(1, len(parts) + 1)}
    return any(part in DEFAULT_EXCLUDE_PARTS or part in prefixes for part in parts)


def severity_for(kind: str, line_text: str) -> str:
    if kind in {"claim_block", "token_vazio"}:
        return "claim_blocking"
    if CLAIM_BLOCKING_HINTS.search(line_text):
        return "claim_relevant"
    if kind in {"placeholder", "stub", "aborted_forgotten"}:
        return "implementation_gap"
    return "review_needed"


def next_action_for(kind: str, severity: str) -> str:
    if severity == "claim_blocking":
        return "Keep claim_allowed=false; resolve only with source, artifact, baseline and checksum."
    if kind == "stub":
        return "Replace stub with executable implementation or mark explicit TOKEN_VAZIO with owner/next test."
    if kind == "placeholder":
        return "Replace placeholder/mock/dummy with real fixture or mark as example-only."
    if kind == "todo_fixme":
        return "Convert TODO/FIXME into issue, ledger item or executable test."
    if kind == "aborted_forgotten":
        return "Classify as abandoned, blocked, or next-action with artifact target."
    return "Review and classify; avoid silent inference."


def scan_file(root: Path, rel: str, max_line_length: int = 260) -> list[Finding]:
    path = root / rel
    if path.suffix.lower() not in TEXT_EXTENSIONS or excluded(rel):
        return []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return []
    findings: list[Finding] = []
    for idx, line in enumerate(text.splitlines(), start=1):
        clean = line.strip()
        if not clean:
            continue
        for kind, pattern in PATTERNS.items():
            if pattern.search(clean):
                severity = severity_for(kind, clean)
                findings.append(
                    Finding(
                        path=rel,
                        line=idx,
                        kind=kind,
                        severity=severity,
                        text=clean[:max_line_length],
                        next_action=next_action_for(kind, severity),
                    )
                )
                break
    return findings


def write_outputs(root: Path, findings: list[Finding], out_json: Path, out_csv: Path, out_md: Path) -> None:
    out_json.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema": "rll.missing_placeholder_stub_scan.v1",
        "claim_allowed": False,
        "total_findings": len(findings),
        "by_kind": dict(Counter(f.kind for f in findings)),
        "by_severity": dict(Counter(f.severity for f in findings)),
        "top_files": dict(Counter(f.path for f in findings).most_common(40)),
        "findings": [asdict(f) for f in findings],
        "safe_conclusion": "Findings are gap markers, not automatic failures. Claim-relevant findings must remain blocked until resolved by artifacts.",
    }
    out_json.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["path", "line", "kind", "severity", "text", "next_action"])
        writer.writeheader()
        writer.writerows(asdict(f) for f in findings)

    by_severity = Counter(f.severity for f in findings)
    by_kind = Counter(f.kind for f in findings)
    lines = [
        "# Missing / Placeholder / Stub Scan",
        "",
        "Status: diagnostic only",
        "Claim: `claim_allowed=false`",
        "",
        "## Summary",
        "",
        f"- total_findings: `{len(findings)}`",
        f"- by_severity: `{dict(by_severity)}`",
        f"- by_kind: `{dict(by_kind)}`",
        "",
        "## Top files",
        "",
    ]
    for path, count in Counter(f.path for f in findings).most_common(30):
        lines.append(f"- `{path}`: {count}")
    lines.extend([
        "",
        "## Claim boundary",
        "",
        "This scan does not remove gaps. It makes gaps visible and routable.",
        "Any claim-relevant item remains blocked until source, artifact, baseline, uncertainty/error model and checksum are present.",
        "",
    ])
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-json", default="data/results/missing_placeholder_stub_scan.json")
    parser.add_argument("--out-csv", default="data/results/missing_placeholder_stub_scan.csv")
    parser.add_argument("--out-md", default="docs/MISSING_PLACEHOLDER_STUB_SCAN.md")
    parser.add_argument("--max-findings", type=int, default=0, help="Fail if findings exceed this number; 0 disables failure.")
    args = parser.parse_args()

    root = repo_root()
    findings: list[Finding] = []
    for rel in tracked_files(root):
        findings.extend(scan_file(root, rel))

    findings.sort(key=lambda f: (f.severity, f.kind, f.path, f.line))
    write_outputs(root, findings, root / args.out_json, root / args.out_csv, root / args.out_md)
    print(json.dumps({
        "total_findings": len(findings),
        "by_kind": dict(Counter(f.kind for f in findings)),
        "by_severity": dict(Counter(f.severity for f in findings)),
        "claim_allowed": False,
    }, indent=2, ensure_ascii=False))

    if args.max_findings and len(findings) > args.max_findings:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
