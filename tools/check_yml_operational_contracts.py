#!/usr/bin/env python3
"""Check YAML/YML operational contracts without promoting scientific claims.

This checker separates syntax from execution semantics:

- workflow YAML executes through GitHub Actions;
- manifest/config/route/ledger/IML YAML is declarative until consumed;
- result/example YAML must not be promoted as empirical validation.

The goal is operational feedback, not theory validation.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_RE = re.compile(r"(?<![A-Za-z0-9_./-])([A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)+\.(?:py|sh))(?![A-Za-z0-9_./-])")
BOUNDARY_RE = re.compile(r"mock|synthetic|sint[eé]tico|placeholder|example|sample|fake|TOKEN_VAZIO|demo", re.I)
CLAIM_TRUE_RE = re.compile(r"claim_allowed\s*:\s*(true|yes|1)", re.I)
FALSIFIER_RE = re.compile(r"falsifier|falsificador|falsifiability|falsificabilidade", re.I)
BASELINE_RE = re.compile(r"baseline|adversary|lcdm|w0wa|cpl|controle|comparador", re.I)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def discover_yml_files() -> list[Path]:
    return sorted(
        p
        for p in [*ROOT.rglob("*.yml"), *ROOT.rglob("*.yaml")]
        if ".git" not in p.parts and "artifacts" not in p.parts and ".venv" not in p.parts
    )


def load_yaml(path: Path) -> tuple[Any | None, str | None]:
    try:
        return yaml.load(path.read_text(encoding="utf-8"), Loader=yaml.BaseLoader), None
    except Exception as exc:  # pragma: no cover - exercised in CI with real files
        return None, str(exc)


def referenced_scripts(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    return sorted({m for m in SCRIPT_RE.findall(text) if "${{" not in m and "$" not in m and "://" not in m})


def classify(path: Path, doc: Any, text: str, scripts: list[str]) -> tuple[str, str]:
    path_s = rel(path)
    lower = path_s.lower()
    name = path.name.lower()

    if path_s.startswith(".github/workflows/"):
        return "workflow", "E3"
    if name.endswith(".iml.yml") or name.endswith(".iml.yaml") or "/iml/" in lower:
        return "iml", "E0"
    if "/examples/" in lower or name.startswith("example") or "invalid_" in name or "valid_minimal" in name:
        return "example", "E0"
    if lower.startswith("data/results/") or lower.startswith("results/"):
        return "result", "E4"
    if "manifest" in lower:
        return "manifest", "E1"
    if "sources" in lower or "ledger" in lower:
        return "ledger", "E1"
    if "route" in lower or "orchestration" in lower or "pipeline" in lower or "validation_paths" in lower:
        return "route", "E2" if scripts else "E1"
    if "schema" in lower:
        return "schema", "E1"
    if scripts:
        return "config", "E2"
    return "config", "E1"


def workflow_issues(path: Path, doc: Any) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(doc, dict):
        return ["workflow document is not a mapping"], warnings

    missing = [key for key in ("name", "on", "jobs") if key not in doc]
    if missing:
        errors.append(f"workflow missing required keys: {missing}")

    jobs = doc.get("jobs") or {}
    if isinstance(jobs, dict):
        for job_name, job in jobs.items():
            if isinstance(job, dict) and "uses" not in job and "timeout-minutes" not in job:
                warnings.append(f"job {job_name!r} missing timeout-minutes")
    else:
        errors.append("workflow jobs block is not a mapping")
    return errors, warnings


def claim_issues(role: str, execution_level: str, text: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    has_claim_true = bool(CLAIM_TRUE_RE.search(text))
    has_boundary_token = bool(BOUNDARY_RE.search(text))
    has_falsifier = bool(FALSIFIER_RE.search(text))
    has_baseline = bool(BASELINE_RE.search(text))

    if has_claim_true and not has_falsifier:
        errors.append("claim_allowed=true without explicit falsifier/falsificability marker")
    if has_claim_true and not has_baseline:
        errors.append("claim_allowed=true without explicit baseline/adversary/comparator marker")
    if role in {"example", "result"} and has_boundary_token and has_claim_true:
        errors.append("boundary/example/result YAML must not set claim_allowed=true")
    if role not in {"workflow", "result"} and execution_level in {"E0", "E1"} and not has_claim_true:
        warnings.append("declarative YAML: metadata/route only; do not treat as executed validation")
    return errors, warnings


def script_issues(role: str, scripts: list[str]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    for script in scripts:
        path = ROOT / script
        if not path.exists():
            if role == "workflow":
                errors.append(f"workflow references missing script: {script}")
            else:
                warnings.append(f"declarative YAML references missing script: {script}")
    return errors, warnings


def analyze_file(path: Path) -> dict[str, Any]:
    doc, parse_error = load_yaml(path)
    text = path.read_text(encoding="utf-8", errors="replace")
    scripts = referenced_scripts(path)
    if parse_error:
        return {
            "path": rel(path),
            "role": "unparsed",
            "execution_level": "E0",
            "scripts": scripts,
            "errors": [f"YAML parse error: {parse_error}"],
            "warnings": [],
            "boundary_terms_present": bool(BOUNDARY_RE.search(text)),
            "claim_allowed_true": bool(CLAIM_TRUE_RE.search(text)),
        }

    role, execution_level = classify(path, doc, text, scripts)
    errors: list[str] = []
    warnings: list[str] = []
    if role == "workflow":
        e, w = workflow_issues(path, doc)
        errors.extend(e)
        warnings.extend(w)
    e, w = script_issues(role, scripts)
    errors.extend(e)
    warnings.extend(w)
    e, w = claim_issues(role, execution_level, text)
    errors.extend(e)
    warnings.extend(w)

    return {
        "path": rel(path),
        "role": role,
        "execution_level": execution_level,
        "scripts": scripts,
        "errors": errors,
        "warnings": warnings,
        "boundary_terms_present": bool(BOUNDARY_RE.search(text)),
        "claim_allowed_true": bool(CLAIM_TRUE_RE.search(text)),
    }


def build_report(items: list[dict[str, Any]]) -> str:
    roles = Counter(item["role"] for item in items)
    levels = Counter(item["execution_level"] for item in items)
    errors = [item for item in items if item["errors"]]
    warnings = [item for item in items if item["warnings"]]

    lines = [
        "# YML Operational Contract Review",
        "",
        "Generated by `tools/check_yml_operational_contracts.py`.",
        "",
        "## Summary",
        "",
        f"- YAML/YML files scanned: `{len(items)}`",
        f"- Files with errors: `{len(errors)}`",
        f"- Files with warnings: `{len(warnings)}`",
        "",
        "## Role counts",
        "",
    ]
    for role, count in sorted(roles.items()):
        lines.append(f"- `{role}`: {count}")
    lines += ["", "## Execution levels", ""]
    for level, count in sorted(levels.items()):
        lines.append(f"- `{level}`: {count}")

    lines += [
        "",
        "## Errors",
        "",
    ]
    if not errors:
        lines.append("- none")
    else:
        for item in errors:
            lines.append(f"- `{item['path']}`")
            for err in item["errors"]:
                lines.append(f"  - ERROR: {err}")

    lines += [
        "",
        "## Warnings",
        "",
    ]
    if not warnings:
        lines.append("- none")
    else:
        for item in warnings[:200]:
            lines.append(f"- `{item['path']}`")
            for warn in item["warnings"]:
                lines.append(f"  - WARN: {warn}")
        if len(warnings) > 200:
            lines.append(f"- truncated: {len(warnings) - 200} additional warning entries")

    lines += [
        "",
        "## Claim boundary rule",
        "",
        "A YAML file is not empirical validation by itself. Execution requires workflow/script, inputs, output artifact, baseline, falsifier, and claim boundary.",
        "",
    ]
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json-out", default="data/results/yml_operational_contracts.json")
    ap.add_argument("--md-out", default="docs/yml/YML_OPERATIONAL_CONTRACT_REVIEW.md")
    ap.add_argument("--write", action="store_true", help="Write JSON/Markdown report files")
    args = ap.parse_args(argv)

    items = [analyze_file(path) for path in discover_yml_files()]
    payload = {
        "schema": "rll.yml_operational_contract_review.v1",
        "scanned": len(items),
        "role_counts": dict(Counter(item["role"] for item in items)),
        "execution_level_counts": dict(Counter(item["execution_level"] for item in items)),
        "errors": sum(len(item["errors"]) for item in items),
        "warnings": sum(len(item["warnings"]) for item in items),
        "items": items,
        "claim_boundary": "YAML existence is not empirical validation; claims require execution, artifact, baseline and falsifier.",
    }

    print(json.dumps({k: payload[k] for k in ("schema", "scanned", "role_counts", "execution_level_counts", "errors", "warnings")}, indent=2, sort_keys=True))

    if args.write:
        json_path = ROOT / args.json_out
        md_path = ROOT / args.md_out
        json_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        md_path.write_text(build_report(items), encoding="utf-8")
        print(f"wrote {json_path.relative_to(ROOT)}")
        print(f"wrote {md_path.relative_to(ROOT)}")

    return 1 if payload["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
