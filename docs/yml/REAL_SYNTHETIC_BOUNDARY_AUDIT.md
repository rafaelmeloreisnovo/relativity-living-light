# REAL / SYNTHETIC / MOCK BOUNDARY AUDIT

Gerado em: `2026-06-26T19:52:53Z`  
Commit auditado: `154b8b6d2e1766fa8e630ad143b02c1d4bb34ca0`

## Escopo e comando

FATO_VERIFICADO: varredura YAML/YML por parser e varredura textual de fronteira executadas.  
Comando equivalente amplo solicitado, executado com `rg` por diretriz do ambiente: `rg -n -i "mock|synthetic|sintetico|sintético|placeholder|example|TOKEN_VAZIO|fake|sample|demo" .`.  
Total amplo medido por `wc -l`: `3577`.

## Regra de promoção

RISCO: termos `mock`, `synthetic`, `example`, `placeholder` e `demo` existem no repositório.  
FATO_VERIFICADO: nenhum YAML auditado contém promoção textual direta `real_validated` associada na mesma linha a mock/synthetic/example/placeholder/demo.  
ACAO_RECOMENDADA: manter `real_validated` BLOQUEADO sem dados reais identificados, fonte externa, checksum, comando executado, commit, métrica, baseline, covariância/erro quando aplicável, artefato final e claim boundary.

## Ocorrências em YAML/YML

