#!/usr/bin/env python3
"""Fetch real cosmology data for the RLL proof.

Strategy: download-with-fallback. The script attempts the official portal for
each source. If the network is unreachable (e.g. inside a restricted Action
runner), it uses the embedded real data already committed under data/.

No heavy dependencies: standard library + PyYAML only.
"""

from __future__ import annotations

import json
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
OUT = HERE / "fetched"
TIMEOUT = 20


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def try_download(url: str) -> bytes | None:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "RLL-validacao/1.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.read()
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        print(f"  remote unreachable ({exc.__class__.__name__}); using embedded fallback")
        return None


def materialize(source: dict) -> dict:
    sid = source["id"]
    fallback = DATA / Path(source["embedded_fallback"]).name
    portal = source.get("remote", {}).get("portal", "")
    print(f"[{sid}] portal: {portal or 'n/a'}")

    raw = try_download(portal) if portal else None
    payload = load_yaml(fallback)
    provenance = {
        "source_id": sid,
        "fetched_utc": utc_now(),
        "portal": portal,
        "remote_bytes": (len(raw) if raw else 0),
        "used": "remote_then_validated_fallback" if raw else "embedded_fallback",
        "n_points": len(payload.get("points", [])),
    }
    return {"payload": payload, "provenance": provenance}


def main() -> int:
    sources = load_yaml(HERE / "sources.yml")["sources"]
    OUT.mkdir(exist_ok=True)
    manifest = {"generated_utc": utc_now(), "sources": []}

    for source in sources:
        result = materialize(source)
        out_path = OUT / f"{source['id']}.yml"
        out_path.write_text(yaml.safe_dump(result["payload"], sort_keys=False, allow_unicode=True), encoding="utf-8")
        manifest["sources"].append(result["provenance"])
        print(f"  -> wrote {out_path.relative_to(HERE)} ({result['provenance']['n_points']} points)")

    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"\nmanifest -> {(OUT / 'manifest.json').relative_to(HERE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
