#!/usr/bin/env python3
"""Validate the RLL-LATENTES catalog and optional example fixtures."""

from __future__ import annotations

import argparse
from pathlib import Path

from rll.latentes import DEFAULT_CATALOG, DEFAULT_SCHEMA, validate_catalog


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--invalid-example", type=Path, default=Path("data/rll_latentes/examples/invalid_missing_falsifier.yml"))
    return parser


def main() -> int:
    args = build_parser().parse_args()
    payload = validate_catalog(args.catalog, args.schema)
    invalid_rejected = False
    if args.invalid_example.exists():
        try:
            validate_catalog(args.invalid_example, args.schema)
        except Exception:
            invalid_rejected = True
        else:
            raise SystemExit(f"Invalid example unexpectedly passed: {args.invalid_example}")
    print(
        f"OK: catalog={args.catalog} sources={len(payload['sources'])} "
        f"future_steps={len(payload['future_steps'])} invalid_rejected={invalid_rejected}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
