"""Audit synthetic/local datasets and route them to real-data materializations.

The audit is intentionally local-first and fail-safe: it scans committed dataset
configuration plus shallow data paths, records hashes, and writes atomically with
rollback backups.  It does not claim that a synthetic fixture is real; instead it
requires an explicit replacement route or records the gap as still pending.
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
from pathlib import Path
from typing import Iterable

BASE_DIR = Path(__file__).resolve().parents[1]
CONFIG_PATH = BASE_DIR / "data" / "pipelines" / "structure_d" / "datasets_config.json"
RESULTS_DIR = BASE_DIR / "results" / "audit"
CSV_OUT = RESULTS_DIR / "real_data_materialization_audit.csv"
JSON_OUT = RESULTS_DIR / "real_data_materialization_audit.json"
MD_OUT = RESULTS_DIR / "real_data_materialization_audit.md"

SYNTHETIC_MARKERS = ("synthetic", "synth", "mock", "example", "local_input", "fixture")
REAL_REPLACEMENTS = {
    "hz": "real_hz",
    "fsigma8": "real_fsigma8",
    "hz_cov_synth": "real_hz",
    "fsigma8_cov_synth": "real_fsigma8",
    "real_bao": "real_desi_dr2_bao",
}
REAL_SOURCE_URLS = {
    "real_hz": [
        "https://arxiv.org/abs/2205.05701",
        "https://arxiv.org/abs/1604.01410",
    ],
    "real_fsigma8": [
        "https://academic.oup.com/mnras/article-abstract/452/3/2930/1750209",
        "https://arxiv.org/abs/1204.4725",
    ],
    "real_desi_dr2_bao": [
        "https://arxiv.org/abs/2503.14738",
        "https://zenodo.org/records/16644577",
    ],
    "real_cmb_shift": ["https://arxiv.org/abs/1807.06209"],
}

FIELDNAMES = [
    "record_type",
    "dataset_id",
    "status",
    "synthetic_path",
    "real_replacement_id",
    "real_path",
    "real_exists",
    "real_sha256",
    "rollback_policy",
    "source_urls",
    "notes",
]


def _abs(path: str | Path) -> Path:
    path = Path(path)
    return path if path.is_absolute() else BASE_DIR / path


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fp:
        for chunk in iter(lambda: fp.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _display_path(path: Path) -> str:
    try:
        return str(path.relative_to(BASE_DIR))
    except ValueError:
        return str(path)


def _atomic_write(path: Path, text: str) -> dict[str, str | bool]:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + f".tmp-{os.getpid()}")
    backup = path.with_suffix(path.suffix + ".bak")
    rollback = False
    if path.exists():
        backup.write_bytes(path.read_bytes())
        rollback = True
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)
    return {
        "path": _display_path(path),
        "backup_path": _display_path(backup) if rollback else "",
        "rollback_available": rollback,
    }


def _looks_synthetic(dataset_id: str, descriptor: dict) -> bool:
    haystack = " ".join(
        str(value).lower()
        for value in [dataset_id, descriptor.get("path", ""), json.dumps(descriptor.get("metadata", {}), ensure_ascii=False)]
    )
    return any(marker in haystack for marker in SYNTHETIC_MARKERS)


def _load_config() -> dict:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def _dataset_row(dataset_id: str, descriptor: dict, cfg: dict) -> dict[str, str | bool]:
    replacement_id = REAL_REPLACEMENTS.get(dataset_id, "")
    replacement = cfg.get("datasets", {}).get(replacement_id, {}) if replacement_id else {}
    real_path = replacement.get("path", "")
    real_abs = _abs(real_path) if real_path else None
    real_exists = bool(real_abs and real_abs.exists())
    source_urls = REAL_SOURCE_URLS.get(replacement_id, [])
    status = "real_replacement_ready" if real_exists else "real_replacement_missing"
    if not replacement_id:
        status = "needs_real_replacement_mapping"
    return {
        "record_type": "configured_dataset",
        "dataset_id": dataset_id,
        "status": status,
        "synthetic_path": descriptor.get("path", ""),
        "real_replacement_id": replacement_id,
        "real_path": real_path,
        "real_exists": real_exists,
        "real_sha256": _sha256(real_abs) if real_exists and real_abs else "",
        "rollback_policy": "keep synthetic fixture; route production profile to real replacement; restore *.bak on failed artifact write",
        "source_urls": ";".join(source_urls),
        "notes": "synthetic/local dataset has explicit real route" if replacement_id else "no explicit real route yet",
    }


def iter_configured_synthetic_rows(cfg: dict) -> Iterable[dict[str, str | bool]]:
    for dataset_id, descriptor in sorted(cfg.get("datasets", {}).items()):
        if _looks_synthetic(dataset_id, descriptor) or dataset_id in REAL_REPLACEMENTS:
            yield _dataset_row(dataset_id, descriptor, cfg)


def iter_filesystem_marker_rows(max_depth: int = 5) -> Iterable[dict[str, str | bool]]:
    data_root = BASE_DIR / "data"
    for path in sorted(data_root.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(BASE_DIR)
        if len(rel.parts) > max_depth + 1:
            continue
        lowered = str(rel).lower()
        if not any(marker in lowered for marker in SYNTHETIC_MARKERS):
            continue
        yield {
            "record_type": "filesystem_marker",
            "dataset_id": rel.as_posix(),
            "status": "inventory_only_needs_manual_classification",
            "synthetic_path": rel.as_posix(),
            "real_replacement_id": "",
            "real_path": "",
            "real_exists": False,
            "real_sha256": "",
            "rollback_policy": "do not delete; classify before replacing; keep archive/fixture semantics",
            "source_urls": "",
            "notes": "filename/path contains synthetic/mock/example marker but is not a configured production dataset",
        }


def build_rows() -> list[dict[str, str | bool]]:
    cfg = _load_config()
    seen = set()
    rows = []
    for row in iter_configured_synthetic_rows(cfg):
        seen.add(row["synthetic_path"])
        rows.append(row)
    for row in iter_filesystem_marker_rows():
        if row["synthetic_path"] not in seen:
            rows.append(row)
    return rows


def _csv_text(rows: list[dict[str, str | bool]]) -> str:
    from io import StringIO

    buf = StringIO()
    writer = csv.DictWriter(buf, fieldnames=FIELDNAMES, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buf.getvalue()


def _md_text(rows: list[dict[str, str | bool]]) -> str:
    ready = sum(1 for row in rows if row["status"] == "real_replacement_ready")
    missing = sum(1 for row in rows if row["status"] == "real_replacement_missing")
    unmapped = sum(1 for row in rows if row["status"] == "needs_real_replacement_mapping")
    inventory = sum(1 for row in rows if row["record_type"] == "filesystem_marker")
    lines = [
        "# Real-data materialization audit",
        "",
        "This audit scans configured Structure-D datasets plus data files up to five path levels for synthetic/mock/example markers.",
        "It does not rename synthetic fixtures as real data; it records an explicit route to committed real replacements or leaves a gap visible.",
        "",
        "## Summary",
        "",
        f"- Real replacements ready: {ready}",
        f"- Real replacements missing: {missing}",
        f"- Configured datasets without route: {unmapped}",
        f"- Inventory-only filesystem markers: {inventory}",
        "",
        "## Failsafe / failover / rollback",
        "",
        "- Production routes must point to `data/real/**` or a documented external URL.",
        "- Synthetic fixtures are retained for regression tests and rollback; they are not deleted.",
        "- Audit artifacts are written atomically and create `*.bak` when replacing prior outputs.",
        "- If a real source is missing or fails validation, keep the previous artifact and mark the route as pending instead of fabricating data.",
        "",
        "## Configured synthetic-to-real routes",
        "",
        "| dataset_id | status | synthetic_path | real_replacement_id | real_path |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        if row["record_type"] != "configured_dataset":
            continue
        lines.append(
            f"| {row['dataset_id']} | {row['status']} | {row['synthetic_path']} | {row['real_replacement_id']} | {row['real_path']} |"
        )
    lines.append("")
    return "\n".join(lines)


def run_audit() -> dict:
    rows = build_rows()
    outputs = [
        _atomic_write(CSV_OUT, _csv_text(rows)),
        _atomic_write(JSON_OUT, json.dumps({"schema": "rll.real_data_materialization_audit.v1", "rows": rows}, ensure_ascii=False, indent=2) + "\n"),
        _atomic_write(MD_OUT, _md_text(rows)),
    ]
    return {"rows": rows, "outputs": outputs}


def main() -> dict:
    payload = run_audit()
    print(f"Audited {len(payload['rows'])} rows")
    for output in payload["outputs"]:
        print(f"Wrote: {output['path']}")
    return payload


if __name__ == "__main__":
    main()
