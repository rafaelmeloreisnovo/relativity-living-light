#!/usr/bin/env python3
"""Run all RLL real observational seed validations v0.

This is an orchestrator for seed-level validation only.
It keeps claim_allowed=false globally.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

SCRIPTS = [
    "scripts/validation/validate_compact_remnant_boundary.py",
    "scripts/validation/validate_dark_lens_candidates.py",
    "scripts/validation/validate_wandering_bh_candidates.py",
    "scripts/validation/validate_historical_impulse_candidates.py",
    "scripts/validation/validate_high_z_smbh_seeds.py",
    "scripts/validation/validate_residual_gravity_structures.py",
]

EXPECTED_OUTPUTS = [
    "data/results/compact_objects/remnant_boundary_validation.json",
    "data/results/compact_objects/wandering_bh_validation.json",
    "data/results/compact_objects/wandering_bh_source_readiness.json",
    "data/results/kinematics/historical_impulse_validation.json",
    "data/results/high_z_smbh/seed_validation.json",
    "data/results/structure/residual_gravity_validation.json",
]

OUT = Path("data/results/bootstrap/real_seed_validation_index.json")
REPORT = Path("docs/science/REAL_SEED_VALIDATION_V0_INDEX.md")


def main() -> int:
    results = []
    for script in SCRIPTS:
        proc = subprocess.run([sys.executable, script], text=True, capture_output=True)
        results.append(
            {
                "script": script,
                "returncode": proc.returncode,
                "stdout": proc.stdout.strip(),
                "stderr": proc.stderr.strip(),
            }
        )
        if proc.returncode != 0:
            print(proc.stdout)
            print(proc.stderr, file=sys.stderr)
            return proc.returncode

    output_status = []
    for path_str in EXPECTED_OUTPUTS:
        path = Path(path_str)
        if path.exists():
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
                output_status.append(
                    {
                        "path": path_str,
                        "exists": True,
                        "module": data.get("module"),
                        "status": data.get("status"),
                        "claim_allowed": bool(data.get("claim_allowed")),
                    }
                )
            except Exception as exc:
                output_status.append({"path": path_str, "exists": True, "parse_error": str(exc), "claim_allowed": False})
        else:
            output_status.append({"path": path_str, "exists": False, "claim_allowed": False})

    payload = {
        "schema_version": "0.1",
        "status": "real_seed_validation_v0_complete",
        "claim_allowed": False,
        "scripts": results,
        "outputs": output_status,
        "safe_conclusion": "seed-level calculations were produced; no final scientific validation claim is allowed yet",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    report_lines = [
        "# Real Seed Validation v0 Index",
        "",
        "Status: generated seed-validation index",
        "",
        "> These outputs are seed-level calculations only. They do not validate final scientific claims.",
        "",
        "| Output | Module | Status | Claim allowed |",
        "|---|---|---|---:|",
    ]
    for item in output_status:
        report_lines.append(
            f"| `{item.get('path')}` | `{item.get('module', 'TOKEN_VAZIO')}` | `{item.get('status', 'missing')}` | `{str(item.get('claim_allowed', False)).lower()}` |"
        )
    report_lines.extend(
        [
            "",
            "## Safe conclusion",
            "",
            "The repository now has first-pass calculations for each real observational seed module, but raw catalogs, checksums, posterior files, full error models, and baseline comparisons are still required.",
            "",
        ]
    )
    REPORT.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"wrote {OUT}")
    print(f"wrote {REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
