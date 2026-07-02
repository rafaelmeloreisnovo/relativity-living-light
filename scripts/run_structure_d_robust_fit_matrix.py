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
    return [
        {
            "seed": int(seed),
            "maxiter": int(maxiter),
            "output_stem": build_output_stem(int(seed), int(maxiter), prefix),
            "command": "python scripts/run_structure_d_joint_likelihood.py --output-stem "
            + build_output_stem(int(seed), int(maxiter), prefix),
        }
        for seed in seeds
    ]


def execute_plan(plan: list[dict[str, object]]) -> list[dict[str, object]]:
    from scripts.run_structure_d_joint_likelihood import main as run_once

    completed = []
    for item in plan:
        os.environ["STRUCTURE_D_JOINT_SEED"] = str(item["seed"])
        os.environ["STRUCTURE_D_JOINT_MAXITER"] = str(item["maxiter"])
        payload = run_once(["--output-stem", str(item["output_stem"])])
        completed.append({"seed": item["seed"], "maxiter": item["maxiter"], "output_stem": item["output_stem"], "outputs": payload.get("outputs", [])})
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
    payload = {
        "schema": "rll.structure_d.robust_fit_matrix_plan.v1",
        "mode": "execute" if args.execute else "dry_run",
        "claim_boundary": "Versioned robust-fit execution planning only; this does not validate RLL or promote scientific claims.",
        "runs": execute_plan(plan) if args.execute else plan,
    }
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.plan_output is not None:
        args.plan_output.parent.mkdir(parents=True, exist_ok=True)
        args.plan_output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
