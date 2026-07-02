#!/usr/bin/env python3
"""Plan or execute Structure-D robust-fit matrix runs with safe output stems.

Default mode is dry-run. Use --execute explicitly to run the likelihood. This
script does not alter model equations, data files, parameter bounds, or claim
policy; it only coordinates versioned output stems for seed/maxiter runs.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Iterable

from scripts.run_structure_d_joint_likelihood import validate_output_stem

DEFAULT_SEEDS = tuple(range(1, 11))
DEFAULT_MAXITER = 100
DEFAULT_PREFIX = "joint_real_likelihood"
CANONICAL_STEM = "joint_real_likelihood"


def parse_seeds(value: str) -> list[int]:
    seeds = [int(item.strip()) for item in value.split(",") if item.strip()]
    if not seeds:
        raise ValueError("at least one seed is required")
    if any(seed <= 0 for seed in seeds):
        raise ValueError("seeds must be positive integers")
    return seeds


def build_output_stem(seed: int, maxiter: int, prefix: str = DEFAULT_PREFIX) -> str:
    if seed <= 0:
        raise ValueError("seed must be positive")
    if maxiter <= 0:
        raise ValueError("maxiter must be positive")
    prefix = validate_output_stem(prefix)
    return validate_output_stem(f"{prefix}_seed_{seed}_maxiter_{maxiter}")


def build_plan(seeds: Iterable[int], maxiter: int, prefix: str = DEFAULT_PREFIX) -> list[dict[str, object]]:
    plan = []
    for seed in seeds:
        output_stem = build_output_stem(int(seed), int(maxiter), prefix)
        plan.append(
            {
                "seed": int(seed),
                "maxiter": int(maxiter),
                "output_stem": output_stem,
                "command": "python scripts/run_structure_d_joint_likelihood.py --output-stem " + output_stem,
            }
        )
    validate_plan(plan)
    return plan


def validate_plan(plan: list[dict[str, object]]) -> None:
    if not plan:
        raise ValueError("robust-fit plan must not be empty")
    stems = [str(item["output_stem"]) for item in plan]
    if len(stems) != len(set(stems)):
        raise ValueError("robust-fit output stems must be unique")
    if CANONICAL_STEM in stems:
        raise ValueError("robust-fit plan must not target the canonical smoke stem")
    for item in plan:
        validate_output_stem(str(item["output_stem"]))
        if int(item["seed"]) <= 0 or int(item["maxiter"]) <= 0:
            raise ValueError("seed and maxiter must remain positive")


def build_watchdog(plan: list[dict[str, object]], mode: str) -> dict[str, object]:
    stems = [str(item["output_stem"]) for item in plan]
    return {
        "schema": "rll.structure_d.robust_fit_matrix_watchdog.v1",
        "mode": mode,
        "overall_status": "pass",
        "dry_run_default": mode == "dry_run",
        "execute_requires_explicit_flag": True,
        "unique_output_stems": len(stems) == len(set(stems)),
        "canonical_stem_blocked": CANONICAL_STEM not in stems,
        "planned_runs": len(plan),
        "rollback_policy": "plan-output uses atomic write with .bak backup; likelihood outputs already use module-level atomic writes",
    }


def atomic_write_text(path: Path, text: str) -> dict[str, object]:
    path.parent.mkdir(parents=True, exist_ok=True)
    backup = path.with_suffix(path.suffix + ".bak")
    tmp = path.with_suffix(path.suffix + f".tmp-{os.getpid()}")
    rollback_available = False
    if path.exists():
        backup.write_bytes(path.read_bytes())
        rollback_available = True
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)
    return {"path": str(path), "backup_path": str(backup) if rollback_available else "", "rollback_available": rollback_available}


def execute_plan(plan: list[dict[str, object]]) -> list[dict[str, object]]:
    validate_plan(plan)
    from scripts.run_structure_d_joint_likelihood import main as run_once

    completed = []
    for item in plan:
        os.environ["STRUCTURE_D_JOINT_SEED"] = str(item["seed"])
        os.environ["STRUCTURE_D_JOINT_MAXITER"] = str(item["maxiter"])
        payload = run_once(["--output-stem", str(item["output_stem"])])
        completed.append(
            {
                "seed": item["seed"],
                "maxiter": item["maxiter"],
                "output_stem": item["output_stem"],
                "outputs": payload.get("outputs", []),
            }
        )
    return completed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Plan or execute robust-fit seed/maxiter runs with safe output stems.")
    parser.add_argument("--seeds", default=",".join(str(seed) for seed in DEFAULT_SEEDS))
    parser.add_argument("--maxiter", type=int, default=DEFAULT_MAXITER)
    parser.add_argument("--prefix", default=DEFAULT_PREFIX)
    parser.add_argument("--execute", action="store_true", help="Run the likelihood; default is dry-run plan only.")
    parser.add_argument("--plan-output", type=Path, default=None, help="Optional JSON path for the generated plan/result.")
    args = parser.parse_args(argv)

    plan = build_plan(parse_seeds(args.seeds), args.maxiter, args.prefix)
    mode = "execute" if args.execute else "dry_run"
    watchdog = build_watchdog(plan, mode)
    payload = {
        "schema": "rll.structure_d.robust_fit_matrix_plan.v2",
        "mode": mode,
        "claim_boundary": "Versioned robust-fit execution planning only; this does not validate RLL or promote scientific claims.",
        "failsafe": {
            "dry_run_default": True,
            "execute_requires_explicit_flag": True,
            "canonical_stem_blocked": watchdog["canonical_stem_blocked"],
            "unique_output_stems": watchdog["unique_output_stems"],
            "atomic_plan_output": args.plan_output is not None,
        },
        "watchdog": watchdog,
        "runs": execute_plan(plan) if args.execute else plan,
    }
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.plan_output is not None:
        payload["plan_output_write"] = atomic_write_text(args.plan_output, text)
        text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
        atomic_write_text(args.plan_output, text)
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
