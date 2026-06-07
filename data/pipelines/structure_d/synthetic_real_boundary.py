"""Dataset provenance and claim-boundary utilities for RLL validation artifacts."""

from __future__ import annotations

import math
from collections.abc import Mapping, Sequence
from typing import Any

CLAIM_BOUNDARY = "No superiority claim unless real-data metrics pass predefined thresholds."
PUBLICATION_LANGUAGE = "RLL is a candidate effective dynamic-transition cosmology under real-data evaluation."
DATASET_TYPES = {
    "real_observational",
    "synthetic_sanity_check",
    "synthetic_regression_test",
    "mixed_forbidden",
    "unknown_forbidden",
}
INTERPRETATION_LABELS = {
    "inconclusive",
    "lcdm_preferred",
    "rll_preferred_tentative",
    "rll_preferred_strong",
    "blocked_non_real_dataset",
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
        {"synthetic", "synth", "mock", "fixture", "tests/fixtures", "data/synthetic", "results/synthetic"},
    )
    real_flag = any(
        _truthy(metadata.get(key)) for key in ("real", "observational", "measured", "real_observational")
    ) or _contains_token(
        all_values,
        {"data/real", "results/real", "observational", "pantheon", "desi", "cosmic chronometers", "fsigma8", "cmb"},
    )

    if synthetic_flag and real_flag:
        return "mixed_forbidden"
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
            "interpretation_reason": "Non-real or mixed datasets cannot support scientific model-comparison claims.",
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
