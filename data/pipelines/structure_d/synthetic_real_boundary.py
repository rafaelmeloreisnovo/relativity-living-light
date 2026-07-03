"""Dataset provenance and claim-boundary utilities for RLL validation artifacts."""

from __future__ import annotations

import json
import math
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

CLAIM_BOUNDARY = "No superiority claim unless real-data metrics pass predefined thresholds."
PUBLICATION_LANGUAGE = "RLL is a candidate effective dynamic-transition cosmology under real-data evaluation."
DATASET_TYPES = {
    "real_observational",
    "synthetic_sanity_check",
    "synthetic_regression_test",
    "forecast",
    "mixed_forbidden",
    "unknown_forbidden",
}
APPROVED_SYNTHETIC_ROOTS = ("data/synthetic/", "results/synthetic/", "tests/fixtures/")
LEGACY_SYNTHETIC_MANIFEST_PATH = Path("data/synthetic/LEGACY_SYNTHETIC_MANIFEST.json")
SYNTHETIC_PATH_TOKENS = ("synthetic", "synth", "mock", "demo", "fixture", "example")

INTERPRETATION_LABELS = {
    "inconclusive",
    "lcdm_preferred",
    "rll_preferred_tentative",
    "rll_preferred_strong",
    "blocked_non_real_dataset",
}


def normalize_repo_path(path: str | Path) -> str:
    """Return a stable POSIX-style relative repository path."""

    return str(path).replace("\\", "/").lstrip("./")


def is_approved_synthetic_path(path: str | Path) -> bool:
    """Return True when a path lives inside an approved synthetic/fixture root."""

    normalized = normalize_repo_path(path)
    return any(normalized.startswith(root) for root in APPROVED_SYNTHETIC_ROOTS)


def looks_like_synthetic_path(path: str | Path) -> bool:
    """Detect path names that carry synthetic/mock/demo/fixture/example semantics."""

    normalized = normalize_repo_path(path).lower()
    return any(token in normalized for token in SYNTHETIC_PATH_TOKENS)


def load_legacy_synthetic_manifest(manifest_path: str | Path = LEGACY_SYNTHETIC_MANIFEST_PATH) -> dict[str, Any]:
    """Load the legacy synthetic manifest used for compatibility exceptions."""

    with Path(manifest_path).open(encoding="utf-8") as handle:
        return json.load(handle)


def legacy_synthetic_paths(manifest_path: str | Path = LEGACY_SYNTHETIC_MANIFEST_PATH) -> set[str]:
    """Return legacy paths already cataloged behind the synthetic claim boundary."""

    manifest = load_legacy_synthetic_manifest(manifest_path)
    return {normalize_repo_path(entry["original_path"]) for entry in manifest.get("entries", [])}


def find_unapproved_synthetic_paths(
    paths: Sequence[str | Path],
    *,
    manifest_path: str | Path = LEGACY_SYNTHETIC_MANIFEST_PATH,
) -> list[str]:
    """List synthetic-looking paths outside approved roots and outside the manifest."""

    cataloged = legacy_synthetic_paths(manifest_path)
    violations: list[str] = []
    for path in paths:
        normalized = normalize_repo_path(path)
        if is_approved_synthetic_path(normalized):
            continue
        if normalized in cataloged:
            continue
        if looks_like_synthetic_path(normalized):
            violations.append(normalized)
    return sorted(violations)


def enforce_real_validation_input_boundary(metadata: Mapping[str, Any]) -> dict[str, Any]:
    """Block real-validation inputs that route through synthetic/mock artifacts."""

    classification_metadata = dict(metadata)
    if _truthy(classification_metadata.get("regression_fixture")):
        classification_metadata.pop("dataset_type", None)
    dataset_type = classify_dataset_type(classification_metadata)
    paths = [normalize_repo_path(path) for path in _as_sequence(metadata.get("path")) + _as_sequence(metadata.get("paths"))]
    violating_paths = [
        path
        for path in paths
        if looks_like_synthetic_path(path)
        and not (is_approved_synthetic_path(path) and _truthy(metadata.get("regression_fixture")))
    ]
    allowed = dataset_type == "real_observational" and not violating_paths
    return {
        "real_validation_input_allowed": allowed,
        "dataset_type": dataset_type,
        "violating_paths": violating_paths,
        "reason": (
            "Real validation input paths are observational and contain no synthetic/mock/fixture markers."
            if allowed
            else "Real validation cannot consume synthetic/mock/demo/example/fixture artifacts unless they are explicit test fixtures."
        ),
    }


