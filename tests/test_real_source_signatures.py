from __future__ import annotations

from tools import verify_real_source_signatures as verify


def test_source_registry_covers_joint_real_inputs() -> None:
    by_dataset = {row["dataset_id"]: row for row in verify.SOURCES}

    assert by_dataset["real_hz"]["local_path"] == "data/real/Hz_data_real.csv"
    assert by_dataset["real_desi_dr2_bao"]["local_path"] == "data/real/cosmology/desi_dr2_bao_primary_points.csv"
    assert by_dataset["real_fsigma8_6dfgs_anchor"]["local_path"] == "data/real/cosmology/fsigma8_growth_real.csv"
    assert by_dataset["real_cmb_shift"]["local_path"] == "data/real/CMB_shift_real.json"


def test_verification_rows_preserve_failover_on_fetch_failure(monkeypatch) -> None:
    def fake_fetch(_url: str, required_terms: list[str]) -> dict:
        return {
            "ok": False,
            "status_code": 503,
            "final_url": _url,
            "content_type": "",
            "content_length": "",
            "etag": "",
            "last_modified": "",
            "sample_bytes": 0,
            "sample_sha256": "",
            "terms_found": [],
            "required_terms": required_terms,
            "required_terms_ok": False,
            "elapsed_seconds": 0.01,
            "error": "synthetic test outage",
        }

    monkeypatch.setattr(verify, "_fetch_signature", fake_fetch)

    payload = verify.verify_sources()

    assert payload["rows"]
    assert {row["status"] for row in payload["rows"]} == {"source_needs_review"}
    assert all("do not replace" in row["failover_policy"] for row in payload["rows"])


def test_signature_outputs_are_atomic_with_backups(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(verify, "SIGNATURE_JSON", tmp_path / "signatures.json")
    monkeypatch.setattr(verify, "RESULT_JSON", tmp_path / "result.json")
    monkeypatch.setattr(verify, "RESULT_MD", tmp_path / "result.md")
    monkeypatch.setattr(
        verify,
        "verify_sources",
        lambda: {"schema": "test", "fetch_limit_bytes": 1, "rows": []},
    )

    first = verify.run_verification()
    second = verify.run_verification()

    assert len(first["outputs"]) == 3
    assert all(output["rollback_available"] is True for output in second["outputs"])


def test_joint_manifest_points_to_source_signature_artifacts() -> None:
    import json

    manifest = json.loads(open("data/inputs/cosmology_joint/joint_real_inputs_manifest.json", encoding="utf-8").read())

    assert manifest["source_signature_manifest"] == "data/real/cosmology/real_source_signatures.json"
    assert "results/audit/real_source_signature_verification.json" in manifest["source_signature_outputs"]
