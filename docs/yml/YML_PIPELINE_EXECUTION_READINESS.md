# YML PIPELINE EXECUTION READINESS

Gerado em: `2026-06-26T20:06:17Z`  
Commit auditado: `623c7be20f0952cd5769615032f8d2d68a1a23e8`

## Objetivo operacional

Este mapa responde ao caminho pedido: cada YAML é tratado como contrato de execução ou metadata; quando ele referencia `.py` ou `.sh`, o caminho é explicitado com gate de sintaxe, entrypoint e rollback/failsafe. O documento não executa efeitos destrutivos e não promove dado científico.

## Gates executados

- YAML parser: `python3 -c ... yaml.safe_load(...)`
- Python: `python3 -m py_compile $(find scripts data/pipelines validacao_real tools -name "*.py" 2>/dev/null)`
- Shell: `find scripts -name "*.sh" -print0 2>/dev/null | xargs -0 -r bash -n`
- Workflow hygiene: `python3 tools/audit_github_workflows.py --strict`

## YAML -> SH/PY

| yaml | tipo | scripts SH/PY referenciados | status | rollback/failsafe |
|---|---|---|---|---|
| `.github/workflows/START_MANUAL_HERE.yml` | workflow | `scripts/rll_pipeline.py, tools/audit_github_workflows.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/academic-parameter-governance.yml` | workflow | `tools/apply_rll_outcome_protocol.py, tools/check_rll_report_claim_language.py, tools/make_h0_rd_ablation_matrix.py, tools/run_rll_academic_claim_governance.py, tools/scan_rll_model_evidence.py, tools/validate_academic_parameter_registry.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/canonical-route-artifacts.yml` | workflow | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/claim-boundary-quality-gates.yml` | workflow | `scripts/validation/check_claim_boundary.py, scripts/validation/check_seed_artifact_contracts.py, scripts/validation/real_seed_utils.py, scripts/validation/validate_orbital_shape_angular_momentum.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/convention-check.yml` | workflow | `scripts/check_convention_conflicts.sh, scripts/check_structure_d_model_dataset_coverage.sh, scripts/check_structure_d_required_outputs.sh, tools/docs_inventory.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/dense-feature-matrix.yml` | workflow | `scripts/data_scan/build_dense_behavior_features.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/desi-dr2-bao-validation.yml` | workflow | `scripts/check_desi_dr2_bao_covariance.py, scripts/smoke_desi_dr2_bao_covariance_loader.py, tests/test_desi_dr2_bao_covariance_loader.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/dha-fisher-ci.yml` | workflow | `scripts/export_dha_forecast.py, scripts/run_desi_dha_pipeline.py, scripts/run_ln1pz_extractor.py, tests/test_desi_dha_extractor.py, tests/test_dha_fisher.py, tests/test_ln1pz_extractor.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/formulas-artifacts-validation.yml` | workflow | `scripts/materialize_formula_index.py, scripts/validate_formula_index_contract.py, scripts/validate_formulas_manifest.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/formulas-artifacts.yml` | workflow | `tools/formula_artifact_builder.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/iml_artifact.yml` | workflow | `tools/iml/iml_pipeline.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/orbital-shape-angular-momentum-validation.yml` | workflow | `scripts/validation/validate_orbital_shape_angular_momentum.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/orbital-state-vector-v2.yml` | workflow | `scripts/data_scan/fetch_horizons_mars_state_vector.py, scripts/validation/validate_orbital_state_vector_v2.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/python-tests.yml` | workflow | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/raw-data-manifest-status.yml` | workflow | `scripts/data_scan/build_raw_data_manifest_status.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/real-data-bootstrap-validation.yml` | workflow | `scripts/data_scan/scan_real_data_bootstrap.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/real-data-complete-execution.yml` | workflow | `scripts/download_real_cosmology_inputs.sh, scripts/run_real_pantheon_validation.py, scripts/verify_pantheon_inputs.py, tools/real_data_materialization_audit.py, tools/verify_real_source_signatures.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/real-data-contract-ci.yml` | workflow | `scripts/compute_rll_real_pipeline.py, scripts/fetch_real_sources.py, tests/test_compute_rll_real_pipeline_contract.py, tests/test_desi_dr2_bao_materialized.py, tools/docs_inventory.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/real-seed-ingestion-plan.yml` | workflow | `scripts/data_scan/build_real_seed_ingestion_plan.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/real-seed-validation-v0.yml` | workflow | `scripts/validation/real_seed_utils.py, scripts/validation/run_real_seed_validations.py, scripts/validation/validate_compact_remnant_boundary.py, scripts/validation/validate_dark_lens_candidates.py, scripts/validation/validate_high_z_smbh_seeds.py, scripts/validation/validate_historical_impulse_candidates.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/repo-real-inventory.yml` | workflow | `tools/docs_inventory.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/rll-book-data-pipeline.yml` | workflow | `scripts/rll_pipeline.py, tools/docs_inventory.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/rll-data-pipeline.yml` | workflow | `scripts/rll_pipeline.py, tools/docs_inventory.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/rll-real-data-orchestrator.yml` | workflow | `scripts/compute_rll_real_pipeline.py, scripts/fetch_real_sources.py, scripts/generate_rll_plots.py, scripts/rll_pipeline.py, tools/docs_inventory.py, tools/formula_artifact_builder.py, tools/iml/iml_pipeline.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/unified-geometry.yml` | workflow | `scripts/unified_geometry_system.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/validacao_real.yml` | workflow | `validacao_real/compute_validation.py, validacao_real/fetch_real_data.py, validacao_real/make_figures.py, validacao_real/render_report.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `.github/workflows/yml-syntax-validation.yml` | workflow | `tools/audit_github_workflows.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `CAMINHOS_VALIDACAO_NOVOS.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `data/observational_sources.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `data/raw/RAW_DATA_MANIFEST.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_observer_2006_sample.meta.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `data/real/bootstrap/canonical_route_checklist.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `data/real/bootstrap/dense_behavior_feature_orchestration.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `data/real/bootstrap/real_data_requirements_bootstrap.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `data/real/bootstrap/real_observational_seed_v0.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `data/real/bootstrap/real_observational_seed_v1.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `data/real/bootstrap/real_seed_pipeline_orchestration.yml` | data_config | `scripts/validation/validate_compact_remnant_boundary.py, scripts/validation/validate_dark_lens_candidates.py, scripts/validation/validate_high_z_smbh_seeds.py, scripts/validation/validate_historical_impulse_candidates.py, scripts/validation/validate_orbital_shape_angular_momentum.py, scripts/validation/validate_residual_gravity_structures.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `data/real/compact_objects/remnant_boundary_sources.yml` | data_config | `scripts/validation/validate_compact_remnant_boundary.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `data/real/compact_objects/wandering_black_hole_sources.yml` | data_config | `scripts/validation/validate_dark_lens_candidates.py, scripts/validation/validate_wandering_bh_candidates.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `data/real/cosmology/DESI_BAO_MATH_ARTIFACTS.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `data/real/cosmology/RLL_COSMO_VALIDATION_MATRIX.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `data/real/high_z_smbh/high_z_seed_sources.yml` | data_config | `scripts/validation/validate_high_z_smbh_seeds.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `data/real/kinematics/hypervelocity_sources.yml` | data_config | `scripts/validation/validate_historical_impulse_candidates.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `data/real/lensing/dark_lens_sources.yml` | data_config | `scripts/validation/validate_dark_lens_candidates.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `data/real/orbital_dynamics/angular_momentum_shape_sources.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `data/real/orbital_dynamics/orbital_shape_angular_momentum_seed_v1.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `data/real/rll_real_sources_manifest_2026.yml` | data_config | `scripts/run_real_pantheon_validation.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `data/real/structure/residual_gravity_sources.yml` | data_config | `scripts/validation/validate_residual_gravity_structures.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `data/real_sources/rll_pantheon_real_validation.iml.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `data/real_sources/rll_real_orchestrator_inventory.iml.yml` | data_config | `data/pipelines/structure_d/joint_real_likelihood.py, scripts/compute_desi_dr2_bao_zml.py, scripts/download_real_cosmology_inputs.sh, scripts/run_real_pantheon_validation.py, scripts/verify_pantheon_inputs.py, tools/audit_github_workflows.py, tools/iml/iml_pipeline.py, tools/real_data_materialization_audit.py, tools/verify_real_source_signatures.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `data/results/desi_dr2_bao_zml.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `data/rll_latentes/examples/invalid_missing_falsifier.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `data/rll_latentes/examples/valid_minimal.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `data/rll_latentes/observations.yml` | data_config | `scripts/fetch_real_sources.py` | scripts_mapeados | não executar mutação; usar commit revert e artefatos versionados |
| `data/strong_lensing_imf/strong_lensing_imf_benchmark_seed_2026.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `docs/pipelines/validation_paths/CAMINHOS_VALIDACAO_NOVOS.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `knowledge_ecosystem/reference_seed_sources.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `knowledge_ecosystem/source_search_queue.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `rll_equation_registry.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `rll_inovacao_tecnologica_watch.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `tools/inventory_config.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `validacao_real/data/desi_dr2_bao.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `validacao_real/data/hz_cosmic_chronometers.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `validacao_real/fetched/desi_dr2_bao.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `validacao_real/fetched/hz_cosmic_chronometers.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |
| `validacao_real/sources.yml` | data_config | `TOKEN_VAZIO` | sem_script_direto_metadata_only | não executar mutação; usar commit revert e artefatos versionados |

