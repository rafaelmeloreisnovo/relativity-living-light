#!/usr/bin/env python3
"""Validate RLL watch YAML against JSON Schema."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml

try:
    import jsonschema
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Missing dependency: jsonschema. Install with `pip install jsonschema`.") from exc


def validate_config(config_path: Path, schema_path: Path) -> None:
    with config_path.open("r", encoding="utf-8") as fh:
        payload = yaml.safe_load(fh)

    with schema_path.open("r", encoding="utf-8") as fh:
        schema = json.load(fh)

    jsonschema.validate(instance=payload, schema=schema)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("rll_inovacao_tecnologica_watch.yml"),
        help="Path to watch config YAML",
    )
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path("schemas/rll_watch.schema.json"),
        help="Path to JSON schema",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    validate_config(config_path=args.config, schema_path=args.schema)
    print(f"OK: {args.config} is valid against {args.schema}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
