"""Referência explícita de saídas textuais deste módulo/pipeline."""

TEXTUAL_OUTPUTS = []

import numpy as np


_COVARIANCE_VALIDATION_ATOL = 1e-10
_COVARIANCE_VALIDATION_RTOL = 1e-8


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


def _validate_covariance_matrix(covariance, expected_size):
    if covariance.shape[0] != expected_size:
        raise ValueError("covariance dimension must match values length")
    if np.any(np.diag(covariance) <= 0):
        raise ValueError("covariance diagonal must be strictly positive")
    if not np.allclose(
        covariance,
        covariance.T,
        rtol=_COVARIANCE_VALIDATION_RTOL,
        atol=_COVARIANCE_VALIDATION_ATOL,
    ):
        raise ValueError(
            "invalid covariance matrix: matrix must be symmetric within tolerance "
            f"(rtol={_COVARIANCE_VALIDATION_RTOL}, atol={_COVARIANCE_VALIDATION_ATOL})"
        )

    sym_cov = 0.5 * (covariance + covariance.T)
    eigvals = np.linalg.eigvalsh(sym_cov)
    min_eig = float(np.min(eigvals))
    scale = max(float(np.max(np.diag(sym_cov))), 1.0)
    eig_tol = _COVARIANCE_VALIDATION_ATOL + _COVARIANCE_VALIDATION_RTOL * scale
    if min_eig < -eig_tol:
        raise ValueError(
            "invalid covariance matrix: matrix must be positive semidefinite "
            f"within tolerance (min_eigenvalue={min_eig:.3e}, tol={eig_tol:.3e})"
        )


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
        _validate_covariance_matrix(covariance, expected_size=len(values))

    metadata = entry["metadata"]
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