def validate_real_dataset_manifest_entry(metadata: Mapping[str, Any]) -> dict[str, Any]:
    """Validate canonical real-dataset metadata before real-validation use.

    Real observational entries must carry source_id, sha256, local_path,
    dataset_type, and may not point at synthetic/mock/demo/fixture/example
    paths. Test fixtures are classified explicitly as regression fixtures and
    are never accepted as real validation inputs.
    """

    classification_metadata = dict(metadata)
    if _truthy(classification_metadata.get("regression_fixture")):
        classification_metadata.pop("dataset_type", None)
    dataset_type = classify_dataset_type(classification_metadata)
    paths = [
        normalize_repo_path(path)
        for path in _as_sequence(metadata.get("local_path"))
        + _as_sequence(metadata.get("path"))
        + _as_sequence(metadata.get("paths"))
    ]
    violating_paths = [
        path
        for path in paths
        if looks_like_synthetic_path(path)
        and not (is_approved_synthetic_path(path) and _truthy(metadata.get("regression_fixture")))
    ]
    missing_fields = [
        field
        for field in ("source_id", "sha256", "local_path", "dataset_type")
        if not str(metadata.get(field, "")).strip()
    ]
    valid = dataset_type == "real_observational" and not violating_paths and not missing_fields
    return {
        "valid": valid,
        "dataset_type": dataset_type,
        "violating_paths": violating_paths,
        "missing_fields": missing_fields,
        "reason": (
            "Canonical real dataset entry is complete and path-clean."
            if valid
            else "Real dataset entries require source_id, sha256, local_path, dataset_type and path-clean real inputs."
        ),
    }


def _as_sequence(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, (str, bytes)):
        return [value]
    if isinstance(value, Sequence):
        return list(value)
    return [value]


def _truthy(value: Any) -> bool:
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "y", "real", "observational"}
    return bool(value)


def _contains_token(values: Sequence[Any], tokens: set[str]) -> bool:
    text = " ".join(str(value).lower() for value in values)
    return any(token in text for token in tokens)


def classify_dataset_type(metadata: dict) -> str:
    """Classify a dataset from explicit flags, source metadata, and paths.

    Synthetic indicators always win over real indicators when both are present,
    because a mixed artifact is forbidden for scientific claims.
    """

    explicit = str(metadata.get("dataset_type", "")).strip()
    if explicit in DATASET_TYPES:
        return explicit

    paths = _as_sequence(metadata.get("path")) + _as_sequence(metadata.get("paths"))
    sources = _as_sequence(metadata.get("source")) + _as_sequence(metadata.get("sources"))
    flags = _as_sequence(metadata.get("flags")) + _as_sequence(metadata.get("tags"))
    all_values = paths + sources + flags + list(metadata.keys())

    synthetic_flag = any(
        _truthy(metadata.get(key))
        for key in ("synthetic", "mock", "fixture", "regression_fixture", "sanity_check")
    ) or _contains_token(
        all_values,
        {"synthetic", "synth", "mock", "demo", "example", "fixture", "tests/fixtures", "data/synthetic", "results/synthetic"},
    )
    forecast_flag = any(
        _truthy(metadata.get(key)) for key in ("forecast", "simulated_forecast", "future_survey")
    ) or _contains_token(
        all_values,
        {"forecast", "future survey", "simulated forecast", "mock forecast"},
    )
    real_flag = any(
        _truthy(metadata.get(key)) for key in ("real", "observational", "measured", "real_observational")
    ) or _contains_token(
        all_values,
        {"data/real", "results/real", "observational", "pantheon", "desi", "cosmic chronometers", "fsigma8", "cmb"},
    )

    explicit_real_flag = any(
        _truthy(metadata.get(key)) for key in ("real", "observational", "measured", "real_observational")
    ) or _contains_token(paths, {"data/real", "results/real", "observational"})
    if forecast_flag and (synthetic_flag or explicit_real_flag):
        return "mixed_forbidden"
    if synthetic_flag and real_flag:
        return "mixed_forbidden"
    if forecast_flag:
        return "forecast"
    if synthetic_flag:
        if _truthy(metadata.get("regression_fixture")) or _contains_token(all_values, {"regression", "tests/fixtures"}):
            return "synthetic_regression_test"
        return "synthetic_sanity_check"
    if real_flag:
        return "real_observational"
    return "unknown_forbidden"


