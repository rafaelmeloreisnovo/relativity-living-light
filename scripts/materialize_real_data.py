from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "real_sources" / "real_data_registry.json"
MANIFEST = ROOT / "data" / "real_sources" / "real_data_manifest.json"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_registry() -> dict:
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def iter_candidate_files(registry: dict, dataset_id: str | None):
    for dataset in registry.get("datasets", []):
        if dataset_id and dataset.get("id") != dataset_id:
            continue
        for entry in dataset.get("candidate_remote_files", []):
            yield dataset, entry


def download_first_available(urls: list[str], dst: Path, timeout: int = 90) -> dict:
    errors: list[str] = []
    dst.parent.mkdir(parents=True, exist_ok=True)
    for url in urls:
        try:
            with urllib.request.urlopen(url, timeout=timeout) as response:
                data = response.read()
            dst.write_bytes(data)
            return {
                "ok": True,
                "url": url,
                "local_path": str(dst.relative_to(ROOT)),
                "bytes": len(data),
                "sha256": sha256_file(dst),
                "errors": errors,
            }
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            errors.append(f"{url}: {exc}")
    return {
        "ok": False,
        "url": None,
        "local_path": str(dst.relative_to(ROOT)),
        "bytes": None,
        "sha256": None,
        "errors": errors,
    }


def materialize(dataset_id: str | None, dry_run: bool) -> dict:
    registry = load_registry()
    results = []
    for dataset, entry in iter_candidate_files(registry, dataset_id):
        dst = ROOT / entry["local_path"]
        item = {
            "dataset_id": dataset.get("id"),
            "local_path": entry["local_path"],
            "candidate_urls": entry.get("urls", []),
            "note": entry.get("note"),
            "already_exists": dst.exists(),
        }
        if dst.exists():
            item.update({
                "ok": True,
                "materialized": False,
                "bytes": dst.stat().st_size,
                "sha256": sha256_file(dst),
            })
        elif dry_run:
            item.update({
                "ok": None,
                "materialized": False,
                "bytes": None,
                "sha256": None,
            })
        else:
            dl = download_first_available(entry.get("urls", []), dst)
            item.update(dl)
            item["materialized"] = bool(dl.get("ok"))
        results.append(item)

    manifest = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "registry": str(REGISTRY.relative_to(ROOT)),
        "dataset_filter": dataset_id,
        "dry_run": dry_run,
        "results": results,
        "claim_boundary": registry.get("claim_boundary"),
    }
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Materialize declared real-data files and write SHA256 manifest.")
    parser.add_argument("--dataset", default=None, help="Optional dataset id, e.g. pantheon_plus_shoes")
    parser.add_argument("--dry-run", action="store_true", help="Do not download; only show planned materialization.")
    args = parser.parse_args()

    manifest = materialize(dataset_id=args.dataset, dry_run=args.dry_run)
    print(json.dumps(manifest, indent=2, ensure_ascii=False))

    failed = [r for r in manifest["results"] if r.get("ok") is False]
    if failed:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
