#!/usr/bin/env python3
"""Single-entry YML orchestrator for the RLL repository.

This is intentionally simple for operators:

    python3 tools/yml_orchestrator.py

It runs all relevant YML checks, does not stop at the first failure, writes one
artifact directory, and exits non-zero only after every stage has completed.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT_DIR = ROOT / "artifacts" / "yml-orchestrator"


@dataclass
class StageResult:
    id: str
    title: str
    command: list[str]
    returncode: int
    status: str
    log_path: str
    next_step: str


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def run_stage(stage_id: str, title: str, command: list[str], out_dir: Path, next_step: str) -> StageResult:
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path = out_dir / f"{stage_id}.log"
    completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
    log_path.write_text(
        "# command\n"
        + " ".join(command)
        + "\n\n# stdout\n"
        + completed.stdout
        + "\n\n# stderr\n"
        + completed.stderr,
        encoding="utf-8",
    )
    status = "OK" if completed.returncode == 0 else "FIX"
    return StageResult(
        id=stage_id,
        title=title,
        command=command,
        returncode=completed.returncode,
        status=status,
        log_path=rel(log_path),
        next_step=next_step,
    )


def yaml_parse_command() -> list[str]:
    code = r'''
from pathlib import Path
import hashlib
import sys
import yaml
files = sorted(
    p for p in [*Path('.').rglob('*.yml'), *Path('.').rglob('*.yaml')]
    if '.git/' not in str(p) and 'artifacts/' not in str(p) and '.venv/' not in str(p)
)
failed = 0
for p in files:
    raw = p.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()[:12]
    try:
        list(yaml.safe_load_all(raw.decode('utf-8')))
        print(f'OK   {sha}  {p}')
    except Exception as exc:
        failed += 1
        print(f'FAIL {sha}  {p}  {exc}')
print(f'TOTAL={len(files)} FAILED={failed}')
sys.exit(1 if failed else 0)
'''
    return [sys.executable, "-c", code]


def existing_stage(command: list[str]) -> bool:
    if len(command) >= 2 and command[1].endswith(".py"):
        return (ROOT / command[1]).exists()
    return True


def build_markdown(results: list[StageResult]) -> str:
    ok_count = sum(1 for item in results if item.status == "OK")
    fix_count = sum(1 for item in results if item.status != "OK")
    lines = [
        "# YML Orchestrator Report",
        "",
        f"Generated UTC: `{datetime.now(timezone.utc).isoformat()}`",
        "",
        "## Operator view",
        "",
        f"- OK stages: `{ok_count}`",
        f"- FIX stages: `{fix_count}`",
        "",
        "## Stages",
        "",
        "| Stage | Status | What it means | Log | Next |",
        "|---|---|---|---|---|",
    ]
    for item in results:
        lines.append(
            f"| `{item.id}` | `{item.status}` | {item.title} | `{item.log_path}` | {item.next_step} |"
        )
    lines += [
        "",
        "## Rule",
        "",
        "YML existence is not proof. The orchestrator only tells what is parseable, executable, referenced, missing, or risky.",
        "",
        "## How to use",
        "",
        "```bash",
        "python3 tools/yml_orchestrator.py",
        "```",
        "",
        "Then open:",
        "",
        "```text",
        "artifacts/yml-orchestrator/YML_ORCHESTRATOR_REPORT.md",
        "artifacts/yml-orchestrator/yml_orchestrator_summary.json",
        "```",
        "",
    ]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run all YML checks and produce one operator report.")
    parser.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR), help="Artifact directory")
    args = parser.parse_args(argv)

    out_dir = Path(args.out_dir)
    if not out_dir.is_absolute():
        out_dir = ROOT / out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    stages: list[tuple[str, str, list[str], str]] = [
        (
            "01_parse",
            "Parse every YAML/YML with PyYAML",
            yaml_parse_command(),
            "Fix syntax before any semantic review.",
        ),
        (
            "02_workflows",
            "Audit GitHub workflow isolation",
            [sys.executable, "tools/audit_github_workflows.py", "--strict"],
            "Fix workflow structure, paths, or unsafe coupling.",
        ),
        (
            "03_operational_contracts",
            "Classify YML role, execution level, scripts, claim risk",
            [
                sys.executable,
                "tools/check_yml_operational_contracts.py",
                "--write",
                "--json-out",
                rel(out_dir / "yml_operational_contracts.json"),
                "--md-out",
                rel(out_dir / "YML_OPERATIONAL_CONTRACT_REVIEW.md"),
            ],
            "Treat FIX/BLOCKED items by file family, not one by one manually.",
        ),
        (
            "04_docs_inventory",
            "Check repository documentation inventory if available",
            [sys.executable, "tools/docs_inventory.py", "--check"],
            "Regenerate inventory only if check says it drifted.",
        ),
    ]

    results: list[StageResult] = []
    for stage_id, title, command, next_step in stages:
        if not existing_stage(command):
            skipped = StageResult(
                id=stage_id,
                title=title,
                command=command,
                returncode=0,
                status="SKIP",
                log_path="TOKEN_VAZIO",
                next_step="Tool not present in this checkout.",
            )
            results.append(skipped)
            continue
        print(f"[yml-orchestrator] {stage_id}: {title}")
        result = run_stage(stage_id, title, command, out_dir, next_step)
        print(f"[yml-orchestrator] {stage_id}: {result.status} rc={result.returncode}")
        results.append(result)

    payload = {
        "schema": "rll.yml_orchestrator.v1",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "out_dir": rel(out_dir),
        "summary": {
            "ok": sum(1 for item in results if item.status == "OK"),
            "fix": sum(1 for item in results if item.status == "FIX"),
            "skip": sum(1 for item in results if item.status == "SKIP"),
        },
        "stages": [asdict(item) for item in results],
    }
    (out_dir / "yml_orchestrator_summary.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (out_dir / "YML_ORCHESTRATOR_REPORT.md").write_text(build_markdown(results), encoding="utf-8")

    print(json.dumps(payload["summary"], indent=2, sort_keys=True))
    return 1 if payload["summary"]["fix"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
