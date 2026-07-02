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

BASE_DIR = Path(__file__).resolve().parents[1]
RESULTS_DIR = BASE_DIR / "results" / "structure_d"
DEFAULT_SEEDS = tuple(range(1, 11))
DEFAULT_MAXITER = 100
DEFAULT_PREFIX = "joint_real_likelihood"
CANONICAL_STEM = "joint_real_likelihood"
EXISTING_OUTPUT_POLICIES = {"fail", "suffix", "skip"}


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


def command_for_stem(stem: str) -> str:
    return "python scripts/run_structure_d_joint_likelihood.py --output-stem " + validate_output_stem(stem)


def build_plan(seeds: Iterable[int], maxiter: int, prefix: str = DEFAULT_PREFIX) -> list[dict[str, object]]:
    plan = []
    for seed in seeds:
        output_stem = build_output_stem(int(seed), int(maxiter), prefix)
        plan.append(
            {
                "seed": int(seed),
                "maxiter": int(maxiter),
                "output_stem": output_stem,
                "command": command_for_stem(output_stem),
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


def planned_output_paths(stem: str, results_dir: Path = RESULTS_DIR) -> list[Path]:
    stem = validate_output_stem(stem)
    return [
        results_dir / f"{stem}.csv",
        results_dir / f"{stem}.json",
        results_dir / f"{stem}_covariance_manifest.json",
    ]


def detect_existing_outputs(plan: list[dict[str, object]], results_dir: Path = RESULTS_DIR) -> dict[str, list[str]]:
    conflicts: dict[str, list[str]] = {}
    for item in plan:
        stem = str(item["output_stem"])
        existing = [str(path) for path in planned_output_paths(stem, results_dir) if path.exists()]
        if existing:
            conflicts[stem] = existing
    return conflicts


def _next_failover_stem(stem: str, used: set[str], results_dir: Path) -> str:
    stem = validate_output_stem(stem)
    for index in range(1, 1000):
        candidate = validate_output_stem(f"{stem}_failover_{index}")
        if candidate in used:
            continue
        if not any(path.exists() for path in planned_output_paths(candidate, results_dir)):
            used.add(candidate)
            return candidate
    raise ValueError(f"could not allocate failover stem for {stem}")


def apply_existing_output_policy(
    plan: list[dict[str, object]],
    policy: str,
    results_dir: Path = RESULTS_DIR,
) -> tuple[list[dict[str, object]], list[dict[str, object]], dict[str, list[str]]]:
    if policy not in EXISTING_OUTPUT_POLICIES:
        raise ValueError(f"unknown existing output policy: {policy}")
    validate_plan(plan)
    conflicts = detect_existing_outputs(plan, results_dir)
    if not conflicts:
        return plan, [], conflicts
    if policy == "fail":
        raise ValueError(f"planned outputs already exist: {sorted(conflicts)}")

    resolved: list[dict[str, object]] = []
    actions: list[dict[str, object]] = []
    used = {str(item["output_stem"]) for item in plan}
    for item in plan:
        stem = str(item["output_stem"])
        if stem not in conflicts:
            resolved.append(item)
            continue
        if policy == "skip":
            actions.append({"action": "skip_existing", "original_output_stem": stem, "existing_outputs": conflicts[stem]})
            continue
        failover_stem = _next_failover_stem(stem, used, results_dir)
        updated = dict(item)
        updated["output_stem"] = failover_stem
        updated["command"] = command_for_stem(failover_stem)
        resolved.append(updated)
        actions.append(
            {
                "action": "suffix_failover",
                "original_output_stem": stem,
                "resolved_output_stem": failover_stem,
                "existing_outputs": conflicts[stem],
            }
        )
    if not resolved:
        raise ValueError("existing-output policy skipped all planned runs")
    validate_plan(resolved)
    return resolved, actions, conflicts


def build_watchdog(
    plan: list[dict[str, object]],
    mode: str,
    existing_output_policy: str = "fail",
    failover_actions: list[dict[str, object]] | None = None,
    existing_output_conflicts: dict[str, list[str]] | None = None,
) -> dict[str, object]:
    stems = [str(item["output_stem"]) for item in plan]
    return {
        "schema": "rll.structure_d.robust_fit_matrix_watchdog.v2",
        "mode": mode,
        "overall_status": "pass",
        "dry_run_default": mode == "dry_run",
        "execute_requires_explicit_flag": True,
        "unique_output_stems": len(stems) == len(set(stems)),
        "canonical_stem_blocked": CANONICAL_STEM not in stems,
        "existing_output_policy": existing_output_policy,
        "existing_output_conflicts": existing_output_conflicts or {},
        "failover_actions": failover_actions or [],
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
    parser.add_argument(
        "--existing-output-policy",
        choices=sorted(EXISTING_OUTPUT_POLICIES),
        default="fail",
        help="What to do when planned output files already exist: fail, suffix, or skip.",
    )
    parser.add_argument("--plan-output", type=Path, default=None, help="Optional JSON path for the generated plan/result.")
    args = parser.parse_args(argv)

    raw_plan = build_plan(parse_seeds(args.seeds), args.maxiter, args.prefix)
    plan, failover_actions, existing_conflicts = apply_existing_output_policy(raw_plan, args.existing_output_policy)
    mode = "execute" if args.execute else "dry_run"
    watchdog = build_watchdog(plan, mode, args.existing_output_policy, failover_actions, existing_conflicts)
    payload = {
        "schema": "rll.structure_d.robust_fit_matrix_plan.v3",
        "mode": mode,
        "claim_boundary": "Versioned robust-fit execution planning only; this does not validate RLL or promote scientific claims.",
        "failsafe": {
            "dry_run_default": True,
            "execute_requires_explicit_flag": True,
            "canonical_stem_blocked": watchdog["canonical_stem_blocked"],
            "unique_output_stems": watchdog["unique_output_stems"],
            "existing_output_policy": args.existing_output_policy,
            "failover_available": args.existing_output_policy in {"suffix", "skip"},
            "atomic_plan_output": args.plan_output is not None,
        },
        "watchdog": watchdog,
        "runs": execute_plan(plan) if args.execute else plan,
    }
    if args.plan_output is not None:
        text_without_write = json.dumps(payload, indent=2, sort_keys=True) + "\n"
        payload["plan_output_write"] = atomic_write_text(args.plan_output, text_without_write)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.plan_output is not None:
        args.plan_output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
