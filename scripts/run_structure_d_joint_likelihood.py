#!/usr/bin/env python3
"""Safe runner for Structure-D joint real likelihood outputs.

This wrapper exists to prevent robust-fit runs from accidentally overwriting the
canonical smoke artifacts produced by data/pipelines/structure_d/joint_real_likelihood.py.
It does not alter data, model equations, parameter bounds, or claim policy.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from data.pipelines.structure_d.joint_real_likelihood import run_joint_likelihood

DEFAULT_OUTPUT_STEM = "joint_real_likelihood"
OUTPUT_STEM_ENV = "STRUCTURE_D_JOINT_OUTPUT_STEM"


def validate_output_stem(value: str) -> str:
    """Return a safe file stem under results/structure_d.

    The stem is intentionally restricted to a single filename component. This
    prevents path traversal and avoids writing outside the canonical results
    directory. Future ablation subdirectories should use a dedicated, reviewed
    runner rather than passing slashes through this variable.
    """

    stem = str(value).strip()
    if not stem:
        raise ValueError("output stem must not be empty")
    if stem in {".", ".."} or "/" in stem or "\\" in stem:
        raise ValueError("output stem must be a filename stem, not a path")
    if ".." in Path(stem).parts:
        raise ValueError("output stem must not contain path traversal")
    if stem.endswith((".json", ".csv", ".tsv")):
        raise ValueError("output stem must not include a file extension")
    return stem


def resolve_output_stem(cli_output_stem: str | None = None) -> str:
    """Resolve CLI > environment > canonical default output stem."""

    if cli_output_stem is not None:
        return validate_output_stem(cli_output_stem)
    return validate_output_stem(os.environ.get(OUTPUT_STEM_ENV, DEFAULT_OUTPUT_STEM))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run Structure-D joint likelihood with a safe, versioned output stem."
    )
    parser.add_argument(
        "--output-stem",
        default=None,
        help=(
            "Filename stem for results/structure_d outputs. Overrides "
            f"{OUTPUT_STEM_ENV}. Must not contain slashes or extensions."
        ),
    )
    return parser


def main(argv: list[str] | None = None) -> dict:
    args = build_parser().parse_args(argv)
    output_stem = resolve_output_stem(args.output_stem)
    payload = run_joint_likelihood(output_stem=output_stem)
    print(pd.DataFrame(payload["rows"]).to_string(index=False))
    for output in payload["outputs"]:
        print(f"Wrote: {output['path']}")
    return payload


if __name__ == "__main__":
    main()
