import json
import os
import numpy as np
import pandas as pd

from .schema import validate_observable_schema

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def _abs_path(path):
    if os.path.isabs(path):
        return path
    return os.path.join(BASE_DIR, path)


def load_run_config(config_path):
    with open(_abs_path(config_path), "r", encoding="utf-8") as f:
        return json.load(f)


def _resolve_profile(cfg, profile_name=None):
    if "profiles" not in cfg:
        # backward-compatible path (legacy flat config)
        active = cfg.get("active_datasets", [])
        run_name = cfg.get("run_name", "legacy")
        return {"run_name": run_name, "active_datasets": active}

    selected = profile_name or cfg.get("default_profile")
    if selected not in cfg["profiles"]:
        raise ValueError(f"profile not found in config: {selected}")
    return cfg["profiles"][selected]


def _parse_csv_dataset(dataset_id, desc):
    df = pd.read_csv(_abs_path(desc["path"]))
    cols = desc["columns"]
    missing = [c for c in cols.values() if c and c not in df.columns]
    if missing:
        raise ValueError(f"dataset {dataset_id} missing columns: {missing}")

    values = df[cols["value"]].to_numpy(dtype=float)
    z_values = df[cols["z"]].to_numpy(dtype=float) if cols.get("z") else None

    entry = {
        "dataset_id": dataset_id,
        "observable": desc["observable"],
        "z": z_values,
        "values": values,
        "metadata": desc["metadata"],
    }

    if desc["error_model"] == "errors":
        entry["errors"] = df[cols["error"]].to_numpy(dtype=float)
    elif desc["error_model"] == "covariance":
        if cols.get("covariance"):
            cov_path = _abs_path(cols["covariance"])
        else:
            cov_path = _abs_path(desc["covariance_path"])
        entry["covariance"] = np.loadtxt(cov_path, delimiter=",")
    else:
        raise ValueError(f"unsupported error_model for {dataset_id}: {desc['error_model']}")

    return validate_observable_schema(entry)


def _parse_scalar_json_dataset(dataset_id, desc):
    with open(_abs_path(desc["path"]), "r", encoding="utf-8") as f:
        raw = json.load(f)

    keys = desc["keys"]
    values = np.array([raw[k] for k in keys["values"]], dtype=float)
    errors = np.array([raw[k] for k in keys["errors"]], dtype=float)

    entry = {
        "dataset_id": dataset_id,
        "observable": desc["observable"],
        "values": values,
        "errors": errors,
        "metadata": desc["metadata"],
        "z": None,
    }
    return validate_observable_schema(entry)


def load_dataset_by_descriptor(dataset_id, desc):
    fmt = desc["format"]
    if fmt == "csv":
        return _parse_csv_dataset(dataset_id, desc)
    if fmt == "json_scalars":
        return _parse_scalar_json_dataset(dataset_id, desc)
    raise ValueError(f"unsupported dataset format for {dataset_id}: {fmt}")


def load_active_datasets(config_path, profile_name=None):
    cfg = load_run_config(config_path)
    profile = _resolve_profile(cfg, profile_name=profile_name)

    datasets = {}
    for dataset_id in profile["active_datasets"]:
        desc = cfg["datasets"].get(dataset_id)
        if desc is None:
            raise ValueError(f"active dataset not found in config: {dataset_id}")
        datasets[dataset_id] = load_dataset_by_descriptor(dataset_id, desc)

    meta = {
        "run_name": profile.get("run_name", "unknown"),
        "active_datasets": list(profile["active_datasets"]),
        "profile_name": profile_name or cfg.get("default_profile", "legacy")
    }
    return meta, datasets


def load_datasets_by_ids(config_path, dataset_ids):
    cfg = load_run_config(config_path)
    datasets = {}
    for dataset_id in dataset_ids:
        desc = cfg["datasets"].get(dataset_id)
        if desc is None:
            raise ValueError(f"dataset not found in config: {dataset_id}")
        datasets[dataset_id] = load_dataset_by_descriptor(dataset_id, desc)
    return cfg, datasets
