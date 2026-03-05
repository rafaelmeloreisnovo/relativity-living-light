"""Referência explícita de saídas textuais deste módulo/pipeline."""

TEXTUAL_OUTPUTS = []

import numpy as np


DEFAULT_MIN_POINTS_WITH_Z = 3


def _as_float_array(values, name):
    arr = np.asarray(values, dtype=float)
    if arr.ndim != 1:
        raise ValueError(f"{name} must be a 1D array")
    if np.any(~np.isfinite(arr)):
        raise ValueError(f"{name} must contain only finite values")
    return arr


def _as_float_matrix(values, name):
    mat = np.asarray(values, dtype=float)
    if mat.ndim != 2:
        raise ValueError(f"{name} must be a 2D matrix")
    if mat.shape[0] != mat.shape[1]:
        raise ValueError(f"{name} must be square")
    if np.any(~np.isfinite(mat)):
        raise ValueError(f"{name} must contain only finite values")
    return mat


def validate_observable_schema(entry, min_points_with_z=DEFAULT_MIN_POINTS_WITH_Z):
    if int(min_points_with_z) != min_points_with_z or min_points_with_z < 1:
        raise ValueError("min_points_with_z must be a positive integer")

    required = ["dataset_id", "observable", "values", "metadata"]
    missing = [k for k in required if k not in entry]
    if missing:
        raise ValueError(f"missing schema keys: {missing}")

    values = _as_float_array(entry["values"], "values")
    z = None
    if "z" in entry and entry["z"] is not None:
        z = _as_float_array(entry["z"], "z")
        if len(z) != len(values):
            raise ValueError("z and values must have the same length")
        if len(z) < int(min_points_with_z):
            raise ValueError(
                f"datasets with z must have at least {int(min_points_with_z)} points"
            )

    has_errors = "errors" in entry and entry["errors"] is not None
    has_cov = "covariance" in entry and entry["covariance"] is not None
    if has_errors == has_cov:
        raise ValueError("provide exactly one of errors or covariance")

    if has_errors:
        errors = _as_float_array(entry["errors"], "errors")
        if len(errors) != len(values):
            raise ValueError("errors and values must have the same length")
        if np.any(errors <= 0):
            raise ValueError("errors must be strictly positive")
    else:
        covariance = _as_float_matrix(entry["covariance"], "covariance")
        _validate_covariance_matrix(covariance, expected_size=len(values))

    metadata = _json_safe_metadata(entry["metadata"])
    for k in ["survey", "redshift_range", "reference"]:
        if k not in metadata:
            raise ValueError(f"metadata missing key: {k}")

    dataset_source = entry.get("dataset_source")

    return {
        "dataset_id": str(entry["dataset_id"]),
        "observable": str(entry["observable"]),
        "z": z,
        "values": values,
        "errors": _as_float_array(entry["errors"], "errors") if has_errors else None,
        "covariance": _as_float_matrix(entry["covariance"], "covariance") if has_cov else None,
        "metadata": metadata,
        "dataset_source": str(dataset_source) if dataset_source is not None else "unknown",
    }


def _validate_covariance_matrix(covariance, expected_size):
    if covariance.shape != (expected_size, expected_size):
        raise ValueError(
            f"covariance must have shape ({expected_size}, {expected_size})"
        )
    if not np.allclose(covariance, covariance.T, rtol=1e-10, atol=1e-12):
        raise ValueError("covariance must be symmetric")
    diag = np.diag(covariance)
    if np.any(diag <= 0):
        raise ValueError("covariance diagonal must be strictly positive")


def _json_safe_metadata(metadata):
    if not isinstance(metadata, dict):
        raise ValueError("metadata must be a dict")
    cleaned = {}
    for key, value in metadata.items():
        cleaned[str(key)] = value if isinstance(value, (str, int, float, bool)) or value is None else str(value)
    return cleaned
