"""Referência explícita de saídas textuais deste módulo/pipeline."""

TEXTUAL_OUTPUTS = []

import json
import os
import hashlib
from datetime import datetime, timezone
import numpy as np
import pandas as pd

from .schema import DEFAULT_MIN_POINTS_WITH_Z, validate_observable_schema

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def _abs_path(path):
    if os.path.isabs(path):
        return path
    return os.path.join(BASE_DIR, path)


def _dataset_source_from_descriptor(desc):
    metadata = desc.get("metadata") or {}
    source_parts = []

    dataset_path = desc.get("path")
    if dataset_path:
        source_parts.append(f"path={dataset_path}")

    reference = metadata.get("reference")
    if reference:
        source_parts.append(f"reference={reference}")

    return "; ".join(source_parts) if source_parts else "unknown"


def load_run_config(config_path):
    with open(_abs_path(config_path), "r", encoding="utf-8") as f:
        cfg = json.load(f)

    validation_cfg = cfg.setdefault("validation", {})
    validation_cfg.setdefault("min_points_with_z", DEFAULT_MIN_POINTS_WITH_Z)
    return cfg


def _resolve_profile(cfg, profile_name=None):
    if "profiles" not in cfg:
        # backward-compatible path (legacy flat config)
        resolved = dict(cfg)
        resolved.setdefault("run_name", "legacy")
        resolved["active_datasets"] = list(cfg.get("active_datasets", []))
        return resolved

    selected = profile_name or cfg.get("default_profile")
    if selected not in cfg["profiles"]:
        raise ValueError(f"profile not found in config: {selected}")
    resolved = dict(cfg["profiles"][selected])
    resolved["active_datasets"] = list(resolved.get("active_datasets", []))
    if "covariance_policy" not in resolved and "covariance_policy" in cfg:
        resolved["covariance_policy"] = cfg["covariance_policy"]
    return resolved


def _parse_csv_dataset(dataset_id, desc, min_points_with_z=DEFAULT_MIN_POINTS_WITH_Z):
    source_info = _build_source_info(desc["path"])
    df = pd.read_csv(source_info["path_abs"])
    cols = desc["columns"]
    missing = [c for c in cols.values() if c and c not in df.columns]
    if missing:
        raise ValueError(f"dataset {dataset_id} missing columns: {missing}")

    selected_covariance_idx = None
    z_col = cols.get("z")
    if z_col:
        dup_mask = df.duplicated(subset=[z_col], keep=False)
        if dup_mask.any():
            raw_policy = str(desc.get("duplicate_z_policy", "erro")).strip().lower()
            policy_aliases = {
                "erro": "erro",
                "error": "erro",
                "agregar": "agregar",
                "aggregate": "agregar",
                "primeira ocorrência": "primeira_ocorrencia",
                "primeira_ocorrencia": "primeira_ocorrencia",
                "first": "primeira_ocorrencia",
            }
            policy = policy_aliases.get(raw_policy)
            if policy is None:
                raise ValueError(
                    f"dataset {dataset_id} has unsupported duplicate_z_policy: {desc.get('duplicate_z_policy')}"
                )

            dup_z_values = sorted(df.loc[dup_mask, z_col].astype(float).unique().tolist())
            if policy == "erro":
                raise ValueError(
                    f"dataset {dataset_id} has duplicated z values in column '{z_col}': {dup_z_values}"
                )

            if policy == "agregar":
                if desc["error_model"] == "covariance":
                    raise ValueError(
                        f"dataset {dataset_id} duplicate_z_policy='agregar' is not supported for covariance"
                    )
                agg_map = {cols["value"]: "mean"}
                if cols.get("error"):
                    agg_map[cols["error"]] = "mean"
                df = df.groupby(z_col, sort=False, as_index=False).agg(agg_map)
            elif policy == "primeira_ocorrencia":
                first_mask = ~df.duplicated(subset=[z_col], keep="first")
                selected_covariance_idx = np.flatnonzero(first_mask.to_numpy())
                df = df.loc[first_mask].reset_index(drop=True)

    values = df[cols["value"]].to_numpy(dtype=float)
    z_values = df[cols["z"]].to_numpy(dtype=float) if cols.get("z") else None
    z_reordered = False

    if z_values is not None:
        z_order_policy = desc.get("z_order_policy", "validate")
        if z_order_policy not in ("validate", "sort"):
            raise ValueError(
                f"unsupported z_order_policy for {dataset_id}: {z_order_policy}"
            )

        monotonic_non_decreasing = np.all(np.diff(z_values) >= 0.0)
        if not monotonic_non_decreasing:
            if z_order_policy == "sort":
                sort_idx = np.argsort(z_values, kind="mergesort")
                z_values = z_values[sort_idx]
                values = values[sort_idx]
                z_reordered = True
            else:
                raise ValueError(
                    f"dataset {dataset_id} has non-monotonic z; "
                    "set z_order_policy='sort' to reorder explicitly"
                )

    metadata = dict(desc["metadata"])
    metadata["z_reordered"] = bool(z_reordered)

    entry = {
        "dataset_id": dataset_id,
        "observable": desc["observable"],
        "z": z_values,
        "values": values,
        "metadata": metadata,
        "source": source_info,
    }

    if desc["error_model"] == "errors":
        errors = df[cols["error"]].to_numpy(dtype=float)
        if z_reordered:
            errors = errors[sort_idx]
        entry["errors"] = errors
    elif desc["error_model"] == "covariance":
        if cols.get("covariance"):
            cov_path = _abs_path(cols["covariance"])
        else:
            cov_path = _abs_path(desc["covariance_path"])
        covariance = np.loadtxt(cov_path, delimiter=",")
        if selected_covariance_idx is not None:
            covariance = covariance[np.ix_(selected_covariance_idx, selected_covariance_idx)]
        if z_reordered:
            covariance = covariance[np.ix_(sort_idx, sort_idx)]
        entry["covariance"] = covariance
    else:
        raise ValueError(f"unsupported error_model for {dataset_id}: {desc['error_model']}")

    return validate_observable_schema(entry, min_points_with_z=min_points_with_z)


