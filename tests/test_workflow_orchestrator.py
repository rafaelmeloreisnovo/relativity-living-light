from __future__ import annotations

import unittest

from tools.workflow_orchestrator import apply_overrides, select_workflows


class WorkflowOrchestratorTests(unittest.TestCase):
    def test_apply_overrides_updates_only_selected_workflow_inputs(self) -> None:
        catalog = {
            "profiles": {"real": {"include_tags": ["real_data"]}},
            "workflows": [
                {
                    "id": "real_run",
                    "file": "real.yml",
                    "tags": ["real_data"],
                    "inputs": {"mode": "audit_only"},
                }
            ],
        }

        selected = apply_overrides(
            select_workflows(catalog, "real"),
            '{"real_run": {"mode": "full", "strict_real_data": true}}',
        )

        self.assertEqual(
            selected[0].inputs, {"mode": "full", "strict_real_data": True}
        )

    def test_apply_overrides_rejects_invalid_values(self) -> None:
        selected = select_workflows(
            {
                "profiles": {"real": {"include_tags": ["real_data"]}},
                "workflows": [
                    {"id": "real_run", "file": "real.yml", "tags": ["real_data"]}
                ],
            },
            "real",
        )
        invalid_values = [
            ("[]", "JSON object"),
            ('{"missing": {"mode": "full"}}', "unselected workflow"),
            ('{"real_run": "full"}', "must be a JSON object"),
        ]

        for overrides, message in invalid_values:
            with self.subTest(overrides=overrides):
                with self.assertRaisesRegex(ValueError, message):
                    apply_overrides(selected, overrides)
