from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "calculate_sequence_metrics.py"


def load_module():
    spec = importlib.util.spec_from_file_location("calculate_sequence_metrics", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_sequence_metrics_outputs_manifest_and_metrics(tmp_path: Path) -> None:
    module = load_module()
    fasta = tmp_path / "sample.fasta"
    fasta.write_text(">seq1\nACGTACGT\n>seq2\nACGTTCGT\n", encoding="utf-8")

    manifest = module.run(fasta, "sample evolutionary input", tmp_path / "out")

    assert manifest["status"] == "CALCULATED_CLAIM_BOUNDED"
    assert "does not validate RLL" in manifest["claim_boundary"]

    metrics_path = Path(manifest["artifacts"]["metrics_json"])
    metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
    assert metrics["record_summary"]["sequence_count"] == 2
    assert metrics["record_summary"]["total_bases"] == 16
    assert metrics["pairwise_summary"]["pairs_emitted"] == 1
    assert metrics["pairwise_summary"]["mean_p_distance"] == 0.125


def test_sequence_metrics_skips_unequal_lengths(tmp_path: Path) -> None:
    module = load_module()
    fasta = tmp_path / "sample.fasta"
    fasta.write_text(">seq1\nACGT\n>seq2\nACGTA\n", encoding="utf-8")

    manifest = module.run(fasta, "unequal", tmp_path / "out")
    pairwise_csv = Path(manifest["artifacts"]["pairwise_csv"]).read_text(encoding="utf-8")

    assert "SKIPPED_UNEQUAL_LENGTH" in pairwise_csv


def test_sequence_metrics_rejects_invalid_fasta(tmp_path: Path) -> None:
    module = load_module()
    fasta = tmp_path / "bad.fasta"
    fasta.write_text("ACGT without header\n", encoding="utf-8")

    try:
        module.run(fasta, "bad", tmp_path / "out")
    except ValueError as exc:
        assert "sequence before FASTA header" in str(exc)
    else:  # pragma: no cover
        raise AssertionError("expected invalid FASTA to fail")
