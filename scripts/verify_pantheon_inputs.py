from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

REQUIRED_FILES = {
    "lcparam_full_long_zhel.txt": "Pantheon+SH0ES light-curve parameter table",
    "Pantheon+SH0ES_STAT+SYS.cov": "Pantheon+SH0ES combined statistical+systematic covariance matrix",
}


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _build_report(data_dir: Path) -> dict[str, object]:
    files: list[dict[str, object]] = []
    missing: list[str] = []
    for filename, description in REQUIRED_FILES.items():
        path = data_dir / filename
        if not path.exists():
            missing.append(filename)
            files.append(
                {
                    "file": filename,
                    "description": description,
                    "status": "missing",
                    "size_bytes": None,
                    "sha256": None,
                }
            )
            continue
        files.append(
            {
                "file": filename,
                "description": description,
                "status": "ok",
                "size_bytes": path.stat().st_size,
                "sha256": _sha256(path),
            }
        )
    return {
        "data_dir": str(data_dir),
        "all_present": not missing,
        "missing": missing,
        "files": files,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify required Pantheon+ inputs and print checksums")
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path("data/pantheon"),
        help="Directory containing Pantheon+ input files",
    )
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    args = parser.parse_args()

    report = _build_report(args.data_dir)
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print("[rll] Pantheon+ input verification")
        print(f"data_dir={report['data_dir']}")
        for entry in report["files"]:
            if entry["status"] == "ok":
                print(
                    f" - OK: {entry['file']} size={entry['size_bytes']} sha256={entry['sha256']}"
                )
            else:
                print(f" - MISSING: {entry['file']}")

    if not report["all_present"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
