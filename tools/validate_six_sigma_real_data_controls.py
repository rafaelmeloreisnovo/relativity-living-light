#!/usr/bin/env python3
"""Validate lightweight Six Sigma / DMAIC real-data control coverage.

This gate is intentionally narrow: it verifies that the operational control
spine exists and that required governance terms remain discoverable in the
controlled documents/workflow. It does not run scientific validation and does
not declare RLL validated.
"""

from __future__ import annotations

from pathlib import Path

REQUIRED_FILES = [
    Path("docs/operations/SIX_SIGMA_REAL_DATA_OPERATING_SYSTEM.md"),
    Path("docs/real_data/REAL_DATA_REQUIRED_INPUTS.md"),
    Path(".github/workflows/real-data-complete-execution.yml"),
    Path("docs/RLL_TRACEABILITY_MAP.md"),
]

REQUIRED_TERMS = [
    "DMAIC",
    "claim boundary",
    "checksum",
    "strict_real_data",
    "commit_light_artifacts",
    "baseline",
    "artifact",
    "No superiority claim unless real-data metrics pass predefined thresholds",
]


def main() -> int:
    missing_files = [str(path) for path in REQUIRED_FILES if not path.is_file()]
    if missing_files:
        print("Six Sigma real-data control check FAILED: missing required files")
        for path in missing_files:
            print(f"- {path}")
        return 1

    corpus_parts: list[str] = []
    for path in REQUIRED_FILES:
        corpus_parts.append(path.read_text(encoding="utf-8", errors="replace"))
    corpus = "\n".join(corpus_parts)
    corpus_casefold = corpus.casefold()

    missing_terms = [term for term in REQUIRED_TERMS if term.casefold() not in corpus_casefold]
    if missing_terms:
        print("Six Sigma real-data control check FAILED: missing required terms")
        for term in missing_terms:
            print(f"- {term}")
        return 1

    print("OK: Six Sigma / DMAIC real-data control files and terms are present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
