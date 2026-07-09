"""Verify live source signatures for committed real cosmology inputs.

The verifier fetches lightweight HTTP metadata and a bounded byte sample from
source URLs, records local file SHA256 hashes, and writes artifacts atomically.
It is a provenance check, not a data downloader: failures are explicit rows for
failover/rollback instead of silent substitution.
"""

from __future__ import annotations

import hashlib
import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
RESULTS_DIR = BASE_DIR / "results" / "audit"
SIGNATURE_JSON = BASE_DIR / "data" / "real" / "cosmology" / "real_source_signatures.json"
RESULT_JSON = RESULTS_DIR / "real_source_signature_verification.json"
RESULT_MD = RESULTS_DIR / "real_source_signature_verification.md"
FETCH_LIMIT = 65536
TIMEOUT_SECONDS = 25

SOURCES = [
    {
        "dataset_id": "real_hz",
        "local_path": "data/real/Hz_data_real.csv",
        "source_url": "https://arxiv.org/abs/2205.05701",
        "required_terms": ["H(z=0.8)", "Moresco"],
        "provenance_note": "Cosmic-chronometer H(z) source check for the materialized expansion table.",
    },
    {
        "dataset_id": "real_desi_dr2_bao",
        "local_path": "data/real/cosmology/desi_dr2_bao_primary_points.csv",
        "source_url": "https://arxiv.org/abs/2503.14738",
        "required_terms": ["DESI DR2", "Baryon Acoustic Oscillations"],
        "provenance_note": "DESI DR2 BAO paper source check for primary BAO measurements.",
    },
    {
        "dataset_id": "real_desi_dr2_bao_supplement",
        "local_path": "data/real/cosmology/desi_dr2_bao_covariance_summary.csv",
        "source_url": "https://zenodo.org/records/16644577",
        "required_terms": ["10.5281/zenodo.16644577", "DESI DR2"],
        "provenance_note": "DESI DR2 supplementary archive check for covariance/supporting data.",
    },
    {
        "dataset_id": "real_fsigma8_6dfgs_anchor",
        "local_path": "data/real/cosmology/fsigma8_growth_real.csv",
        "source_url": "https://arxiv.org/abs/1204.4725",
        "required_terms": ["6dF", "growth"],
        "provenance_note": "6dFGS fσ8 anchor source check for growth materialization.",
    },
    {
        "dataset_id": "real_fsigma8_compilation",
        "local_path": "data/real/cosmology/fsigma8_growth_real.csv",
        "source_url": "https://academic.oup.com/mnras/article-abstract/452/3/2930/1750209",
        "required_terms": ["Growth", "Cosmic Structure"],
        "provenance_note": "Compilation/source-page check; HTTP failures are retained as explicit provenance risk.",
    },
    {
        "dataset_id": "real_cmb_shift",
        "local_path": "data/real/CMB_shift_real.json",
        "source_url": "https://arxiv.org/abs/1807.06209",
        "required_terms": ["Planck", "cosmological parameters"],
        "provenance_note": "Planck 2018 source check for CMB-shift summary values.",
    },
    {
        "dataset_id": "real_cmb_shift_covariance",
        "local_path": "data/real/CMB_shift_real.json",
        "source_url": "https://arxiv.org/abs/1808.05724",
        "required_terms": ["distance priors", "Planck"],
        "provenance_note": "Chen, Huang & Wang (2019) Table I source check for the R/l_A/Omega_b h^2 mean vector and correlation matrix.",
    },
]


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
    return {"path": _display_path(path), "backup_path": _display_path(backup) if rollback else "", "rollback_available": rollback}


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fp:
        for chunk in iter(lambda: fp.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _fetch_signature(url: str, required_terms: list[str]) -> dict:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "rll-real-source-verifier/1.0 (+local provenance audit)",
            "Range": f"bytes=0-{FETCH_LIMIT - 1}",
        },
    )
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            body = response.read(FETCH_LIMIT)
            text = body.decode("utf-8", errors="ignore")
            headers = response.headers
            terms_found = [term for term in required_terms if term.lower() in text.lower()]
            return {
                "ok": 200 <= int(response.status) < 300,
                "status_code": int(response.status),
                "final_url": response.geturl(),
                "content_type": headers.get("content-type", ""),
                "content_length": headers.get("content-length", ""),
                "etag": headers.get("etag", ""),
                "last_modified": headers.get("last-modified", ""),
                "sample_bytes": len(body),
                "sample_sha256": hashlib.sha256(body).hexdigest(),
                "terms_found": terms_found,
                "required_terms": required_terms,
                "required_terms_ok": len(terms_found) == len(required_terms),
                "elapsed_seconds": time.perf_counter() - started,
                "error": "",
            }
    except urllib.error.HTTPError as exc:
        return {
            "ok": False,
            "status_code": int(exc.code),
            "final_url": url,
            "content_type": exc.headers.get("content-type", "") if exc.headers else "",
            "content_length": exc.headers.get("content-length", "") if exc.headers else "",
            "etag": exc.headers.get("etag", "") if exc.headers else "",
            "last_modified": exc.headers.get("last-modified", "") if exc.headers else "",
            "sample_bytes": 0,
            "sample_sha256": "",
            "terms_found": [],
            "required_terms": required_terms,
            "required_terms_ok": False,
            "elapsed_seconds": time.perf_counter() - started,
            "error": f"HTTPError: {exc.code}",
        }
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {
            "ok": False,
            "status_code": 0,
            "final_url": url,
            "content_type": "",
            "content_length": "",
            "etag": "",
            "last_modified": "",
            "sample_bytes": 0,
            "sample_sha256": "",
            "terms_found": [],
            "required_terms": required_terms,
            "required_terms_ok": False,
            "elapsed_seconds": time.perf_counter() - started,
            "error": f"{type(exc).__name__}: {exc}",
        }


