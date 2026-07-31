from __future__ import annotations

import copy
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_cosmological_photonic_manifest import ContractError, validate_manifest  # noqa: E402

EXAMPLE_PATH = ROOT / "data" / "observational" / "examples" / "cosmological_photonic_observation.example.json"


class PhotonicManifestContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.example = json.loads(EXAMPLE_PATH.read_text(encoding="utf-8"))

    def test_public_safe_example_passes(self) -> None:
        validate_manifest(copy.deepcopy(self.example))

    def test_rendered_image_requires_channel_mapping(self) -> None:
        candidate = copy.deepcopy(self.example)
        candidate["visualization"]["channel_mapping"] = {}
        with self.assertRaises(ContractError):
            validate_manifest(candidate)

    def test_hypothesis_cannot_enable_claim(self) -> None:
        candidate = copy.deepcopy(self.example)
        candidate["claim_state"] = "HYPOTHESIS"
        candidate["claim_allowed"] = True
        with self.assertRaises(ContractError):
            validate_manifest(candidate)

    def test_evidence_state_cannot_enable_public_claim(self) -> None:
        candidate = copy.deepcopy(self.example)
        candidate["claim_state"] = "EVIDENCE"
        candidate["claim_allowed"] = True
        with self.assertRaises(ContractError):
            validate_manifest(candidate)

    def test_authorial_dark_hypothesis_requires_definition(self) -> None:
        candidate = copy.deepcopy(self.example)
        candidate["dark_sector_interpretation"] = {
            "state": "AUTHORIAL_HYPOTHESIS",
            "operational_definition": None,
            "claim_allowed": False
        }
        with self.assertRaises(ContractError):
            validate_manifest(candidate)

    def test_forbidden_private_field_is_rejected(self) -> None:
        candidate = copy.deepcopy(self.example)
        candidate["raw_conversation"] = "private"
        with self.assertRaises(ContractError):
            validate_manifest(candidate)


if __name__ == "__main__":
    unittest.main()
