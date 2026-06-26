#!/usr/bin/env python3
"""Validate the RLL academic parameter-origin registry.

This gate protects three operational invariants:

1. external academic parameters must cite bibliography keys;
2. RLL authorial parameters must remain separated from literature parameters;
3. fitted/free/nuisance parameters must declare how they affect k, priors,
   covariance policy, or claim boundaries before AIC/AICc/BIC claims.

The script intentionally validates metadata only. It does not edit or read raw
observational datasets.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "inputs" / "cosmology_joint" / "parameter_origin_registry.json"

REQUIRED_TOP_LEVEL = {
    "schema",
    "purpose",
    "claim_policy",
    "no_plagiarism_policy",
    "layers",
    "parameters",
    "bibliography",
    "integration_rules",
    "failsafe",
}

REQUIRED_PARAMETER_FIELDS = {
    "name",
    "model",
    "layer",
    "origin",
    "role",
    "status",
    "reference_keys",
    "notes",
}

AUTHORIAL_RLL_PARAMS = {"Os0", "zt", "wt"}
STANDARD_BASELINES = {"w", "w0", "wa"}
CLAIM_BLOCKING_COVARIANCE_PARAMS = {"SN_covariance", "BAO_covariance", "R_shift"}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def warn(message: str) -> None:
    print(f"WARN: {message}", file=sys.stderr)


def load_registry(path: Path) -> dict[str, Any]:
    if not path.exists():
        fail(f"registry not found: {path}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON: {exc}")
    if not isinstance(data, dict):
        fail("registry root must be a JSON object")
    return data


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def validate_top_level(data: dict[str, Any]) -> None:
    missing = sorted(REQUIRED_TOP_LEVEL - set(data))
    require(not missing, f"missing top-level keys: {missing}")
    require(str(data["schema"]).startswith("rll.parameter_origin_registry."), "schema must identify rll.parameter_origin_registry")
    require(isinstance(data["parameters"], list) and data["parameters"], "parameters must be a non-empty list")
    require(isinstance(data["bibliography"], dict) and data["bibliography"], "bibliography must be a non-empty object")
    require(isinstance(data["integration_rules"], list) and data["integration_rules"], "integration_rules must be a non-empty list")
    failsafe = data.get("failsafe", {})
    require(isinstance(failsafe, dict), "failsafe must be an object")
    require(failsafe.get("raw_datasets_modified") is False, "failsafe.raw_datasets_modified must be false")


def validate_bibliography(data: dict[str, Any]) -> set[str]:
    bib = data["bibliography"]
    for key, entry in bib.items():
        require(isinstance(entry, dict), f"bibliography[{key}] must be an object")
        require(entry.get("type"), f"bibliography[{key}] missing type")
        require(entry.get("title"), f"bibliography[{key}] missing title")
        require(entry.get("used_for"), f"bibliography[{key}] missing used_for")
        if entry.get("type") != "internal_model":
            require(entry.get("authors"), f"bibliography[{key}] missing authors")
            require(entry.get("arxiv") or entry.get("doi"), f"bibliography[{key}] needs arxiv or doi")
    return set(bib)


def validate_parameters(data: dict[str, Any], bib_keys: set[str]) -> None:
    seen: set[str] = set()
    params = data["parameters"]
    for index, param in enumerate(params):
        require(isinstance(param, dict), f"parameter[{index}] must be an object")
        missing = sorted(REQUIRED_PARAMETER_FIELDS - set(param))
        require(not missing, f"parameter[{index}] missing fields: {missing}")

        name = str(param["name"])
        layer = str(param["layer"])
        origin = str(param["origin"])
        status = str(param["status"])
        refs = param["reference_keys"]
        notes = str(param["notes"])

        require(name, f"parameter[{index}] has empty name")
        require(name not in seen, f"duplicate parameter name: {name}")
        seen.add(name)

        require(isinstance(refs, list) and refs, f"{name}: reference_keys must be a non-empty list")
        unknown_refs = sorted(set(refs) - bib_keys)
        require(not unknown_refs, f"{name}: unknown reference_keys: {unknown_refs}")
        require(notes.strip(), f"{name}: notes must be non-empty")

        if layer == "rll_authorial" or name in AUTHORIAL_RLL_PARAMS:
            require(name in AUTHORIAL_RLL_PARAMS, f"unexpected RLL authorial parameter: {name}")
            require(layer == "rll_authorial", f"{name}: authorial RLL params must use layer=rll_authorial")
            require("RLL_internal_ansatz" in refs, f"{name}: authorial params must cite RLL_internal_ansatz")
            require("authorial" in origin.lower() or "rll" in origin.lower(), f"{name}: origin must mark RLL authorship")
            require("must_report_in_k" in status, f"{name}: authorial params must be counted in k")
        else:
            require("RLL_internal_ansatz" not in refs, f"{name}: external parameter must not cite only the RLL internal ansatz")
            require(layer in {"consensus_base", "standard_extension", "observational_nuisance"}, f"{name}: invalid external layer {layer}")

        if name in STANDARD_BASELINES:
            require(layer == "standard_extension", f"{name}: w/w0/wa must be standard_extension")
            require("CPL" in str(param["model"]) or name == "w", f"{name}: baseline dark-energy parameter must identify CPL/wCDM model")

        if name in CLAIM_BLOCKING_COVARIANCE_PARAMS:
            require(layer == "observational_nuisance", f"{name}: covariance/shift blocks must be observational_nuisance")
            require("covariance" in status.lower() or "claim" in status.lower() or "partial" in status.lower(), f"{name}: must declare covariance/claim limitation")

    missing_authorial = sorted(AUTHORIAL_RLL_PARAMS - seen)
    require(not missing_authorial, f"missing authorial RLL params: {missing_authorial}")
    missing_baselines = sorted(STANDARD_BASELINES - seen)
    require(not missing_baselines, f"missing standard dark-energy baselines: {missing_baselines}")


def validate_rules(data: dict[str, Any]) -> None:
    rules_text = "\n".join(map(str, data["integration_rules"])).lower()
    for needle in ["k", "covariance", "rll", "claim", "class", "camb", "pantheon", "desi"]:
        require(needle in rules_text, f"integration_rules must mention {needle}")


def main() -> None:
    data = load_registry(REGISTRY)
    validate_top_level(data)
    bib_keys = validate_bibliography(data)
    validate_parameters(data, bib_keys)
    validate_rules(data)
    print("PASS: academic parameter registry is coherent")
    print(f"PASS: {len(data['parameters'])} parameters validated")
    print(f"PASS: {len(data['bibliography'])} bibliography entries validated")


if __name__ == "__main__":
    main()
