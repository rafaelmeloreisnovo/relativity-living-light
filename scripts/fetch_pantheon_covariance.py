#!/usr/bin/env python3
"""Materialize and verify the official Pantheon+SH0ES covariance outside Git.

The upstream object is pinned by repository, commit, path and Git blob SHA-1.
The large matrix is streamed to an atomic temporary file, verified, then moved
into place. Git stores only the fetcher, compact receipt and SHA-256 policy.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import tempfile
import urllib.parse
import urllib.request
from pathlib import Path
from typing import BinaryIO, Iterator

UPSTREAM_REPOSITORY = "PantheonPlusSH0ES/DataRelease"
UPSTREAM_COMMIT = "c447f0fea703fcd0fff57de5000947b5ca81286b"
UPSTREAM_PATH = (
    "Pantheon+_Data/4_DISTANCES_AND_COVAR/"
    "Pantheon+SH0ES_STAT+SYS.cov"
)
UPSTREAM_GIT_BLOB_SHA1 = "d1a1498154e7ba826df14bdbef35ebcb7f5efba1"
FILENAME = "Pantheon+SH0ES_STAT+SYS.cov"
EXPECTED_DIMENSION = 1701
EXPECTED_VALUES = EXPECTED_DIMENSION * EXPECTED_DIMENSION
# Replaced after the calibration workflow measures the pinned official blob.
EXPECTED_SHA256 = "TOKEN_VAZIO_CALIBRATION"
EXPECTED_BYTES: int | None = None
DEFAULT_OUTPUT_DIR = Path(
    "data/real/cosmology/pantheon_plus/"
    "Pantheon+_Data/4_DISTANCES_AND_COVAR"
)
DEFAULT_RECEIPT = Path("artifacts/pantheon/pantheon_covariance_materialization_v1.json")


def raw_url() -> str:
    quoted_path = urllib.parse.quote(UPSTREAM_PATH, safe="/")
    return (
        "https://raw.githubusercontent.com/"
        f"{UPSTREAM_REPOSITORY}/{UPSTREAM_COMMIT}/{quoted_path}"
    )


def git_blob_sha1(path: Path) -> str:
    size = path.stat().st_size
    digest = hashlib.sha1(usedforsecurity=False)
    digest.update(f"blob {size}\0".encode("ascii"))
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_ascii_tokens(handle: BinaryIO, chunk_size: int = 1024 * 1024) -> Iterator[bytes]:
    carry = b""
    while True:
        chunk = handle.read(chunk_size)
        if not chunk:
            break
        data = carry + chunk
        pieces = data.split()
        if data and not data[-1:].isspace():
            carry = pieces.pop() if pieces else data
        else:
            carry = b""
        yield from pieces
    if carry:
        yield carry


def inspect_covariance(path: Path) -> dict[str, object]:
    with path.open("rb") as handle:
        tokens = iter_ascii_tokens(handle)
        try:
            dimension_token = next(tokens)
        except StopIteration as exc:
            raise ValueError("empty covariance file") from exc
        try:
            dimension = int(dimension_token)
        except ValueError as exc:
            raise ValueError("covariance dimension is not an integer") from exc

        values = 0
        finite_values = 0
        positive_diagonal = 0
        minimum = math.inf
        maximum = -math.inf
        for token in tokens:
            try:
                value = float(token)
            except ValueError as exc:
                raise ValueError(f"non-numeric covariance token at index {values}") from exc
            if not math.isfinite(value):
                raise ValueError(f"non-finite covariance value at index {values}")
            row, column = divmod(values, dimension)
            if row == column and value > 0.0:
                positive_diagonal += 1
            minimum = min(minimum, value)
            maximum = max(maximum, value)
            finite_values += 1
            values += 1

    return {
        "dimension": dimension,
        "values": values,
        "finite_values": finite_values,
        "positive_diagonal": positive_diagonal,
        "minimum": minimum,
        "maximum": maximum,
    }


def download_to(url: str, destination: Path, timeout: float = 180.0) -> dict[str, object]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "RLL-Pantheon-Covariance-Materializer/1",
            "Accept": "application/octet-stream",
        },
    )
    sha256 = hashlib.sha256()
    total = 0
    with urllib.request.urlopen(request, timeout=timeout) as response, destination.open("wb") as output:
        content_length_header = response.headers.get("Content-Length")
        declared_length = int(content_length_header) if content_length_header else None
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            output.write(chunk)
            sha256.update(chunk)
            total += len(chunk)
        output.flush()
        os.fsync(output.fileno())
    if declared_length is not None and declared_length != total:
        raise ValueError(
            f"download length mismatch: declared={declared_length} actual={total}"
        )
    return {
        "bytes": total,
        "sha256": sha256.hexdigest(),
        "declared_bytes": declared_length,
    }


def materialize(
    output_dir: Path,
    receipt_path: Path,
    *,
    source_url: str | None = None,
    expected_sha256: str = EXPECTED_SHA256,
    expected_bytes: int | None = EXPECTED_BYTES,
    allow_calibration: bool = False,
) -> dict[str, object]:
    output_dir.mkdir(parents=True, exist_ok=True)
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    final_path = output_dir / FILENAME

    with tempfile.NamedTemporaryFile(
        prefix=f".{FILENAME}.", suffix=".part", dir=output_dir, delete=False
    ) as temp:
        temporary_path = Path(temp.name)
    try:
        transfer = download_to(source_url or raw_url(), temporary_path)
        actual_blob_sha1 = git_blob_sha1(temporary_path)
        actual_sha256 = str(transfer["sha256"])
        actual_bytes = int(transfer["bytes"])
        shape = inspect_covariance(temporary_path)

        errors: list[str] = []
        if actual_blob_sha1 != UPSTREAM_GIT_BLOB_SHA1:
            errors.append("official Git blob SHA-1 mismatch")
        if shape["dimension"] != EXPECTED_DIMENSION:
            errors.append("covariance dimension mismatch")
        if shape["values"] != EXPECTED_VALUES:
            errors.append("covariance value-count mismatch")
        if shape["finite_values"] != EXPECTED_VALUES:
            errors.append("non-finite covariance values detected")
        if shape["positive_diagonal"] != EXPECTED_DIMENSION:
            errors.append("not every diagonal covariance value is positive")
        if expected_bytes is not None and actual_bytes != expected_bytes:
            errors.append("byte-count mismatch")

        sha256_pinned = expected_sha256 != "TOKEN_VAZIO_CALIBRATION"
        if sha256_pinned and actual_sha256 != expected_sha256:
            errors.append("SHA-256 mismatch")
        elif not sha256_pinned and not allow_calibration:
            errors.append("SHA-256 policy is TOKEN_VAZIO; calibration not authorized")

        status = "PASS" if not errors else "FAIL"
        receipt: dict[str, object] = {
            "schema": "rll_pantheon_covariance_materialization_v1",
            "status": status,
            "claim_allowed": False,
            "source": {
                "repository": UPSTREAM_REPOSITORY,
                "commit": UPSTREAM_COMMIT,
                "path": UPSTREAM_PATH,
                "git_blob_sha1_expected": UPSTREAM_GIT_BLOB_SHA1,
                "git_blob_sha1_actual": actual_blob_sha1,
                "url": source_url or raw_url(),
            },
            "artifact": {
                "filename": FILENAME,
                "bytes": actual_bytes,
                "sha256": actual_sha256,
                "sha256_expected": expected_sha256,
                "sha256_pinned": sha256_pinned,
                **shape,
            },
            "policy": {
                "matrix_committed_to_git": False,
                "sidecar_written": status == "PASS",
                "full_covariance_likelihood_ready": status == "PASS" and sha256_pinned,
                "calibration_only": not sha256_pinned,
                "claim_allowed": False,
            },
            "errors": errors,
        }
        receipt_path.write_text(
            json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        if errors:
            raise ValueError("; ".join(errors))

        os.replace(temporary_path, final_path)
        sidecar = final_path.with_name(final_path.name + ".sha256")
        sidecar.write_text(f"{actual_sha256}  {final_path.name}\n", encoding="utf-8")
        return receipt
    finally:
        if temporary_path.exists():
            temporary_path.unlink()


def verify_existing(
    covariance_path: Path,
    receipt_path: Path,
    *,
    expected_sha256: str = EXPECTED_SHA256,
    expected_bytes: int | None = EXPECTED_BYTES,
) -> dict[str, object]:
    if not covariance_path.exists():
        raise FileNotFoundError(covariance_path)
    actual_sha256 = sha256_file(covariance_path)
    actual_blob_sha1 = git_blob_sha1(covariance_path)
    shape = inspect_covariance(covariance_path)
    errors: list[str] = []
    if expected_sha256 == "TOKEN_VAZIO_CALIBRATION":
        errors.append("SHA-256 policy is TOKEN_VAZIO")
    elif actual_sha256 != expected_sha256:
        errors.append("SHA-256 mismatch")
    if actual_blob_sha1 != UPSTREAM_GIT_BLOB_SHA1:
        errors.append("official Git blob SHA-1 mismatch")
    if expected_bytes is not None and covariance_path.stat().st_size != expected_bytes:
        errors.append("byte-count mismatch")
    if shape["dimension"] != EXPECTED_DIMENSION or shape["values"] != EXPECTED_VALUES:
        errors.append("covariance shape mismatch")
    if shape["positive_diagonal"] != EXPECTED_DIMENSION:
        errors.append("diagonal positivity mismatch")

    receipt = {
        "schema": "rll_pantheon_covariance_materialization_v1",
        "status": "PASS" if not errors else "FAIL",
        "claim_allowed": False,
        "mode": "verify_existing",
        "artifact": {
            "path": str(covariance_path),
            "bytes": covariance_path.stat().st_size,
            "sha256": actual_sha256,
            "git_blob_sha1": actual_blob_sha1,
            **shape,
        },
        "errors": errors,
    }
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if errors:
        raise ValueError("; ".join(errors))
    return receipt


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--receipt", type=Path, default=DEFAULT_RECEIPT)
    parser.add_argument("--source-url", default=None)
    parser.add_argument("--allow-calibration", action="store_true")
    parser.add_argument("--verify-existing", type=Path, default=None)
    args = parser.parse_args()

    try:
        if args.verify_existing is not None:
            receipt = verify_existing(args.verify_existing, args.receipt)
        else:
            receipt = materialize(
                args.output_dir,
                args.receipt,
                source_url=args.source_url,
                allow_calibration=args.allow_calibration,
            )
    except (OSError, ValueError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc), "claim_allowed": False}))
        return 2

    print(
        json.dumps(
            {
                "status": receipt["status"],
                "sha256": receipt["artifact"]["sha256"],
                "bytes": receipt["artifact"]["bytes"],
                "dimension": receipt["artifact"]["dimension"],
                "values": receipt["artifact"]["values"],
                "claim_allowed": False,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
