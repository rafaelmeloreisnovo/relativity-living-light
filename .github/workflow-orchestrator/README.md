# Workflow Orchestrator Catalog

This directory centralizes the evolvable orchestration structure for GitHub Actions workflows.

- `session.yml` is the single orchestrator entry file (profiles + directories to load).
- `workflows/` is the modular directory tree with nested manifests that replace direct listing in one monolithic catalog.
- `tools/workflow_orchestrator.py` reads `session.yml`, expands `workflow_catalog_dirs`, and dispatches workflows as one unified session.

## Schema Evolution

- `rll.workflow_orchestrator.catalog.v1`: monolithic `catalog.yml` with inline `workflows`.
- `rll.workflow_orchestrator.catalog.v2`: single entry (`session.yml`) + `workflow_catalog_dirs` that load nested manifest files from directories.