def verify_sources() -> dict:
    rows = []
    for source in SOURCES:
        local_path = BASE_DIR / source["local_path"]
        fetch = _fetch_signature(source["source_url"], list(source["required_terms"]))
        local_exists = local_path.exists()
        row = {
            **source,
            "local_exists": local_exists,
            "local_sha256": _sha256_file(local_path) if local_exists else "",
            "verified_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "source_signature": fetch,
            "status": "source_verified" if fetch["ok"] and fetch["required_terms_ok"] and local_exists else "source_needs_review",
            "failover_policy": "keep committed local file and previous output; do not replace with partial download; inspect status/error before promotion",
        }
        rows.append(row)
    return {
        "schema": "rll.real_source_signatures.v1",
        "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "fetch_limit_bytes": FETCH_LIMIT,
        "rows": rows,
    }


def _md(payload: dict) -> str:
    verified = sum(1 for row in payload["rows"] if row["status"] == "source_verified")
    review = len(payload["rows"]) - verified
    lines = [
        "# Real source signature verification",
        "",
        f"- Sources verified: {verified}",
        f"- Sources needing review/failover: {review}",
        f"- Fetch limit per URL: {payload['fetch_limit_bytes']} bytes",
        "",
        "| dataset_id | status | status_code | local_path | source_url |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in payload["rows"]:
        sig = row["source_signature"]
        lines.append(f"| {row['dataset_id']} | {row['status']} | {sig['status_code']} | {row['local_path']} | {row['source_url']} |")
    lines.extend([
        "",
        "## Failsafe",
        "",
        "If a source is blocked or a required term is absent, keep the committed local file, mark the row as needing review, and do not fabricate replacement data.",
    ])
    return "\n".join(lines) + "\n"


def run_verification() -> dict:
    payload = verify_sources()
    outputs = [
        _atomic_write(SIGNATURE_JSON, json.dumps(payload, ensure_ascii=False, indent=2) + "\n"),
        _atomic_write(RESULT_JSON, json.dumps(payload, ensure_ascii=False, indent=2) + "\n"),
        _atomic_write(RESULT_MD, _md(payload)),
    ]
    payload["outputs"] = outputs
    return payload


def main() -> dict:
    payload = run_verification()
    verified = sum(1 for row in payload["rows"] if row["status"] == "source_verified")
    print(f"Verified {verified}/{len(payload['rows'])} source signatures")
    for output in payload["outputs"]:
        print(f"Wrote: {output['path']}")
    return payload


if __name__ == "__main__":
    main()
