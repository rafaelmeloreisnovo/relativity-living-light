from pathlib import Path

import yaml

from tools.workflow_orchestrator import load_and_expand_catalog, select_workflows

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / ".github/workflow-orchestrator/session.yml"
SESSION_WORKFLOW = ROOT / ".github/workflows/unified-workflow-session-orchestrator.yml"


def test_catalog_uses_only_explicit_manifests_and_single_flight_execution():
    raw = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
    assert "workflow_files" not in raw
    assert raw["execution"] == {
        "mode": "sequential",
        "stage_barrier": True,
        "max_in_flight": 1,
    }
    catalog = load_and_expand_catalog(CATALOG)
    assert len(catalog["workflows"]) == 8
    assert len({item["file"] for item in catalog["workflows"]}) == 8


def test_profiles_select_bounded_workflow_sets_and_budgets():
    catalog = load_and_expand_catalog(CATALOG)
    expected = {
        "full_session": (
            {
                "yml_syntax_validation",
                "start_manual_interop",
                "real_data_complete_execution",
                "rll_real_data_orchestrator",
                "formulas_artifacts",
                "iml_artifact",
                "academic_correlation_package",
            },
            260,
        ),
        "quick_session": ({"yml_syntax_validation"}, 20),
        "real_data_session": (
            {
                "start_manual_interop",
                "real_data_complete_execution",
                "rll_real_data_orchestrator",
            },
            165,
        ),
        "science_session": (
            {"formulas_artifacts", "iml_artifact", "academic_correlation_package"},
            75,
        ),
        "frontier_session": ({"frontier_research_omega"}, 190),
        "literature_session": ({"academic_correlation_package"}, 15),
        "pages_preview_session": ({"academic_correlation_package"}, 15),
    }
    for profile, (expected_ids, expected_budget) in expected.items():
        selected = select_workflows(catalog, profile)
        assert {workflow.workflow_id for workflow in selected} == expected_ids
        assert sum(workflow.timeout_minutes for workflow in selected) == expected_budget
        assert [workflow.stage for workflow in selected] == sorted(
            workflow.stage for workflow in selected
        )
        assert expected_budget <= 320

    assert "frontier_research_omega" not in {
        workflow.workflow_id for workflow in select_workflows(catalog, "full_session")
    }


def test_manual_profile_choices_match_catalog_profiles_and_budget():
    catalog = load_and_expand_catalog(CATALOG)
    workflow = yaml.safe_load(SESSION_WORKFLOW.read_text(encoding="utf-8"))
    trigger = workflow.get("on", workflow.get(True, {}))
    choices = trigger["workflow_dispatch"]["inputs"]["profile"]["options"]
    assert choices == list(catalog["profiles"])
    job = workflow["jobs"]["orchestrate-workflow-session"]
    assert job["timeout-minutes"] == 320
    assert job["timeout-minutes"] < 360
    run_step = next(
        step for step in job["steps"] if step["name"] == "Run unified workflow orchestration"
    )
    run_text = run_step["run"]
    assert '--ref "$SESSION_REF"' in run_text
    assert '--overrides "$SESSION_OVERRIDES"' in run_text
    assert "${{ inputs.ref }}" not in run_text