| arquivo:linha | termo | classificação | trecho |
|---|---|---|---|
| `.github/workflows/START_MANUAL_HERE.yml:37` | `sintético` | risco de contaminação controlado por rótulo | `description: Fonte dos dados reais não sintéticos para cálculo` |
| `.github/workflows/academic-parameter-governance.yml:81` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `python3 tools/apply_rll_outcome_protocol.py --no-write --status TOKEN_VAZIO` |
| `.github/workflows/canonical-route-artifacts.yml:58` | `sample` | risco de contaminação controlado por rótulo | `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv` |
| `.github/workflows/canonical-route-artifacts.yml:59` | `sample` | risco de contaminação controlado por rótulo | `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml` |
| `.github/workflows/canonical-route-artifacts.yml:96` | `sample` | risco de contaminação controlado por rótulo | `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv` |
| `.github/workflows/canonical-route-artifacts.yml:97` | `sample` | risco de contaminação controlado por rótulo | `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml` |
| `.github/workflows/dense-feature-matrix.yml:9` | `token_vazio` | TOKEN_VAZIO protegido | `- "data/results/bootstrap/token_vazio_priority_ledger.json"` |
| `.github/workflows/dense-feature-matrix.yml:18` | `token_vazio` | TOKEN_VAZIO protegido | `- "data/results/bootstrap/token_vazio_priority_ledger.json"` |
| `.github/workflows/dha-fisher-ci.yml:37` | `mock` | risco de contaminação controlado por rótulo | `- name: Build mock catalog for ln(1+z) extraction` |
| `.github/workflows/dha-fisher-ci.yml:46` | `mock` | risco de contaminação controlado por rótulo | `pd.DataFrame({'z': z, 'pk_obs': pk_obs, 'pk_baseline': pk_baseline}).to_csv('results/dha/mock_catalog.csv', index=False)` |
| `.github/workflows/dha-fisher-ci.yml:50` | `mock` | risco de contaminação controlado por rótulo | `run: python scripts/run_ln1pz_extractor.py --input results/dha/mock_catalog.csv --output results/dha/ln1pz_fit.csv --summary results/dha/ln1pz_fit_summary.json` |
| `.github/workflows/iml_artifact.yml:40` | `example` | placeholder/exemplo honesto | `cp data/iml/daise_input.example.json data/iml/daise_input.json` |
| `.github/workflows/orbital-state-vector-v2.yml:61` | `sample` | risco de contaminação controlado por rótulo | `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv` |
| `.github/workflows/orbital-state-vector-v2.yml:62` | `sample` | risco de contaminação controlado por rótulo | `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml` |
| `.github/workflows/real-data-complete-execution.yml:102` | `mock` | risco de contaminação controlado por rótulo | `- Never promote mock/synthetic/example/placeholder files as real data.` |
| `.github/workflows/real-data-complete-execution.yml:133` | `mock` | risco de contaminação controlado por rótulo | `for term in ['dado real', 'checksum', 'mock', 'synthetic', 'Pantheon+SH0ES', 'DESI DR2 BAO']:` |
| `.github/workflows/real-data-complete-execution.yml:217` | `synthetic` | risco de contaminação controlado por rótulo | `'no synthetic promotion',` |
| `.github/workflows/real-data-contract-ci.yml:86` | `synthetic` | risco de contaminação controlado por rótulo | `if manifest.get('status') != 'Real data computed from non-synthetic inputs':` |
| `.github/workflows/real-data-contract-ci.yml:91` | `synthetic` | risco de contaminação controlado por rótulo | `if any(row.get('status') != 'used_real_non_synthetic' for row in inputs):` |
| `.github/workflows/real-data-contract-ci.yml:92` | `synthetic` | risco de contaminação controlado por rótulo | `raise SystemExit('all inputs must be marked used_real_non_synthetic')` |
| `data/observational_sources.yml:31` | `real_validated` | placeholder/exemplo honesto | `evidence_level: real_validated` |
| `data/observational_sources.yml:52` | `real_validated` | placeholder/exemplo honesto | `evidence_level: real_validated` |
| `data/raw/RAW_DATA_MANIFEST.yml:50` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `source_url: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:51` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:52` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `license_or_terms: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:53` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `source_version: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:54` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: data/raw/compact_objects/gw/posteriors/TOKEN_VAZIO_GW190814_posterior.dat` |
| `data/raw/RAW_DATA_MANIFEST.yml:55` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `sha256: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:65` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `source_url: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:66` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:67` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `license_or_terms: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:68` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `source_version: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:69` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: data/raw/compact_objects/gw/posteriors/TOKEN_VAZIO_GW230529_posterior.dat` |
| `data/raw/RAW_DATA_MANIFEST.yml:70` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `sha256: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:80` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `source_url: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:81` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:82` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `license_or_terms: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:83` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `source_version: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:84` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: data/raw/orbital_dynamics/ephemerides/TOKEN_VAZIO_earth_state_vectors.csv` |
| `data/raw/RAW_DATA_MANIFEST.yml:85` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `sha256: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:95` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `source_url: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:96` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:97` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `license_or_terms: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:98` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `source_version: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:99` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: data/raw/orbital_dynamics/ephemerides/TOKEN_VAZIO_mars_state_vectors.csv` |
| `data/raw/RAW_DATA_MANIFEST.yml:100` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `sha256: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:110` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `source_url: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:111` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:112` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `license_or_terms: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:113` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `source_version: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:114` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: data/raw/astrometry/gaia_bh/TOKEN_VAZIO_gaia_bh1_astrometry.csv` |
| `data/raw/RAW_DATA_MANIFEST.yml:115` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `sha256: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:125` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `source_url: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:126` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:127` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `license_or_terms: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:128` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `source_version: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:129` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: data/raw/high_z_smbh/TOKEN_VAZIO_uhz1_context_table.csv` |
| `data/raw/RAW_DATA_MANIFEST.yml:130` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `sha256: TOKEN_VAZIO` |
| `data/raw/RAW_DATA_MANIFEST.yml:137` | `SAMPLE` | risco de contaminação controlado por rótulo | `- raw_id: RAW_JPL_HORIZONS_MARS_OBSERVER_2006_SAMPLE` |
| `data/raw/RAW_DATA_MANIFEST.yml:144` | `sample` | risco de contaminação controlado por rótulo | `local_path: data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_observer_2006_sample.csv` |
| `data/raw/RAW_DATA_MANIFEST.yml:152` | `SAMPLE` | risco de contaminação controlado por rótulo | `- raw_id: RAW_JPL_HORIZONS_MARS_VECTORS_2006_SAMPLE` |
| `data/raw/RAW_DATA_MANIFEST.yml:159` | `sample` | risco de contaminação controlado por rótulo | `local_path: data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv` |
| `data/raw/RAW_DATA_MANIFEST.yml:167` | `sample` | risco de contaminação controlado por rótulo | `safe_conclusion: "This manifest creates custody slots and now includes two local raw JPL Horizons samples: observer ephemeris and heliocentric state vectors. Sc` |
| `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_observer_2006_sample.meta.yml:5` | `SAMPLE` | risco de contaminação controlado por rótulo | `raw_id: RAW_JPL_HORIZONS_MARS_OBSERVER_2006_SAMPLE` |
| `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_observer_2006_sample.meta.yml:8` | `sample` | risco de contaminação controlado por rótulo | `raw_role: observer_ephemeris_sample` |
| `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_observer_2006_sample.meta.yml:18` | `sample` | risco de contaminação controlado por rótulo | `path: data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_observer_2006_sample.csv` |
| `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_observer_2006_sample.meta.yml:42` | `sample` | risco de contaminação controlado por rótulo | `raw_sample_is_not_full_validation: true` |
| `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_observer_2006_sample.meta.yml:53` | `sample` | risco de contaminação controlado por rótulo | `safe_conclusion: First raw Horizons sample is locally versioned and checksummed, but it is observer ephemeris data, not the final state-vector dataset required ` |
| `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml:4` | `SAMPLE` | risco de contaminação controlado por rótulo | `raw_id: RAW_JPL_HORIZONS_MARS_VECTORS_2006_SAMPLE` |
| `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml:7` | `sample` | risco de contaminação controlado por rótulo | `raw_role: heliocentric_cartesian_state_vector_sample` |
| `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml:15` | `sample` | risco de contaminação controlado por rótulo | `path: data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv` |
| `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml:20` | `sample` | risco de contaminação controlado por rótulo | `state_vector_sample_is_not_full_validation: true` |
| `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml:24` | `sample` | risco de contaminação controlado por rótulo | `safe_conclusion: Raw Horizons vector sample is locally present and checksummed against the canonical LF-normalized repository artifact, but claims remain blocke` |
| `data/real/bootstrap/canonical_route_checklist.yml:15` | `token_vazio` | TOKEN_VAZIO protegido | `- sha256_or_token_vazio_declared` |
| `data/real/bootstrap/canonical_route_checklist.yml:72` | `sample` | risco de contaminação controlado por rótulo | `- data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv` |
| `data/real/bootstrap/canonical_route_checklist.yml:73` | `sample` | risco de contaminação controlado por rótulo | `- data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml` |
| `data/real/bootstrap/dense_behavior_feature_orchestration.yml:13` | `token_vazio` | TOKEN_VAZIO protegido | `token_vazio_priority_ledger: data/results/bootstrap/token_vazio_priority_ledger.json` |
| `data/real/bootstrap/real_data_requirements_bootstrap.yml:12` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- docs/science/TOKEN_VAZIO_PRIORITY_LEDGER.md` |
| `data/real/bootstrap/real_data_requirements_bootstrap.yml:23` | `token_vazio` | TOKEN_VAZIO protegido | `no_superiority_claim_from_token_vazio: true` |
| `data/real/bootstrap/real_data_requirements_bootstrap.yml:218` | `token_vazio` | TOKEN_VAZIO protegido | `fail_closed_if_token_vazio: true` |
| `data/real/bootstrap/real_observational_seed_v0.yml:44` | `sample` | risco de contaminação controlado por rótulo | `- ingest_GWOSC_or_LVK_posterior_samples_when_available` |
| `data/real/bootstrap/real_observational_seed_v0.yml:120` | `sample` | risco de contaminação controlado por rótulo | `data_context: Gaia_DR3_proper_motions_and_HVS_Survey_sample` |
| `data/real/compact_objects/remnant_boundary_sources.yml:2` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `# Status: TOKEN_VAZIO protected source ledger` |
| `data/real/compact_objects/remnant_boundary_sources.yml:7` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:23` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- id: TOKEN_VAZIO_REMNANT_NS_001` |
| `data/real/compact_objects/remnant_boundary_sources.yml:25` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `dataset_name: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:26` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `provider: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:27` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `url_or_reference: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:28` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:29` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `data_type: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:31` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:32` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:45` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `eos_model: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:54` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:56` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- id: TOKEN_VAZIO_REMNANT_GW_001` |
| `data/real/compact_objects/remnant_boundary_sources.yml:58` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `dataset_name: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:59` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `provider: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:60` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `url_or_reference: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:61` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:62` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `data_type: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:64` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:65` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:88` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:90` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- id: TOKEN_VAZIO_REMNANT_BH_XRB_001` |
| `data/real/compact_objects/remnant_boundary_sources.yml:92` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `dataset_name: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:93` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `provider: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:94` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `url_or_reference: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:95` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:96` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `data_type: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:98` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:99` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:115` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:117` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- id: TOKEN_VAZIO_PAIR_INSTABILITY_001` |
| `data/real/compact_objects/remnant_boundary_sources.yml:119` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `dataset_name: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:120` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `provider: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:121` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `url_or_reference: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:122` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:123` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `data_type: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:125` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:126` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/compact_objects/remnant_boundary_sources.yml:141` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:2` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `# Status: TOKEN_VAZIO protected source ledger` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:7` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:23` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- id: TOKEN_VAZIO_WBH_001` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:25` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `dataset_name: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:26` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `provider: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:27` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `url_or_reference: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:28` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:29` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `data_type: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:31` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:32` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:52` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `metric_expected: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:53` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `baseline_model: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:60` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:62` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- id: TOKEN_VAZIO_DARK_LENS_001` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:64` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `dataset_name: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:65` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `provider: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:66` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `url_or_reference: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:67` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:68` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `data_type: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:70` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:71` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:80` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `metric_expected: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:81` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `baseline_model: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:86` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:88` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- id: TOKEN_VAZIO_RECOIL_001` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:90` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `dataset_name: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:91` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `provider: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:92` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `url_or_reference: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:93` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:94` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `data_type: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:96` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:97` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:106` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `metric_expected: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:107` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `baseline_model: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:111` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:2` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `# Status: TOKEN_VAZIO protected source ledger` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:7` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:24` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- id: TOKEN_VAZIO_HIGHZ_QSO_001` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:26` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `dataset_name: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:27` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `provider: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:28` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `url_or_reference: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:29` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:30` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `data_type: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:32` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:33` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:58` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:60` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- id: TOKEN_VAZIO_JWST_AGN_001` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:62` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `dataset_name: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:63` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `provider: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:64` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `url_or_reference: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:65` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:66` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `data_type: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:68` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:69` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:91` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:93` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- id: TOKEN_VAZIO_DIRECT_COLLAPSE_001` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:95` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `dataset_name: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:96` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `provider: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:97` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `url_or_reference: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:98` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:99` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `data_type: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:101` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:102` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/high_z_smbh/high_z_seed_sources.yml:122` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:2` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `# Status: TOKEN_VAZIO protected source ledger` |
| `data/real/kinematics/hypervelocity_sources.yml:7` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:25` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- id: TOKEN_VAZIO_HVS_001` |
| `data/real/kinematics/hypervelocity_sources.yml:27` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `dataset_name: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:28` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `provider: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:29` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `url_or_reference: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:30` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:31` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `data_type: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:33` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:34` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:51` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `origin_candidate: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:60` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:62` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- id: TOKEN_VAZIO_RUNAWAY_001` |
| `data/real/kinematics/hypervelocity_sources.yml:64` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `dataset_name: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:65` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `provider: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:66` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `url_or_reference: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:67` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:68` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `data_type: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:70` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:71` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:90` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:92` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- id: TOKEN_VAZIO_RECOIL_TRACE_001` |
| `data/real/kinematics/hypervelocity_sources.yml:94` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `dataset_name: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:95` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `provider: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:96` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `url_or_reference: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:97` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:98` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `data_type: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:100` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:101` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/kinematics/hypervelocity_sources.yml:121` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:2` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `# Status: TOKEN_VAZIO protected source ledger` |
| `data/real/lensing/dark_lens_sources.yml:7` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:24` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- id: TOKEN_VAZIO_MICROLENS_001` |
| `data/real/lensing/dark_lens_sources.yml:26` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `dataset_name: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:27` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `provider: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:28` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `url_or_reference: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:29` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:30` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `data_type: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:32` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:33` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:58` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:60` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- id: TOKEN_VAZIO_ASTRO_LENS_001` |
| `data/real/lensing/dark_lens_sources.yml:62` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `dataset_name: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:63` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `provider: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:64` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `url_or_reference: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:65` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:66` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `data_type: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:68` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:69` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:88` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:90` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- id: TOKEN_VAZIO_STRONG_LENS_001` |
| `data/real/lensing/dark_lens_sources.yml:92` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `dataset_name: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:93` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `provider: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:94` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `url_or_reference: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:95` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:96` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `data_type: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:98` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:99` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:119` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:121` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- id: TOKEN_VAZIO_WEAK_LENS_001` |
| `data/real/lensing/dark_lens_sources.yml:123` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `dataset_name: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:124` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `provider: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:125` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `url_or_reference: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:126` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:127` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `data_type: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:129` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:130` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/lensing/dark_lens_sources.yml:144` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/orbital_dynamics/angular_momentum_shape_sources.yml:2` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `# Status: TOKEN_VAZIO protected source ledger` |
| `data/real/orbital_dynamics/angular_momentum_shape_sources.yml:7` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/orbital_dynamics/angular_momentum_shape_sources.yml:70` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- record_id: TOKEN_VAZIO_EARTH_MOON_ORBIT_SHAPE_001` |
| `data/real/orbital_dynamics/angular_momentum_shape_sources.yml:85` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/orbital_dynamics/angular_momentum_shape_sources.yml:88` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- record_id: TOKEN_VAZIO_MARS_ORBIT_SHAPE_001` |
| `data/real/orbital_dynamics/angular_momentum_shape_sources.yml:102` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/orbital_dynamics/angular_momentum_shape_sources.yml:105` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- record_id: TOKEN_VAZIO_JUPITER_SYSTEM_001` |
| `data/real/orbital_dynamics/angular_momentum_shape_sources.yml:119` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/rll_real_sources_manifest_2026.yml:13` | `fake` | risco de contaminação controlado por rótulo | `- "Permitir que scripts futuros baixem, verifiquem hashes e normalizem cada dataset sem fake-fill."` |
| `data/real/rll_real_sources_manifest_2026.yml:81` | `sample` | risco de contaminação controlado por rótulo | `dynamic_dark_energy_context: "DESI BAO plus CMB favors w0-wa over LCDM at 3.1 sigma; with SNe the preference ranges from 2.8 to 4.2 sigma depending on sample, p` |
| `data/real/structure/residual_gravity_sources.yml:2` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `# Status: TOKEN_VAZIO protected source ledger` |
| `data/real/structure/residual_gravity_sources.yml:7` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:24` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- id: TOKEN_VAZIO_RES_GRAV_001` |
| `data/real/structure/residual_gravity_sources.yml:26` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `dataset_name: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:27` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `provider: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:28` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `url_or_reference: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:29` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:30` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `data_type: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:32` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:33` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:50` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `metric_expected: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:51` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `baseline_model: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:56` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:58` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- id: TOKEN_VAZIO_ORPHAN_HALO_001` |
| `data/real/structure/residual_gravity_sources.yml:60` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `dataset_name: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:61` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `provider: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:62` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `url_or_reference: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:63` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:64` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `data_type: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:66` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:67` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:76` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `metric_expected: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:77` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `baseline_model: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:81` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:83` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- id: TOKEN_VAZIO_HIST_IMPULSE_001` |
| `data/real/structure/residual_gravity_sources.yml:85` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `dataset_name: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:86` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `provider: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:87` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `url_or_reference: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:88` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `access_date_utc: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:89` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `data_type: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:91` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:92` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:103` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `metric_expected: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:104` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `baseline_model: TOKEN_VAZIO` |
| `data/real/structure/residual_gravity_sources.yml:109` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `data/real_sources/rll_pantheon_real_validation.iml.yml:69` | `sample` | risco de contaminação controlado por rótulo | `null_hypothesis: "LCDM explains the Pantheon+ observations at least as well as RLL under the declared likelihood, sample, covariance, and parameter count."` |
| `data/real_sources/rll_pantheon_real_validation.iml.yml:75` | `sample` | risco de contaminação controlado por rótulo | `- "same observational sample used for both models"` |
| `data/real_sources/rll_pantheon_real_validation.iml.yml:79` | `synthetic` | risco de contaminação controlado por rótulo | `- "no superiority claim from synthetic or partial data"` |
| `data/real_sources/rll_real_orchestrator_inventory.iml.yml:3` | `fake` | risco de contaminação controlado por rótulo | `purpose: "Unificar IML/ML, Doc Inventory, Real Data Complete, Structure-D, Pantheon, DESI e pipelines sem criar rota paralela ou fake-fill."` |
| `data/real_sources/rll_real_orchestrator_inventory.iml.yml:10` | `example` | placeholder/exemplo honesto | `example_input: "data/iml/daise_input.example.json"` |
| `data/real_sources/rll_real_orchestrator_inventory.iml.yml:110` | `fake` | risco de contaminação controlado por rótulo | `no_fake_fill: "Missing data remains TOKEN_VAZIO/lacuna instead of invented value."` |
| `data/rll_latentes/examples/invalid_missing_falsifier.yml:48` | `example` | placeholder/exemplo honesto | `url: "https://example.org/rll-latentes-fixture"` |
| `data/rll_latentes/examples/valid_minimal.yml:48` | `example` | placeholder/exemplo honesto | `url: "https://example.org/rll-latentes-fixture"` |
| `data/rll_latentes/observations.yml:115` | `synthetic` | risco de contaminação controlado por rótulo | `- "Require candidate residuals to survive documented DR2 validation and synthetic-dataset checks."` |
| `data/rll_latentes/observations.yml:234` | `demo` | risco de contaminação controlado por rótulo | `- "Residual neural signatures must survive motion, physiology, batch, task and demographic controls."` |
| `knowledge_ecosystem/source_search_queue.yml:6` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `teses, conceitos e fórmulas de REF_REQUIRED/TOKEN_VAZIO para SOURCE_LINKED,` |
| `knowledge_ecosystem/source_search_queue.yml:13` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- Se a fonte não for encontrada, manter TOKEN_VAZIO_REFERENCE.` |
| `knowledge_ecosystem/source_search_queue.yml:33` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `result: TOKEN_VAZIO_RESULT` |
| `knowledge_ecosystem/source_search_queue.yml:45` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `result: TOKEN_VAZIO_RESULT` |
| `knowledge_ecosystem/source_search_queue.yml:95` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `result: TOKEN_VAZIO_RESULT` |
| `rll_equation_registry.yml:58` | `placeholder` | placeholder/exemplo honesto | `claim_boundary: "placeholder metric; formula depends on code implementation"` |
| `rll_equation_registry.yml:92` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `claim_boundary: "TOKEN_VAZIO corresponds to H_max; CLAIM_ALLOWED to H=0; monotonic decrease as evidence accumulates"` |
| `tools/inventory_config.yml:4` | `synthetic` | risco de contaminação controlado por rótulo | `claim_boundary: "No synthetic claim without repository-measured evidence. TOKEN_VAZIO preserves unmeasured gaps."` |
