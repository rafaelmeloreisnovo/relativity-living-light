# Workflow Orchestrator Catalog

This directory centralizes the evolvable orchestration structure for GitHub Actions workflows.

- `catalog.yml` defines profiles, ordering stages, tags, and default inputs.
- `tools/workflow_orchestrator.py` reads this catalog and dispatches workflows as one unified session.