## SH/PY -> consumidores YAML

| script | consumidores YAML | existe | gate sintaxe | entrypoint | rollback |
|---|---|---:|---|---:|---|
| `data/pipelines/structure_d/joint_real_likelihood.py` | `data/real_sources/rll_real_orchestrator_inventory.iml.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/check_convention_conflicts.sh` | `.github/workflows/convention-check.yml` | True | `bash -n` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/check_desi_dr2_bao_covariance.py` | `.github/workflows/desi-dr2-bao-validation.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/check_structure_d_model_dataset_coverage.sh` | `.github/workflows/convention-check.yml` | True | `bash -n` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/check_structure_d_required_outputs.sh` | `.github/workflows/convention-check.yml` | True | `bash -n` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/compute_desi_dr2_bao_zml.py` | `data/real_sources/rll_real_orchestrator_inventory.iml.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/compute_rll_real_pipeline.py` | `.github/workflows/real-data-contract-ci.yml, .github/workflows/rll-real-data-orchestrator.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/data_scan/build_dense_behavior_features.py` | `.github/workflows/dense-feature-matrix.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/data_scan/build_raw_data_manifest_status.py` | `.github/workflows/raw-data-manifest-status.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/data_scan/build_real_seed_ingestion_plan.py` | `.github/workflows/real-seed-ingestion-plan.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/data_scan/fetch_horizons_mars_state_vector.py` | `.github/workflows/orbital-state-vector-v2.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/data_scan/scan_real_data_bootstrap.py` | `.github/workflows/real-data-bootstrap-validation.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/download_real_cosmology_inputs.sh` | `.github/workflows/real-data-complete-execution.yml, data/real_sources/rll_real_orchestrator_inventory.iml.yml` | True | `bash -n` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/export_dha_forecast.py` | `.github/workflows/dha-fisher-ci.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/fetch_real_sources.py` | `.github/workflows/real-data-contract-ci.yml, .github/workflows/rll-real-data-orchestrator.yml, data/rll_latentes/observations.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/generate_rll_plots.py` | `.github/workflows/rll-real-data-orchestrator.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/materialize_formula_index.py` | `.github/workflows/formulas-artifacts-validation.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/rll_pipeline.py` | `.github/workflows/START_MANUAL_HERE.yml, .github/workflows/rll-book-data-pipeline.yml, .github/workflows/rll-data-pipeline.yml, .github/workflows/rll-real-data-orchestrator.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/run_desi_dha_pipeline.py` | `.github/workflows/dha-fisher-ci.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/run_ln1pz_extractor.py` | `.github/workflows/dha-fisher-ci.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/run_real_pantheon_validation.py` | `.github/workflows/real-data-complete-execution.yml, data/real/rll_real_sources_manifest_2026.yml, data/real_sources/rll_real_orchestrator_inventory.iml.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/smoke_desi_dr2_bao_covariance_loader.py` | `.github/workflows/desi-dr2-bao-validation.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/unified_geometry_system.py` | `.github/workflows/unified-geometry.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/validate_formula_index_contract.py` | `.github/workflows/formulas-artifacts-validation.yml` | True | `python3 -m py_compile` | False | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/validate_formulas_manifest.py` | `.github/workflows/formulas-artifacts-validation.yml` | True | `python3 -m py_compile` | False | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/validation/check_claim_boundary.py` | `.github/workflows/claim-boundary-quality-gates.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/validation/check_seed_artifact_contracts.py` | `.github/workflows/claim-boundary-quality-gates.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/validation/real_seed_utils.py` | `.github/workflows/claim-boundary-quality-gates.yml, .github/workflows/real-seed-validation-v0.yml` | True | `python3 -m py_compile` | False | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/validation/run_real_seed_validations.py` | `.github/workflows/real-seed-validation-v0.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/validation/validate_compact_remnant_boundary.py` | `.github/workflows/real-seed-validation-v0.yml, data/real/bootstrap/real_seed_pipeline_orchestration.yml, data/real/compact_objects/remnant_boundary_sources.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/validation/validate_dark_lens_candidates.py` | `.github/workflows/real-seed-validation-v0.yml, data/real/bootstrap/real_seed_pipeline_orchestration.yml, data/real/compact_objects/wandering_black_hole_sources.yml, data/real/lensing/dark_lens_sources.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/validation/validate_high_z_smbh_seeds.py` | `.github/workflows/real-seed-validation-v0.yml, data/real/bootstrap/real_seed_pipeline_orchestration.yml, data/real/high_z_smbh/high_z_seed_sources.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/validation/validate_historical_impulse_candidates.py` | `.github/workflows/real-seed-validation-v0.yml, data/real/bootstrap/real_seed_pipeline_orchestration.yml, data/real/kinematics/hypervelocity_sources.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/validation/validate_orbital_shape_angular_momentum.py` | `.github/workflows/claim-boundary-quality-gates.yml, .github/workflows/orbital-shape-angular-momentum-validation.yml, data/real/bootstrap/real_seed_pipeline_orchestration.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/validation/validate_orbital_state_vector_v2.py` | `.github/workflows/orbital-state-vector-v2.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/validation/validate_residual_gravity_structures.py` | `data/real/bootstrap/real_seed_pipeline_orchestration.yml, data/real/structure/residual_gravity_sources.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/validation/validate_wandering_bh_candidates.py` | `data/real/compact_objects/wandering_black_hole_sources.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `scripts/verify_pantheon_inputs.py` | `.github/workflows/real-data-complete-execution.yml, data/real_sources/rll_real_orchestrator_inventory.iml.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `tests/test_compute_rll_real_pipeline_contract.py` | `.github/workflows/real-data-contract-ci.yml` | True | `python3 -m py_compile` | False | reverter commit/artefato do consumidor; preservar inputs originais |
| `tests/test_desi_dha_extractor.py` | `.github/workflows/dha-fisher-ci.yml` | True | `python3 -m py_compile` | False | reverter commit/artefato do consumidor; preservar inputs originais |
| `tests/test_desi_dr2_bao_covariance_loader.py` | `.github/workflows/desi-dr2-bao-validation.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `tests/test_desi_dr2_bao_materialized.py` | `.github/workflows/real-data-contract-ci.yml` | True | `python3 -m py_compile` | False | reverter commit/artefato do consumidor; preservar inputs originais |
| `tests/test_dha_fisher.py` | `.github/workflows/dha-fisher-ci.yml` | True | `python3 -m py_compile` | False | reverter commit/artefato do consumidor; preservar inputs originais |
| `tests/test_ln1pz_extractor.py` | `.github/workflows/dha-fisher-ci.yml` | True | `python3 -m py_compile` | False | reverter commit/artefato do consumidor; preservar inputs originais |
| `tools/apply_rll_outcome_protocol.py` | `.github/workflows/academic-parameter-governance.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `tools/audit_github_workflows.py` | `.github/workflows/START_MANUAL_HERE.yml, .github/workflows/yml-syntax-validation.yml, data/real_sources/rll_real_orchestrator_inventory.iml.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `tools/check_rll_report_claim_language.py` | `.github/workflows/academic-parameter-governance.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `tools/docs_inventory.py` | `.github/workflows/convention-check.yml, .github/workflows/real-data-contract-ci.yml, .github/workflows/repo-real-inventory.yml, .github/workflows/rll-book-data-pipeline.yml, .github/workflows/rll-data-pipeline.yml, .github/workflows/rll-real-data-orchestrator.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `tools/formula_artifact_builder.py` | `.github/workflows/formulas-artifacts.yml, .github/workflows/rll-real-data-orchestrator.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `tools/iml/iml_pipeline.py` | `.github/workflows/iml_artifact.yml, .github/workflows/rll-real-data-orchestrator.yml, data/real_sources/rll_real_orchestrator_inventory.iml.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `tools/make_h0_rd_ablation_matrix.py` | `.github/workflows/academic-parameter-governance.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `tools/real_data_materialization_audit.py` | `.github/workflows/real-data-complete-execution.yml, data/real_sources/rll_real_orchestrator_inventory.iml.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `tools/run_rll_academic_claim_governance.py` | `.github/workflows/academic-parameter-governance.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `tools/scan_rll_model_evidence.py` | `.github/workflows/academic-parameter-governance.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `tools/validate_academic_parameter_registry.py` | `.github/workflows/academic-parameter-governance.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `tools/verify_real_source_signatures.py` | `.github/workflows/real-data-complete-execution.yml, data/real_sources/rll_real_orchestrator_inventory.iml.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `validacao_real/compute_validation.py` | `.github/workflows/validacao_real.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `validacao_real/fetch_real_data.py` | `.github/workflows/validacao_real.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `validacao_real/make_figures.py` | `.github/workflows/validacao_real.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |
| `validacao_real/render_report.py` | `.github/workflows/validacao_real.yml` | True | `python3 -m py_compile` | True | reverter commit/artefato do consumidor; preservar inputs originais |

## Política failsafe/failover/rollback

| caso | mitigação | rollback |
|---|---|---|
| script inexistente | status `BLOQUEADO_ARQUIVO_INEXISTENTE`; não executar | corrigir caminho ou remover referência |
| syntax gate falha | bloquear PR e preservar artefatos anteriores | `git revert` do commit que alterou o consumidor |
| workflow com `contents: write` | exigir justificativa e input explícito em PR futuro | reverter workflow específico |
| metadata sem script direto | manter `metadata_ready`; não inferir execução | adicionar `consumed_by` documental |
| dado mock/synthetic/example | manter rótulo de fronteira; nunca promover para real | remover promoção e regenerar auditoria |