def _parse_scalar_json_dataset(dataset_id, desc, min_points_with_z=DEFAULT_MIN_POINTS_WITH_Z):
    source_info = _build_source_info(desc["path"])
    with open(source_info["path_abs"], "r", encoding="utf-8") as f:
        raw = json.load(f)

    keys = desc["keys"]
    missing_values = [k for k in keys["values"] if k not in raw]
    missing_errors = [k for k in keys["errors"] if k not in raw]
    if missing_values or missing_errors:
        raise ValueError(
            "dataset "
            f"{dataset_id} missing json keys in file {source_info['path_abs']}: "
            f"values={missing_values}, errors={missing_errors}"
        )

    values = np.array([raw[k] for k in keys["values"]], dtype=float)
    errors = np.array([raw[k] for k in keys["errors"]], dtype=float)

    entry = {
        "dataset_id": dataset_id,
        "observable": desc["observable"],
        "values": values,
        "errors": errors,
        "metadata": dict(desc["metadata"]),
        "dataset_source": _dataset_source_from_descriptor(desc),
        "z": None,
        "source": source_info,
    }
    return validate_observable_schema(entry, min_points_with_z=min_points_with_z)


def _build_source_info(path):
    path_abs = _abs_path(path)
    digest_obj = hashlib.sha256()
    with open(path_abs, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest_obj.update(chunk)
    digest = digest_obj.hexdigest()
    mtime_utc = datetime.fromtimestamp(os.path.getmtime(path_abs), tz=timezone.utc).isoformat()
    return {
        "path_abs": path_abs,
        "timestamp_utc": mtime_utc,
        "sha256": digest,
    }


def load_dataset_by_descriptor(dataset_id, desc, min_points_with_z=DEFAULT_MIN_POINTS_WITH_Z):
    fmt = desc["format"]
    if fmt == "csv":
        return _parse_csv_dataset(dataset_id, desc, min_points_with_z=min_points_with_z)
    if fmt == "json_scalars":
        return _parse_scalar_json_dataset(dataset_id, desc, min_points_with_z=min_points_with_z)
    raise ValueError(f"unsupported dataset format for {dataset_id}: {fmt}")


def load_active_datasets(config_path, profile_name=None):
    cfg = load_run_config(config_path)
    profile = _resolve_profile(cfg, profile_name=profile_name)

    min_points_with_z = cfg.get("validation", {}).get("min_points_with_z", DEFAULT_MIN_POINTS_WITH_Z)

    datasets = {}
    for dataset_id in profile["active_datasets"]:
        desc = cfg["datasets"].get(dataset_id)
        if desc is None:
            raise ValueError(f"active dataset not found in config: {dataset_id}")
        datasets[dataset_id] = load_dataset_by_descriptor(
            dataset_id, desc, min_points_with_z=min_points_with_z
        )

    meta = dict(profile)
    meta["run_name"] = profile.get("run_name", "unknown")
    meta["active_datasets"] = list(profile["active_datasets"])
    meta["profile_name"] = profile_name or cfg.get("default_profile", "legacy")
    return meta, datasets


def load_datasets_by_ids(config_path, dataset_ids):
    cfg = load_run_config(config_path)
    min_points_with_z = cfg.get("validation", {}).get("min_points_with_z", DEFAULT_MIN_POINTS_WITH_Z)

    datasets = {}
    for dataset_id in dataset_ids:
        desc = cfg["datasets"].get(dataset_id)
        if desc is None:
            raise ValueError(f"dataset not found in config: {dataset_id}")
        datasets[dataset_id] = load_dataset_by_descriptor(
            dataset_id, desc, min_points_with_z=min_points_with_z
        )
    return cfg, datasets
