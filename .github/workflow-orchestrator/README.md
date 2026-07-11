# Workflow Orchestrator Catalog

This directory centralizes the evolvable orchestration structure for GitHub Actions workflows.

- `session.yml` is the single orchestrator entry file (profiles + directories to load).
- `workflows/` is the modular directory tree with nested manifests that replace direct listing in one monolithic catalog.
- `tools/workflow_orchestrator.py` reads `session.yml`, expands `workflow_catalog_dirs`, and dispatches workflows as one unified session.
