"""Referência explícita de saídas textuais deste módulo/pipeline."""

TEXTUAL_OUTPUTS = []

import numpy as np


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


def _json_safe_scalar(value):
    if isinstance(value, (bool, np.bool_)):
        return bool(value)
    if isinstance(value, (int, np.integer)):
        return int(value)
    if isinstance(value, (float, np.floating)):
        scalar = float(value)
        if not np.isfinite(scalar):
            raise ValueError("metadata contains non-finite float")
        return scalar
    if isinstance(value, str):
        return value
    return str(value)


def _json_safe_metadata(metadata):
    if isinstance(metadata, dict):
        return {str(k): _json_safe_metadata(v) for k, v in metadata.items()}
    if isinstance(metadata, (list, tuple)):
        return [_json_safe_metadata(v) for v in metadata]
    return _json_safe_scalar(metadata)


def validate_observable_schema(entry):
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
        if covariance.shape[0] != len(values):
            raise ValueError("covariance dimension must match values length")
        if np.any(np.diag(covariance) <= 0):
            raise ValueError("covariance diagonal must be strictly positive")

    metadata = _json_safe_metadata(entry["metadata"])
    for k in ["survey", "redshift_range", "reference"]:
        if k not in metadata:
            raise ValueError(f"metadata missing key: {k}")

    return {
        "dataset_id": str(entry["dataset_id"]),
        "observable": str(entry["observable"]),
        "z": z,
        "values": values,
        "errors": _as_float_array(entry["errors"], "errors") if has_errors else None,
        "covariance": _as_float_matrix(entry["covariance"], "covariance") if has_cov else None,
        "metadata": metadata,
    }
