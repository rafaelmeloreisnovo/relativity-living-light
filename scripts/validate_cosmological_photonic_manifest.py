#!/usr/bin/env python3
"""Fail-closed validator for RLL cosmological photonic observation manifests."""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from typing import Any

ALLOWED_CLAIM_STATES = {"EVIDENCE", "COMPUTED", "HYPOTHESIS", "TOKEN_VAZIO", "CONTRADICTION"}
ALLOWED_SPECTRAL_COORDINATES = {"wavelength", "frequency", "energy", "channel"}
ALLOWED_PRODUCT_STATES = {"not_rendered", "calibrated_data", "derived_product", "rendered_image"}
ALLOWED_DARK_STATES = {
    "NOT_APPLICABLE", "AUTHORIAL_HYPOTHESIS", "OBSERVATIONALLY_CONSTRAINED",
    "TOKEN_VAZIO", "CONTRADICTED"
}
SHA256_RE = re.compile(r"^[a-f0-9]{64}$")


class ContractError(ValueError):
    pass


def require(mapping: dict[str, Any], key: str, path: str) -> Any:
    if key not in mapping:
        raise ContractError(f"{path}.{key}: missing required field")
    return mapping[key]


def require_nonempty_string(value: Any, path: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ContractError(f"{path}: expected non-empty string")
    return value


def validate_optional_sha256(value: Any, path: str) -> None:
    if value is not None and (not isinstance(value, str) or not SHA256_RE.fullmatch(value)):
        raise ContractError(f"{path}: expected null or lowercase SHA-256")


def validate_manifest(data: Any) -> None:
    if not isinstance(data, dict):
        raise ContractError("$: expected object")
    if data.get("manifest_version") != "1.0.0":
        raise ContractError("$.manifest_version: expected 1.0.0")

    require_nonempty_string(require(data, "observation_id", "$"), "$.observation_id")
    claim_state = require(data, "claim_state", "$")
    if claim_state not in ALLOWED_CLAIM_STATES:
        raise ContractError("$.claim_state: invalid state")
    claim_allowed = require(data, "claim_allowed", "$")
    if not isinstance(claim_allowed, bool):
        raise ContractError("$.claim_allowed: expected boolean")
    if claim_state in {"HYPOTHESIS", "TOKEN_VAZIO", "CONTRADICTION"} and claim_allowed:
        raise ContractError("$.claim_allowed: must be false for non-evidence states")

    source = require(data, "source_dataset", "$")
    if not isinstance(source, dict):
        raise ContractError("$.source_dataset: expected object")
    for field in ("title", "publisher", "dataset_id", "license", "access_url"):
        require_nonempty_string(require(source, field, "$.source_dataset"), f"$.source_dataset.{field}")
    validate_optional_sha256(source.get("sha256"), "$.source_dataset.sha256")

    spectral = require(data, "spectral_axis", "$")
    if not isinstance(spectral, dict):
        raise ContractError("$.spectral_axis: expected object")
    if require(spectral, "coordinate", "$.spectral_axis") not in ALLOWED_SPECTRAL_COORDINATES:
        raise ContractError("$.spectral_axis.coordinate: invalid coordinate")
    require_nonempty_string(require(spectral, "unit", "$.spectral_axis"), "$.spectral_axis.unit")
    coverage = require(spectral, "coverage", "$.spectral_axis")
    if not isinstance(coverage, dict):
        raise ContractError("$.spectral_axis.coverage: expected object")
    low = require(coverage, "min", "$.spectral_axis.coverage")
    high = require(coverage, "max", "$.spectral_axis.coverage")
    if not isinstance(low, (int, float)) or not isinstance(high, (int, float)) or not low < high:
        raise ContractError("$.spectral_axis.coverage: expected numeric min < max")

    flux = require(data, "flux_axis", "$")
    if not isinstance(flux, dict):
        raise ContractError("$.flux_axis: expected object")
    require_nonempty_string(require(flux, "quantity", "$.flux_axis"), "$.flux_axis.quantity")
    require_nonempty_string(require(flux, "unit", "$.flux_axis"), "$.flux_axis.unit")

    instrument = require(data, "instrument", "$")
    if not isinstance(instrument, dict):
        raise ContractError("$.instrument: expected object")
    for field in ("facility", "instrument", "detector", "response_reference"):
        require_nonempty_string(require(instrument, field, "$.instrument"), f"$.instrument.{field}")

    for section, fields in {
        "calibration": ("pipeline", "version", "background_subtraction"),
        "uncertainty": ("statistical", "systematic", "covariance"),
        "quality": ("mask", "upper_limits", "saturation"),
    }.items():
        value = require(data, section, "$")
        if not isinstance(value, dict):
            raise ContractError(f"$.{section}: expected object")
        for field in fields:
            require_nonempty_string(require(value, field, f"$.{section}"), f"$.{section}.{field}")

    visualization = require(data, "visualization", "$")
    if not isinstance(visualization, dict):
        raise ContractError("$.visualization: expected object")
    product_state = require(visualization, "product_state", "$.visualization")
    if product_state not in ALLOWED_PRODUCT_STATES:
        raise ContractError("$.visualization.product_state: invalid state")
    for field in ("normalization", "transfer_function", "color_space"):
        require_nonempty_string(require(visualization, field, "$.visualization"), f"$.visualization.{field}")
    channel_mapping = require(visualization, "channel_mapping", "$.visualization")
    if not isinstance(channel_mapping, dict):
        raise ContractError("$.visualization.channel_mapping: expected object")
    if product_state == "rendered_image" and not channel_mapping:
        raise ContractError("$.visualization.channel_mapping: required for rendered image")

    dark = data.get("dark_sector_interpretation")
    if dark is not None:
        if not isinstance(dark, dict):
            raise ContractError("$.dark_sector_interpretation: expected object or null")
        state = require(dark, "state", "$.dark_sector_interpretation")
        if state not in ALLOWED_DARK_STATES:
            raise ContractError("$.dark_sector_interpretation.state: invalid state")
        dark_claim = require(dark, "claim_allowed", "$.dark_sector_interpretation")
        if not isinstance(dark_claim, bool):
            raise ContractError("$.dark_sector_interpretation.claim_allowed: expected boolean")
        if state != "OBSERVATIONALLY_CONSTRAINED" and dark_claim:
            raise ContractError("$.dark_sector_interpretation.claim_allowed: must be false")
        if state == "AUTHORIAL_HYPOTHESIS" and not dark.get("operational_definition"):
            raise ContractError("$.dark_sector_interpretation.operational_definition: required")

    provenance = require(data, "provenance", "$")
    if not isinstance(provenance, dict):
        raise ContractError("$.provenance: expected object")
    for field in ("created_at", "software_commit"):
        require_nonempty_string(require(provenance, field, "$.provenance"), f"$.provenance.{field}")
    transformations = require(provenance, "transformations", "$.provenance")
    if not isinstance(transformations, list) or not all(isinstance(item, str) for item in transformations):
        raise ContractError("$.provenance.transformations: expected array of strings")
    validate_optional_sha256(provenance.get("manifest_sha256"), "$.provenance.manifest_sha256")

    forbidden = {"raw_conversation", "credentials", "access_token", "personal_data"}
    leaked = forbidden.intersection(data)
    if leaked:
        raise ContractError(f"$: forbidden public fields present: {sorted(leaked)}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=pathlib.Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.manifest.read_text(encoding="utf-8"))
        validate_manifest(data)
    except (OSError, json.JSONDecodeError, ContractError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 2
    print("PASS: cosmological photonic observation contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
