"""Source-only producer boundary tests; no GitHub authentication."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "data" / "governance" / "github_credential_producer_v1.json"

class ProducerCredentialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(PATH.read_text(encoding="utf-8"))

    def test_no_master_pat(self):
        self.assertIs(self.data["accepts_global_admin_pat"], False)
        self.assertEqual(self.data["secret_values"], "NOT_COPIED")
        self.assertEqual(self.data["remote_secret_metadata"], "TOKEN_VAZIO_NOT_ACCESSIBLE")

    def test_authority_routes(self):
        self.assertEqual(self.data["broker"], "rafaelmeloreisnovo/RafGitTools")
        self.assertEqual(self.data["router"], "rafaelmeloreisnovo/Mapa")
        self.assertEqual(self.data["state"], "CANDIDATE_HOLD")
        self.assertIs(self.data["claim_allowed"], False)

if __name__ == "__main__":
    unittest.main()
