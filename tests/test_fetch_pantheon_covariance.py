from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/fetch_pantheon_covariance.py"


def load_module():
    spec = importlib.util.spec_from_file_location("fetch_pantheon_covariance", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git_blob_sha1(payload: bytes) -> str:
    digest = hashlib.sha1(usedforsecurity=False)
    digest.update(f"blob {len(payload)}\0".encode("ascii"))
    digest.update(payload)
    return digest.hexdigest()


def write_matrix(path: Path, dimension: int, values: list[float]) -> bytes:
    payload = (
        f"{dimension}\n" + "\n".join(f"{value:.8e}" for value in values) + "\n"
    ).encode("ascii")
    path.write_bytes(payload)
    return payload


def configure_small_matrix(module, payload: bytes, dimension: int = 2) -> None:
    module.UPSTREAM_GIT_BLOB_SHA1 = git_blob_sha1(payload)
    module.EXPECTED_DIMENSION = dimension
    module.EXPECTED_VALUES = dimension * dimension
    module.EXPECTED_BYTES = len(payload)


def test_git_blob_sha1_matches_git_object_definition(tmp_path: Path) -> None:
    module = load_module()
    payload = b"2\n1\n0\n0\n1\n"
    path = tmp_path / "matrix.cov"
    path.write_bytes(payload)
    assert module.git_blob_sha1(path) == git_blob_sha1(payload)


def test_streaming_shape_inspection_counts_values_and_diagonal(tmp_path: Path) -> None:
    module = load_module()
    path = tmp_path / "matrix.cov"
    write_matrix(path, 2, [1.0, -0.25, -0.25, 2.0])
    shape = module.inspect_covariance(path)
    assert shape == {
        "dimension": 2,
        "values": 4,
        "finite_values": 4,
        "positive_diagonal": 2,
        "minimum": -0.25,
        "maximum": 2.0,
    }


def test_calibration_materializes_atomically_but_is_not_full_ready(tmp_path: Path) -> None:
    module = load_module()
    source = tmp_path / "source.cov"
    payload = write_matrix(source, 2, [1.0, 0.1, 0.1, 1.5])
    configure_small_matrix(module, payload)
    module.EXPECTED_SHA256 = "TOKEN_VAZIO_CALIBRATION"

    output_dir = tmp_path / "output"
    receipt_path = tmp_path / "receipt.json"
    receipt = module.materialize(
        output_dir,
        receipt_path,
        source_url=source.as_uri(),
        expected_sha256="TOKEN_VAZIO_CALIBRATION",
        expected_bytes=len(payload),
        allow_calibration=True,
    )

    final_path = output_dir / module.FILENAME
    assert final_path.read_bytes() == payload
    assert receipt["status"] == "PASS"
    assert receipt["artifact"]["sha256"] == hashlib.sha256(payload).hexdigest()
    assert receipt["policy"]["calibration_only"] is True
    assert receipt["policy"]["full_covariance_likelihood_ready"] is False
    assert receipt["claim_allowed"] is False
    assert final_path.with_name(final_path.name + ".sha256").exists()
    assert not list(output_dir.glob("*.part"))


def test_pinned_materialization_is_full_ready(tmp_path: Path) -> None:
    module = load_module()
    source = tmp_path / "source.cov"
    payload = write_matrix(source, 2, [1.0, 0.0, 0.0, 2.0])
    configure_small_matrix(module, payload)
    expected_sha256 = hashlib.sha256(payload).hexdigest()

    receipt = module.materialize(
        tmp_path / "output",
        tmp_path / "receipt.json",
        source_url=source.as_uri(),
        expected_sha256=expected_sha256,
        expected_bytes=len(payload),
    )
    assert receipt["status"] == "PASS"
    assert receipt["artifact"]["sha256_pinned"] is True
    assert receipt["policy"]["full_covariance_likelihood_ready"] is True
    assert receipt["claim_allowed"] is False


def test_unpinned_policy_fails_without_explicit_calibration(tmp_path: Path) -> None:
    module = load_module()
    source = tmp_path / "source.cov"
    payload = write_matrix(source, 2, [1.0, 0.0, 0.0, 1.0])
    configure_small_matrix(module, payload)

    receipt_path = tmp_path / "receipt.json"
    with pytest.raises(ValueError, match="calibration not authorized"):
        module.materialize(
            tmp_path / "output",
            receipt_path,
            source_url=source.as_uri(),
            expected_sha256="TOKEN_VAZIO_CALIBRATION",
            expected_bytes=len(payload),
        )
    report = json.loads(receipt_path.read_text(encoding="utf-8"))
    assert report["status"] == "FAIL"
    assert report["claim_allowed"] is False


def test_wrong_shape_is_blocked_even_with_correct_hash(tmp_path: Path) -> None:
    module = load_module()
    source = tmp_path / "source.cov"
    payload = write_matrix(source, 2, [1.0, 0.0, 0.0, 1.0])
    module.UPSTREAM_GIT_BLOB_SHA1 = git_blob_sha1(payload)
    module.EXPECTED_DIMENSION = 3
    module.EXPECTED_VALUES = 9

    with pytest.raises(ValueError, match="dimension mismatch"):
        module.materialize(
            tmp_path / "output",
            tmp_path / "receipt.json",
            source_url=source.as_uri(),
            expected_sha256=hashlib.sha256(payload).hexdigest(),
            expected_bytes=len(payload),
        )


def test_non_positive_diagonal_is_blocked(tmp_path: Path) -> None:
    module = load_module()
    source = tmp_path / "source.cov"
    payload = write_matrix(source, 2, [1.0, 0.0, 0.0, 0.0])
    configure_small_matrix(module, payload)

    with pytest.raises(ValueError, match="diagonal covariance"):
        module.materialize(
            tmp_path / "output",
            tmp_path / "receipt.json",
            source_url=source.as_uri(),
            expected_sha256=hashlib.sha256(payload).hexdigest(),
            expected_bytes=len(payload),
        )