def _finite_number(value: Any) -> float | None:
    if value is None:
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(number):
        return None
    return number


def interpret_model_comparison(delta: dict, dataset_type: str) -> dict:
    """Interpret RLL-minus-LCDM deltas using conservative predefined thresholds."""

    if dataset_type != "real_observational":
        return {
            "interpretation_label": "blocked_non_real_dataset",
            "interpretation_reason": "Non-real, forecast, or mixed datasets cannot support scientific model-comparison claims.",
        }

    daic = _finite_number(delta.get("delta_aic_rll_minus_lcdm"))
    dbic = _finite_number(delta.get("delta_bic_rll_minus_lcdm"))
    dchi2 = _finite_number(delta.get("delta_chi2_rll_minus_lcdm"))
    if daic is None or dbic is None:
        return {
            "interpretation_label": "inconclusive",
            "interpretation_reason": "AIC/BIC deltas are absent or invalid for this execution.",
        }
    if daic > 0 or dbic > 0:
        return {
            "interpretation_label": "lcdm_preferred",
            "interpretation_reason": "At least one information-criterion delta is positive for RLL minus LCDM.",
        }
    if daic <= -6 and dbic <= -6 and dchi2 is not None and dchi2 < 0:
        return {
            "interpretation_label": "rll_preferred_strong",
            "interpretation_reason": "Predefined real-data thresholds were satisfied in this dataset and execution only.",
        }
    if daic <= -2 and dbic <= -2:
        return {
            "interpretation_label": "rll_preferred_tentative",
            "interpretation_reason": "Tentative predefined real-data thresholds were satisfied in this dataset and execution only.",
        }
    return {
        "interpretation_label": "inconclusive",
        "interpretation_reason": "Predefined AIC/BIC thresholds were not jointly satisfied.",
    }


def enforce_claim_boundary(dataset_type: str, metrics: dict | None = None) -> dict:
    """Return machine-readable claim permissions for an artifact."""

    metrics = metrics or {}
    interpretation = interpret_model_comparison(metrics, dataset_type)
    label = interpretation["interpretation_label"]
    claim_allowed = bool(dataset_type == "real_observational" and label in {"rll_preferred_tentative", "rll_preferred_strong"})
    if dataset_type != "real_observational":
        reason = "Synthetic, mixed, fixture, or unknown data are blocked from scientific claims."
    elif claim_allowed:
        reason = "Only predefined real-data thresholds were satisfied; no broad superiority language is allowed."
    else:
        reason = interpretation["interpretation_reason"]
    return {
        "claim_allowed": claim_allowed,
        "claim_boundary": CLAIM_BOUNDARY,
        "reason": reason,
        "publication_language": PUBLICATION_LANGUAGE,
    }


def main(paths: Sequence[str | Path] | None = None) -> int:
    """CI gate for unapproved synthetic-looking artifact paths.

    By default this validates the legacy migration manifest itself: cataloged
    legacy aliases remain allowed temporarily, and every proposed migration path
    must live under an approved synthetic/fixture root. Callers may pass an
    explicit path sequence to gate newly produced artifacts.
    """

    if paths is None:
        manifest = load_legacy_synthetic_manifest()
        paths = [
            path
            for entry in manifest.get("entries", [])
            for path in (entry.get("original_path"), entry.get("proposed_boundary_path"))
            if path
        ]
    violations = find_unapproved_synthetic_paths(paths)
    if violations:
        print("Unapproved synthetic/mock/demo/example/fixture paths found outside approved roots:")
        for path in violations:
            print(f"- {path}")
        return 1
    print("Synthetic path boundary check passed.")
    return 0


if __name__ == "__main__":
    import sys

    raise SystemExit(main(sys.argv[1:] or None))
