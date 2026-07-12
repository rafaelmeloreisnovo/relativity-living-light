from __future__ import annotations

import pytest

from tools.workflow_orchestrator import apply_overrides, select_workflows


def test_apply_overrides_updates_only_selected_workflow_inputs() -> None:
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

    assert selected[0].inputs == {"mode": "full", "strict_real_data": True}


@pytest.mark.parametrize(
    "overrides, message",
    [
        ("[]", "JSON object"),
        ('{"missing": {"mode": "full"}}', "unselected workflow"),
        ('{"real_run": "full"}', "must be a JSON object"),
    ],
)
def test_apply_overrides_rejects_invalid_values(
    overrides: str, message: str
) -> None:
    selected = [
        select_workflows(
            {
                "profiles": {"real": {"include_tags": ["real_data"]}},
                "workflows": [
                    {"id": "real_run", "file": "real.yml", "tags": ["real_data"]}
                ],
            },
            "real",
        )[0]
    ]

    with pytest.raises(ValueError, match=message):
        apply_overrides(selected, overrides)
