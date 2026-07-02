from __future__ import annotations

import importlib.util
import json
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "import_raw_json_dataset.py"
SPEC = importlib.util.spec_from_file_location("import_raw_json_dataset", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
importer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(importer)


def test_import_object_json_writes_manifest_checksum_and_boundary(tmp_path: Path) -> None:
    source = tmp_path / "source.json"
    source.write_text(json.dumps({"z": 0.1, "value": 42}), encoding="utf-8")
    out = tmp_path / "raw"

    manifest = importer.import_json(source, out, "dataset-alpha")

    assert manifest["dataset_id"] == "dataset-alpha"
    assert manifest["status"] == "RAW_JSON_IMPORTED_STRUCTURAL_ONLY"
    assert manifest["autodetected_shape"]["json_type"] == "object"
    assert "does not validate RLL" in manifest["claim_boundary"]
    assert (out / "dataset-alpha.raw.json").exists()
    assert (out / "dataset-alpha.MANIFEST.json").exists()
    assert (out / "dataset-alpha.CHECKSUMS.sha256").exists()
