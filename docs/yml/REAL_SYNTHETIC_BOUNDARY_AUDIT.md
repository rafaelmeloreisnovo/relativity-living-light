# REAL / SYNTHETIC / MOCK BOUNDARY AUDIT

Gerado em: `2026-07-03T16:02:54Z`  
Commit auditado: `929807336098e7edb7cfa2194dc2986fb6458deb`

## Escopo e comando

FATO_VERIFICADO: varredura YAML/YML por parser e varredura textual de fronteira executadas.  
Comando equivalente amplo solicitado, executado com `rg` por diretriz do ambiente: `rg -n -i "mock|synthetic|sintetico|sintético|placeholder|example|TOKEN_VAZIO|fake|sample|demo" .`.  
Total amplo medido por `wc -l`: `5445`.

## Regra de promoção

RISCO: termos `mock`, `synthetic`, `example`, `placeholder` e `demo` existem no repositório.  
FATO_VERIFICADO: nenhum YAML auditado contém promoção textual direta `real_validated` associada na mesma linha a mock/synthetic/example/placeholder/demo.  
ACAO_RECOMENDADA: manter `real_validated` BLOQUEADO sem dados reais identificados, fonte externa, checksum, comando executado, commit, métrica, baseline, covariância/erro quando aplicável, artefato final e claim boundary.

## Ocorrências em YAML/YML

| arquivo:linha | termo | classificação | trecho |
|---|---|---|---|
| `.github/To_add/01_wandering_bh_sources_real.yml:41` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `.github/To_add/01_wandering_bh_sources_real.yml:72` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `.github/To_add/01_wandering_bh_sources_real.yml:116` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `.github/To_add/05_slingshot_zt_falsification.yml:100` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `reason: "Sem varredura de chi2(zt) materializada — TOKEN_VAZIO"` |
| `.github/To_add/06_hypervelocity_sources_real.yml:4` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `# Substitui: data/real/kinematics/hypervelocity_sources.yml (TOKEN_VAZIO)` |
| `.github/To_add/06_hypervelocity_sources_real.yml:45` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `.github/To_add/06_hypervelocity_sources_real.yml:83` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `.github/To_add/06_hypervelocity_sources_real.yml:115` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `.github/To_add/07_high_z_smbh_sources_real.yml:4` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `# Substitui: data/real/high_z_smbh/high_z_seed_sources.yml (TOKEN_VAZIO)` |
| `.github/To_add/07_high_z_smbh_sources_real.yml:48` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `.github/To_add/07_high_z_smbh_sources_real.yml:77` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `.github/To_add/07_high_z_smbh_sources_real.yml:93` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `Isso é HONESTO — TOKEN_VAZIO preservado.` |
| `.github/To_add/07_high_z_smbh_sources_real.yml:109` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `.github/To_add/07_high_z_smbh_sources_real.yml:123` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `honest_assessment: "TOKEN_VAZIO — RLL não prevê diferença mensurável em z~10"` |
| `.github/To_add/08_falsification_master_protocol.yml:13` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `TOKEN_VAZIO > fabricação.` |
| `.github/To_add/11_diagnosis_weff_gap.yml:93` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO_AGUARDA_REFORMULACAO_DA_EQUACAO` |
| `.github/To_add/11_diagnosis_weff_gap.yml:101` | `token_vazio` | TOKEN_VAZIO protegido | `token_vazio_preservado: true` |
| `.github/workflows/START_MANUAL_HERE.yml:245` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/START_MANUAL_HERE.yml:246` | `Synthetic` | risco de contaminação controlado por rótulo | `x-canonical-real-data-policy: Auxiliary real-data workflow; canonical policy is .github/workflows/real-data-complete-execution.yml. Synthetic/mock/fixture/demo/` |
| `.github/workflows/academic-parameter-governance.yml:77` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `python3 tools/apply_rll_outcome_protocol.py --no-write --status TOKEN_VAZIO` |
| `.github/workflows/academic-parameter-governance.yml:118` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/academic-parameter-governance.yml:119` | `Synthetic` | risco de contaminação controlado por rótulo | `x-canonical-real-data-policy: Auxiliary real-data workflow; canonical policy is .github/workflows/real-data-complete-execution.yml. Synthetic/mock/fixture/demo/` |
| `.github/workflows/canonical-route-artifacts.yml:66` | `sample` | risco de contaminação controlado por rótulo | `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv` |
| `.github/workflows/canonical-route-artifacts.yml:68` | `sample` | risco de contaminação controlado por rótulo | `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml` |
| `.github/workflows/canonical-route-artifacts.yml:94` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/canonical-route-artifacts.yml:134` | `sample` | risco de contaminação controlado por rótulo | `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv` |
| `.github/workflows/canonical-route-artifacts.yml:136` | `sample` | risco de contaminação controlado por rótulo | `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml` |
| `.github/workflows/canonical-route-artifacts.yml:175` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/canonical-route-artifacts.yml:176` | `Synthetic` | risco de contaminação controlado por rótulo | `x-canonical-real-data-policy: Auxiliary real-data workflow; canonical policy is .github/workflows/real-data-complete-execution.yml. Synthetic/mock/fixture/demo/` |
| `.github/workflows/claim-boundary-quality-gates.yml:93` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/claim-boundary-quality-gates.yml:94` | `Synthetic` | risco de contaminação controlado por rótulo | `x-canonical-real-data-policy: Auxiliary real-data workflow; canonical policy is .github/workflows/real-data-complete-execution.yml. Synthetic/mock/fixture/demo/` |
| `.github/workflows/dense-feature-matrix.yml:9` | `token_vazio` | TOKEN_VAZIO protegido | `- data/results/bootstrap/token_vazio_priority_ledger.json` |
| `.github/workflows/dense-feature-matrix.yml:18` | `token_vazio` | TOKEN_VAZIO protegido | `- data/results/bootstrap/token_vazio_priority_ledger.json` |
| `.github/workflows/dense-feature-matrix.yml:83` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/dense-feature-matrix.yml:84` | `Synthetic` | risco de contaminação controlado por rótulo | `x-canonical-real-data-policy: Auxiliary real-data workflow; canonical policy is .github/workflows/real-data-complete-execution.yml. Synthetic/mock/fixture/demo/` |
| `.github/workflows/desi-dr2-bao-validation.yml:78` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/desi-dr2-bao-validation.yml:79` | `Synthetic` | risco de contaminação controlado por rótulo | `x-canonical-real-data-policy: Auxiliary real-data workflow; canonical policy is .github/workflows/real-data-complete-execution.yml. Synthetic/mock/fixture/demo/` |
| `.github/workflows/dha-fisher-ci.yml:37` | `mock` | risco de contaminação controlado por rótulo | `- name: Build mock catalog for ln(1+z) extraction` |
| `.github/workflows/dha-fisher-ci.yml:47` | `mock` | risco de contaminação controlado por rótulo | `pd.DataFrame({'z': z, 'pk_obs': pk_obs, 'pk_baseline': pk_baseline}).to_csv('results/dha/mock_catalog.csv', index=False)` |
| `.github/workflows/dha-fisher-ci.yml:51` | `mock` | risco de contaminação controlado por rótulo | `run: python scripts/run_ln1pz_extractor.py --input results/dha/mock_catalog.csv --output results/dha/ln1pz_fit.csv --summary results/dha/ln1pz_fit_summary.json` |
| `.github/workflows/iml_artifact.yml:40` | `example` | placeholder/exemplo honesto | `cp data/iml/daise_input.example.json data/iml/daise_input.json` |
| `.github/workflows/import-data.yml:12` | `sample` | risco de contaminação controlado por rótulo | `default: raw-data-audit-sample` |
| `.github/workflows/import-data.yml:36` | `synthetic` | risco de contaminação controlado por rótulo | `- name: Run synthetic detector as report-only guard` |
| `.github/workflows/import-data.yml:37` | `synthetic` | risco de contaminação controlado por rótulo | `run: "if [ -f scripts/detect_synthetic.py ]; then\n  python scripts/detect_synthetic.py --report-only\nelse\n  echo \"scripts/detect_synthetic.py not found; ski` |
| `.github/workflows/import-data.yml:65` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/import-data.yml:66` | `Synthetic` | risco de contaminação controlado por rótulo | `x-canonical-real-data-policy: Auxiliary real-data workflow; canonical policy is .github/workflows/real-data-complete-execution.yml. Synthetic/mock/fixture/demo/` |
| `.github/workflows/orbital-shape-angular-momentum-validation.yml:83` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/orbital-shape-angular-momentum-validation.yml:84` | `Synthetic` | risco de contaminação controlado por rótulo | `x-canonical-real-data-policy: Auxiliary real-data workflow; canonical policy is .github/workflows/real-data-complete-execution.yml. Synthetic/mock/fixture/demo/` |
| `.github/workflows/orbital-state-vector-v2.yml:57` | `sample` | risco de contaminação controlado por rótulo | `path: 'data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv` |
| `.github/workflows/orbital-state-vector-v2.yml:59` | `sample` | risco de contaminação controlado por rótulo | `data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml` |
| `.github/workflows/orbital-state-vector-v2.yml:85` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/orbital-state-vector-v2.yml:86` | `Synthetic` | risco de contaminação controlado por rótulo | `x-canonical-real-data-policy: Auxiliary real-data workflow; canonical policy is .github/workflows/real-data-complete-execution.yml. Synthetic/mock/fixture/demo/` |
| `.github/workflows/real-data-bootstrap-validation.yml:105` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/real-data-bootstrap-validation.yml:106` | `Synthetic` | risco de contaminação controlado por rótulo | `x-canonical-real-data-policy: Auxiliary real-data workflow; canonical policy is .github/workflows/real-data-complete-execution.yml. Synthetic/mock/fixture/demo/` |
| `.github/workflows/real-data-complete-execution.yml:99` | `mock` | risco de contaminação controlado por rótulo | `- Never promote mock/synthetic/example/placeholder files as real data.` |
| `.github/workflows/real-data-complete-execution.yml:130` | `mock` | risco de contaminação controlado por rótulo | `for term in ['dado real', 'checksum', 'mock', 'synthetic', 'Pantheon+SH0ES', 'DESI DR2 BAO']:` |
| `.github/workflows/real-data-complete-execution.yml:215` | `synthetic` | risco de contaminação controlado por rótulo | `'no synthetic promotion',` |
| `.github/workflows/real-data-contract-ci.yml:89` | `synthetic` | risco de contaminação controlado por rótulo | `run: "set -euo pipefail\ntest -s artifacts/real-data-contract/MANIFEST.json\ntest -s artifacts/real-data-contract/COMPUTE_REPORT.md\ntest -s artifacts/real-data` |
| `.github/workflows/real-data-contract-ci.yml:90` | `synthetic` | risco de contaminação controlado por rótulo | `\    raise SystemExit('all inputs must be marked used_real_non_synthetic')\nvalidation_status = manifest.get('validation_status') or {}\nif validation_status.ge` |
| `.github/workflows/real-data-contract-ci.yml:121` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/real-data-contract-ci.yml:122` | `Synthetic` | risco de contaminação controlado por rótulo | `x-canonical-real-data-policy: Auxiliary real-data workflow; canonical policy is .github/workflows/real-data-complete-execution.yml. Synthetic/mock/fixture/demo/` |
| `.github/workflows/real-seed-ingestion-plan.yml:89` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/real-seed-ingestion-plan.yml:90` | `Synthetic` | risco de contaminação controlado por rótulo | `x-canonical-real-data-policy: Auxiliary real-data workflow; canonical policy is .github/workflows/real-data-complete-execution.yml. Synthetic/mock/fixture/demo/` |
| `.github/workflows/real-seed-validation-v0.yml:103` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/real-seed-validation-v0.yml:104` | `Synthetic` | risco de contaminação controlado por rótulo | `x-canonical-real-data-policy: Auxiliary real-data workflow; canonical policy is .github/workflows/real-data-complete-execution.yml. Synthetic/mock/fixture/demo/` |
| `.github/workflows/repo-real-inventory.yml:88` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/repo-real-inventory.yml:89` | `Synthetic` | risco de contaminação controlado por rótulo | `x-canonical-real-data-policy: Auxiliary real-data workflow; canonical policy is .github/workflows/real-data-complete-execution.yml. Synthetic/mock/fixture/demo/` |
| `.github/workflows/rll-book-data-pipeline.yml:122` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/rll-book-data-pipeline.yml:168` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/rll-book-data-pipeline.yml:169` | `Synthetic` | risco de contaminação controlado por rótulo | `x-canonical-real-data-policy: Auxiliary real-data workflow; canonical policy is .github/workflows/real-data-complete-execution.yml. Synthetic/mock/fixture/demo/` |
| `.github/workflows/rll-real-data-orchestrator.yml:144` | `placeholder` | placeholder/exemplo honesto | `run: "set -euo pipefail\nmkdir -p artifacts/rll-real-run/diagnostics artifacts/rll-real-run/tables artifacts/rll-real-run/reports\n\npython3 tools/scan_missing_` |
| `.github/workflows/rll-real-data-orchestrator.yml:198` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/rll-real-data-orchestrator.yml:199` | `Synthetic` | risco de contaminação controlado por rótulo | `x-canonical-real-data-policy: Auxiliary real-data workflow; canonical policy is .github/workflows/real-data-complete-execution.yml. Synthetic/mock/fixture/demo/` |
| `.github/workflows/six-sigma-real-data-controls.yml:66` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/six-sigma-real-data-controls.yml:67` | `Synthetic` | risco de contaminação controlado por rótulo | `x-canonical-real-data-policy: Auxiliary real-data workflow; canonical policy is .github/workflows/real-data-complete-execution.yml. Synthetic/mock/fixture/demo/` |
| `.github/workflows/validacao_real.yml:83` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/validacao_real.yml:129` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/validacao_real.yml:130` | `Synthetic` | risco de contaminação controlado por rótulo | `x-canonical-real-data-policy: Auxiliary real-data workflow; canonical policy is .github/workflows/real-data-complete-execution.yml. Synthetic/mock/fixture/demo/` |
| `.github/workflows/validate-real-dataset-variance-registry.yml:63` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/validate-real-dataset-variance-registry.yml:64` | `Synthetic` | risco de contaminação controlado por rótulo | `x-canonical-real-data-policy: Auxiliary real-data workflow; canonical policy is .github/workflows/real-data-complete-execution.yml. Synthetic/mock/fixture/demo/` |
| `.github/workflows/validate-sequence-metrics.yml:63` | `synthetic` | risco de contaminação controlado por rótulo | `CLAIM_BOUNDARY: Auxiliary real-data workflow only; no RLL/cosmology/superiority claim and no synthetic, mock, fixture, demo, example, or placeholder promotion b` |
| `.github/workflows/validate-sequence-metrics.yml:64` | `Synthetic` | risco de contaminação controlado por rótulo | `x-canonical-real-data-policy: Auxiliary real-data workflow; canonical policy is .github/workflows/real-data-complete-execution.yml. Synthetic/mock/fixture/demo/` |
| `RLL_JSON_EVOLUTION_WATCHER.yml:103` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `domain: TOKEN_VAZIO` |
| `RLL_JSON_EVOLUTION_WATCHER.yml:106` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `title: TOKEN_VAZIO` |
| `RLL_JSON_EVOLUTION_WATCHER.yml:107` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `url: TOKEN_VAZIO` |
| `RLL_JSON_EVOLUTION_WATCHER.yml:108` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `epistemic_initial: TOKEN_VAZIO` |
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
| `data/real/compact_objects/wandering_black_hole_sources.yml:17` | `token_vazio` | TOKEN_VAZIO protegido | `token_vazio_is_valid_for_missing_raw_data: true` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:42` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- "4. Compute SHA256 and replace TOKEN_VAZIO only with measured checksum."` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:63` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:64` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:102` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:103` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:145` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `local_path: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:146` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `checksum_sha256: TOKEN_VAZIO` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:180` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `step4: "Compute SHA256 before replacing TOKEN_VAZIO."` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:184` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `step3: "Compute SHA256 before replacing TOKEN_VAZIO."` |
| `data/real/compact_objects/wandering_black_hole_sources.yml:188` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `step3: "Compute SHA256 before replacing TOKEN_VAZIO."` |
| `data/real/cosmology/fsigma8_perturbation_test.yml:36` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `note: "Current repository file has 16 rows (17 lines including header); uses diagonal sigma only; full covariance remains TOKEN_VAZIO."` |
| `data/real/cosmology/real_cosmology_inputs.yml:11` | `synthetic` | risco de contaminação controlado por rótulo | `no_synthetic_promotion: true` |
| `data/real/cosmology/real_cosmology_inputs.yml:24` | `REAL_VALIDATED` | placeholder/exemplo honesto | `state: REAL_VALIDATED_LIMITED` |
| `data/real/cosmology/real_cosmology_inputs.yml:47` | `REAL_VALIDATED` | placeholder/exemplo honesto | `state: REAL_VALIDATED_LIMITED` |
| `data/real/cosmology/real_cosmology_inputs.yml:72` | `REAL_VALIDATED` | placeholder/exemplo honesto | `state: REAL_VALIDATED_LIMITED` |
| `data/real/cosmology/real_cosmology_inputs.yml:95` | `REAL_VALIDATED` | placeholder/exemplo honesto | `state: REAL_VALIDATED_LIMITED` |
| `data/real/cosmology/real_cosmology_inputs.yml:123` | `synthetic` | risco de contaminação controlado por rótulo | `synthetic_fixture_detected: block_promotion` |
| `data/real/cosmology/weff_cpl_mapping.yml:15` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `exact_table_values_status: TOKEN_VAZIO` |
| `data/real/cosmology/weff_cpl_mapping.yml:78` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `gate_1_source_boundary: "Official DESI exact best-fit values remain TOKEN_VAZIO until table provenance is ingested."` |
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
| `data/real_sources/rll_joint_cosmology_real_inputs.iml.yml:30` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- TOKEN_VAZIO` |
| `data/real_sources/rll_joint_cosmology_real_inputs.iml.yml:33` | `REAL_VALIDATED` | placeholder/exemplo honesto | `- REAL_VALIDATED_BLOCKED` |
| `data/real_sources/rll_joint_cosmology_real_inputs.iml.yml:152` | `real_validated` | placeholder/exemplo honesto | `- "Do not promote source_registered or metadata_ready to real_validated."` |
| `data/real_sources/rll_joint_cosmology_real_inputs.iml.yml:153` | `sample` | risco de contaminação controlado por rótulo | `- "Do not merge unrelated public catalog samples into cosmology likelihood inputs."` |
| `data/real_sources/rll_latent_theses_registry.yml:32` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `default_state: TOKEN_VAZIO` |
| `data/real_sources/rll_latent_theses_registry.yml:35` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `A latent thesis can move from TOKEN_VAZIO to TEST_READY only after data,` |
| `data/real_sources/rll_latent_theses_registry.yml:58` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `state: TOKEN_VAZIO_ROBUST_FIT` |
| `data/real_sources/rll_latent_theses_registry.yml:95` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `state: TOKEN_VAZIO_GROWTH_BACKEND` |
| `data/real_sources/rll_latent_theses_registry.yml:128` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `state: TOKEN_VAZIO_DATASET` |
| `data/real_sources/rll_latent_theses_registry.yml:157` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `state: TOKEN_VAZIO_RAW_POSTERIORS` |
| `data/real_sources/rll_latent_theses_registry.yml:161` | `sample` | risco de contaminação controlado por rótulo | `compact-remnant boundary test using LVK/GWOSC posterior samples.` |
| `data/real_sources/rll_latent_theses_registry.yml:165` | `sample` | risco de contaminação controlado por rótulo | `current_limit: "No raw LVK/GWOSC posterior samples are registered with checksum."` |
| `data/real_sources/rll_latent_theses_registry.yml:167` | `sample` | risco de contaminação controlado por rótulo | `- LVK_GWOSC_posterior_samples` |
| `data/real_sources/rll_latent_theses_registry.yml:177` | `sample` | risco de contaminação controlado por rótulo | `If posterior samples do not show a reproducible boundary signal beyond` |
| `data/real_sources/rll_latent_theses_registry.yml:185` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `state: TOKEN_VAZIO_BASELINES` |
| `data/real_sources/rll_latent_theses_registry.yml:217` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `state: TOKEN_VAZIO_ASTROMETRY` |
| `data/real_sources/rll_pantheon_real_validation.iml.yml:69` | `sample` | risco de contaminação controlado por rótulo | `null_hypothesis: "LCDM explains the Pantheon+ observations at least as well as RLL under the declared likelihood, sample, covariance, and parameter count."` |
| `data/real_sources/rll_pantheon_real_validation.iml.yml:75` | `sample` | risco de contaminação controlado por rótulo | `- "same observational sample used for both models"` |
| `data/real_sources/rll_pantheon_real_validation.iml.yml:79` | `synthetic` | risco de contaminação controlado por rótulo | `- "no superiority claim from synthetic or partial data"` |
| `data/real_sources/rll_real_orchestrator_inventory.iml.yml:3` | `fake` | risco de contaminação controlado por rótulo | `purpose: "Unificar IML/ML, Doc Inventory, Real Data Complete, Structure-D, Pantheon, DESI e pipelines sem criar rota paralela ou fake-fill."` |
| `data/real_sources/rll_real_orchestrator_inventory.iml.yml:10` | `example` | placeholder/exemplo honesto | `example_input: "data/iml/daise_input.example.json"` |
| `data/real_sources/rll_real_orchestrator_inventory.iml.yml:110` | `fake` | risco de contaminação controlado por rótulo | `no_fake_fill: "Missing data remains TOKEN_VAZIO/lacuna instead of invented value."` |
| `data/real_sources/rll_required_data_gap_registry.yml:13` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `default_state: TOKEN_VAZIO` |
| `data/real_sources/rll_required_data_gap_registry.yml:27` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `state: TOKEN_VAZIO_ROBUST_FIT` |
| `data/real_sources/rll_required_data_gap_registry.yml:40` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `state: TOKEN_VAZIO_SUPERNOVA` |
| `data/real_sources/rll_required_data_gap_registry.yml:53` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `state: TOKEN_VAZIO_GROWTH_BACKEND` |
| `data/real_sources/rll_required_data_gap_registry.yml:66` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `state: TOKEN_VAZIO_CMB_NATIVE_BACKEND` |
| `data/real_sources/rll_required_data_gap_registry.yml:83` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `C_l likelihood, so the gap state remains TOKEN_VAZIO* and no RLL` |
| `data/real_sources/rll_required_data_gap_registry.yml:89` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `state: TOKEN_VAZIO_DATASET` |
| `data/real_sources/rll_required_data_gap_registry.yml:102` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `state: TOKEN_VAZIO_RAW_POSTERIORS` |
| `data/real_sources/rll_required_data_gap_registry.yml:104` | `sample` | risco de contaminação controlado por rótulo | `needed_data_or_artifact: public_compact_remnant_posterior_samples` |
| `data/real_sources/rll_required_data_gap_registry.yml:110` | `sample` | risco de contaminação controlado por rótulo | `next_action: ingest_public_posterior_sample_manifest` |
| `data/real_sources/rll_required_data_gap_registry.yml:115` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `state: TOKEN_VAZIO_BASELINES` |
| `data/real_sources/rll_required_data_gap_registry.yml:128` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `state: TOKEN_VAZIO_ASTROMETRY` |
| `data/rll_latentes/examples/invalid_missing_falsifier.yml:48` | `example` | placeholder/exemplo honesto | `url: "https://example.org/rll-latentes-fixture"` |
| `data/rll_latentes/examples/valid_minimal.yml:48` | `example` | placeholder/exemplo honesto | `url: "https://example.org/rll-latentes-fixture"` |
| `data/rll_latentes/observations.yml:115` | `synthetic` | risco de contaminação controlado por rótulo | `- "Require candidate residuals to survive documented DR2 validation and synthetic-dataset checks."` |
| `data/rll_latentes/observations.yml:234` | `demo` | risco de contaminação controlado por rótulo | `- "Residual neural signatures must survive motion, physiology, batch, task and demographic controls."` |
| `docs/pipelines/validation_paths/CAMINHOS_VALIDACAO_NOVOS.yml:22` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- TOKEN_VAZIO` |
| `docs/pipelines/validation_paths/CAMINHOS_VALIDACAO_NOVOS.yml:25` | `REAL_VALIDATED` | placeholder/exemplo honesto | `- REAL_VALIDATED_BLOCKED` |
| `docs/pipelines/validation_paths/CAMINHOS_VALIDACAO_NOVOS.yml:79` | `REAL_VALIDATED` | placeholder/exemplo honesto | `state: REAL_VALIDATED_BLOCKED` |
| `docs/pipelines/validation_paths/CAMINHOS_VALIDACAO_NOVOS.yml:96` | `REAL_VALIDATED` | placeholder/exemplo honesto | `state: REAL_VALIDATED_BLOCKED` |
| `docs/pipelines/validation_paths/CAMINHOS_VALIDACAO_NOVOS.yml:109` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `state: TOKEN_VAZIO` |
| `docs/pipelines/validation_paths/CAMINHOS_VALIDACAO_NOVOS.yml:123` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `state: TOKEN_VAZIO` |
| `docs/pipelines/validation_paths/CAMINHOS_VALIDACAO_NOVOS.yml:142` | `REAL_VALIDATED` | placeholder/exemplo honesto | `state: REAL_VALIDATED_BLOCKED` |
| `docs/pipelines/validation_paths/CAMINHOS_VALIDACAO_NOVOS.yml:155` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `state: TOKEN_VAZIO` |
| `docs/pipelines/validation_paths/CAMINHOS_VALIDACAO_NOVOS.yml:175` | `REAL_VALIDATED` | placeholder/exemplo honesto | `state: REAL_VALIDATED_BLOCKED` |
| `docs/pipelines/validation_paths/CAMINHOS_VALIDACAO_NOVOS.yml:188` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `state: TOKEN_VAZIO` |
| `docs/pipelines/validation_paths/CAMINHOS_VALIDACAO_NOVOS.yml:202` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `state: TOKEN_VAZIO` |
| `docs/pipelines/validation_paths/CAMINHOS_VALIDACAO_NOVOS.yml:220` | `REAL_VALIDATED` | placeholder/exemplo honesto | `state: REAL_VALIDATED_BLOCKED` |
| `docs/professionalization/PROFESSIONAL_DOCUMENTS_REGISTRY.yml:21` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- TOKEN_VAZIO` |
| `docs/professionalization/PROFESSIONAL_DOCUMENTS_REGISTRY.yml:135` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- hide TOKEN_VAZIO blockers for presentation quality` |
| `docs/yml/FRONTIER_SCIENCE_CROSSMAP_2026.yml:187` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `docs/yml/FRONTIER_SCIENCE_CROSSMAP_2026.yml:190` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `docs/yml/FRONTIER_SCIENCE_CROSSMAP_2026.yml:193` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `docs/yml/PROOF_OBLIGATION_REGISTRY.yml:17` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- TOKEN_VAZIO_PROOF_PATH` |
| `docs/yml/PROOF_OBLIGATION_REGISTRY.yml:55` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- TOKEN_VAZIO_RAFAELIA_SIMULATION_TESTS` |
| `docs/yml/PROOF_OBLIGATION_REGISTRY.yml:56` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `formalization_target: TOKEN_VAZIO_FORMAL_SYSTEM` |
| `docs/yml/PROOF_OBLIGATION_REGISTRY.yml:66` | `synthetic` | risco de contaminação controlado por rótulo | `comparison, parameter bounds and synthetic-only artifact recording.` |
| `docs/yml/PROOF_OBLIGATION_REGISTRY.yml:83` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `formalization_target: TOKEN_VAZIO_FORMAL_SYSTEM` |
| `docs/yml/PROOF_OBLIGATION_REGISTRY.yml:108` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `derivation_path: TOKEN_VAZIO_PROOF_PATH` |
| `docs/yml/RLL_ARTIFACT_GAP_LEDGER_2026_06_27.yml:2` | `placeholder` | placeholder/exemplo honesto | `# Purpose: map the CI artifacts, previous-answer references, missing pieces, placeholders and safe next actions.` |
| `docs/yml/RLL_ARTIFACT_GAP_LEDGER_2026_06_27.yml:27` | `synthetic` | risco de contaminação controlado por rótulo | `no_synthetic_substitution: true` |
| `docs/yml/RLL_ARTIFACT_GAP_LEDGER_2026_06_27.yml:29` | `placeholder` | placeholder/exemplo honesto | `placeholder_resolution_requires:` |
| `docs/yml/RLL_ARTIFACT_GAP_LEDGER_2026_06_27.yml:40` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- TOKEN_VAZIO` |
| `docs/yml/RLL_ARTIFACT_GAP_LEDGER_2026_06_27.yml:201` | `placeholder` | placeholder/exemplo honesto | `- id: P10_missing_placeholder_scan` |
| `docs/yml/RLL_ARTIFACT_GAP_LEDGER_2026_06_27.yml:202` | `Placeholder` | placeholder/exemplo honesto | `statement: "Placeholder/stub/ausência precisam de scanner e ledger."` |
| `docs/yml/RLL_ARTIFACT_GAP_LEDGER_2026_06_27.yml:204` | `placeholder` | placeholder/exemplo honesto | `- tools/scan_missing_placeholders.py` |
| `docs/yml/RLL_ARTIFACT_GAP_LEDGER_2026_06_27.yml:206` | `placeholder` | placeholder/exemplo honesto | `- data/results/missing_placeholder_stub_scan.json` |
| `docs/yml/RLL_ARTIFACT_GAP_LEDGER_2026_06_27.yml:207` | `placeholder` | placeholder/exemplo honesto | `- data/results/missing_placeholder_stub_scan.csv` |
| `docs/yml/RLL_ARTIFACT_GAP_LEDGER_2026_06_27.yml:208` | `PLACEHOLDER` | placeholder/exemplo honesto | `- docs/MISSING_PLACEHOLDER_STUB_SCAN.md` |
| `docs/yml/RLL_ARTIFACT_GAP_LEDGER_2026_06_27.yml:212` | `placeholder` | placeholder/exemplo honesto | `missing_placeholder_stub_policy:` |
| `docs/yml/RLL_ARTIFACT_GAP_LEDGER_2026_06_27.yml:214` | `token_vazio` | TOKEN_VAZIO protegido | `token_vazio:` |
| `docs/yml/RLL_ARTIFACT_GAP_LEDGER_2026_06_27.yml:217` | `placeholder` | placeholder/exemplo honesto | `placeholder:` |
| `docs/yml/RLL_ARTIFACT_GAP_LEDGER_2026_06_27.yml:218` | `Mock` | risco de contaminação controlado por rótulo | `meaning: "Mock/example/dummy content that must not be promoted."` |
| `docs/yml/RLL_ARTIFACT_GAP_LEDGER_2026_06_27.yml:219` | `example` | placeholder/exemplo honesto | `action: "Replace with real fixture or label as example-only."` |
| `docs/yml/RLL_ARTIFACT_GAP_LEDGER_2026_06_27.yml:222` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `action: "Implement executable function or mark explicit TOKEN_VAZIO."` |
| `docs/yml/RLL_ARTIFACT_GAP_LEDGER_2026_06_27.yml:235` | `placeholder` | placeholder/exemplo honesto | `- command: "python3 tools/scan_missing_placeholders.py"` |
| `docs/yml/RLL_ARTIFACT_GAP_LEDGER_2026_06_27.yml:236` | `placeholder` | placeholder/exemplo honesto | `expected: "missing/stub/placeholder ledger generated"` |
| `docs/yml/TO_ADD_LOOSE_FILES_PLACEMENT_REGISTRY.yml:125` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `next_action: reconcile with current RLL limitations and TOKEN_VAZIO markers` |
| `docs/yml/TO_ADD_MIGRATION_LEDGER.yml:27` | `example` | placeholder/exemplo honesto | `- python -m data.pipelines.structure_d.make_example_data` |
| `docs/yml/TO_ADD_MIGRATION_LEDGER.yml:86` | `example` | placeholder/exemplo honesto | `- source: to_Add/RAFAELIA_COSMO_STRUCTURE_D/code/make_example_data.py` |
| `docs/yml/TO_ADD_MIGRATION_LEDGER.yml:87` | `example` | placeholder/exemplo honesto | `canonical: data/pipelines/structure_d/make_example_data.py` |
| `docs/yml/TO_ADD_NEURO_ECHO_PHOTON_CHEMISTRY.yml:120` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `status: TOKEN_VAZIO` |
| `docs/yml/YML_MASTER_LEDGER.yml:18` | `token_vazio` | TOKEN_VAZIO protegido | `token_vazio_is_valid_boundary: true` |
| `docs/yml/YML_MASTER_LEDGER.yml:24` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- TOKEN_VAZIO` |
| `docs/yml/YML_MASTER_LEDGER.yml:83` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `next_safe_action: "Replace TOKEN_VAZIO only after measured file/hash exists."` |
| `docs/yml/YML_MASTER_LEDGER.yml:119` | `placeholder` | placeholder/exemplo honesto | `role: "Maps CI artifacts, previous-answer references, missing files, placeholders, stubs and safe next actions."` |
| `docs/yml/YML_MASTER_LEDGER.yml:123` | `placeholder` | placeholder/exemplo honesto | `scanner: tools/scan_missing_placeholders.py` |
| `docs/yml/YML_MASTER_LEDGER.yml:124` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `next_safe_action: "Run scanner and convert findings into artifacts or explicit TOKEN_VAZIO."` |
| `docs/yml/YML_MASTER_LEDGER.yml:127` | `placeholder` | placeholder/exemplo honesto | `- path: tools/scan_missing_placeholders.py` |
| `docs/yml/YML_MASTER_LEDGER.yml:131` | `placeholder` | placeholder/exemplo honesto | `human_name: "Scanner de placeholder/stub/ausência"` |
| `docs/yml/YML_MASTER_LEDGER.yml:132` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `role: "Scans tracked text files for TOKEN_VAZIO, placeholder, stub, TODO, missing, skipped, abortado, esquecido and claim blocks."` |
| `docs/yml/YML_MASTER_LEDGER.yml:134` | `placeholder` | placeholder/exemplo honesto | `- data/results/missing_placeholder_stub_scan.json` |
| `docs/yml/YML_MASTER_LEDGER.yml:135` | `placeholder` | placeholder/exemplo honesto | `- data/results/missing_placeholder_stub_scan.csv` |
| `docs/yml/YML_MASTER_LEDGER.yml:136` | `PLACEHOLDER` | placeholder/exemplo honesto | `- docs/MISSING_PLACEHOLDER_STUB_SCAN.md` |
| `docs/yml/YML_MASTER_LEDGER.yml:225` | `token_vazio` | TOKEN_VAZIO protegido | `token_vazio: "[TOKEN_VAZIO] Known gap; do not infer."` |
| `docs/yml/YML_MASTER_LEDGER.yml:228` | `placeholder` | placeholder/exemplo honesto | `safe_conclusion: "The repository now has a master YAML navigation layer, artifact gap ledger, placeholder scanner, to_Add migration validator and frontier-scien` |
| `knowledge_ecosystem/source_search_queue.yml:6` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `teses, conceitos e fórmulas de REF_REQUIRED/TOKEN_VAZIO para SOURCE_LINKED,` |
| `knowledge_ecosystem/source_search_queue.yml:13` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- Se a fonte não for encontrada, manter TOKEN_VAZIO_REFERENCE.` |
| `knowledge_ecosystem/source_search_queue.yml:33` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `result: TOKEN_VAZIO_RESULT` |
| `knowledge_ecosystem/source_search_queue.yml:45` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `result: TOKEN_VAZIO_RESULT` |
| `knowledge_ecosystem/source_search_queue.yml:95` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `result: TOKEN_VAZIO_RESULT` |
| `protocols/05_slingshot_zt_falsification.yml:94` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `reason: "Sem varredura de chi2(zt) materializada — TOKEN_VAZIO"` |
| `results/relational_validation/RELATIONAL_VALIDATION_LEDGER.yml:47` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- claim_id: TOKEN_VAZIO_INITIAL_RELATIONAL_PACKAGE` |
| `results/relational_validation/RELATIONAL_VALIDATION_LEDGER.yml:48` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `relation_graph_id: TOKEN_VAZIO_RELATION_GRAPH` |
| `results/relational_validation/RELATIONAL_VALIDATION_LEDGER.yml:54` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `baseline_or_adversary: TOKEN_VAZIO_BASELINE` |
| `results/relational_validation/RELATIONAL_VALIDATION_LEDGER.yml:55` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `uncertainty_or_covariance_status: TOKEN_VAZIO_UNCERTAINTY` |
| `results/relational_validation/RELATIONAL_VALIDATION_LEDGER.yml:56` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `contradiction_check: TOKEN_VAZIO_CONTRADICTION_CHECK` |
| `results/relational_validation/RELATIONAL_VALIDATION_LEDGER.yml:57` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `reproducibility_command: TOKEN_VAZIO_COMMAND` |
| `results/relational_validation/RELATIONAL_VALIDATION_LEDGER.yml:88` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- TOKEN_VAZIO_METRIC_UNTIL_TESTED_AXIS_EXISTS` |
| `results/relational_validation/RELATIONAL_VALIDATION_LEDGER.yml:91` | `synthetic` | risco de contaminação controlado por rótulo | `baseline for formula axes; synthetic null and stability baselines for` |
| `results/relational_validation/RELATIONAL_VALIDATION_LEDGER.yml:93` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `uncertainty_or_covariance_status: TOKEN_VAZIO_UNCERTAINTY_FOR_NUMERICAL_AXES` |
| `results/relational_validation/RELATIONAL_VALIDATION_LEDGER.yml:94` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `contradiction_check: TOKEN_VAZIO_CONTRADICTION_CHECK` |
| `results/relational_validation/packages/ACADEMIC_CORR_001/package.yml:69` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `- TOKEN_VAZIO_METRIC_UNTIL_VALIDATOR_EXISTS` |
| `results/relational_validation/packages/ACADEMIC_CORR_001/package.yml:72` | `synthetic` | risco de contaminação controlado por rótulo | `derivation-required baseline. For graph/chaos axes: synthetic null model and` |
| `results/relational_validation/packages/ACADEMIC_CORR_001/package.yml:74` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `uncertainty_or_covariance_status: TOKEN_VAZIO_UNCERTAINTY_FOR_NUMERICAL_AXES` |
| `results/relational_validation/packages/ACADEMIC_CORR_001/package.yml:75` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `contradiction_check: TOKEN_VAZIO_CONTRADICTION_CHECK` |
| `results/relational_validation/packages/ACADEMIC_CORR_001/package.yml:76` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `reproducibility_command: TOKEN_VAZIO_COMMAND` |
| `rll_equation_registry.yml:58` | `placeholder` | placeholder/exemplo honesto | `claim_boundary: "placeholder metric; formula depends on code implementation"` |
| `rll_equation_registry.yml:92` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `claim_boundary: "TOKEN_VAZIO corresponds to H_max; CLAIM_ALLOWED to H=0; monotonic decrease as evidence accumulates"` |
| `tests/fixtures/rll_latentes/invalid_missing_falsifier.yml:48` | `example` | placeholder/exemplo honesto | `url: "https://example.org/rll-latentes-fixture"` |
| `tests/fixtures/rll_latentes/valid_minimal.yml:48` | `example` | placeholder/exemplo honesto | `url: "https://example.org/rll-latentes-fixture"` |
| `to_Add/data_evolution_watch.yml:181` | `token_vazio` | TOKEN_VAZIO protegido | `token_vazio    = [s for s, e in latest.items() if e["epistemic_after"] == "TOKEN_VAZIO"]` |
| `to_Add/data_evolution_watch.yml:189` | `TOKEN_VAZIO` | TOKEN_VAZIO protegido | `f.write(f"/ ⚠️ TOKEN_VAZIO       / {', '.join(token_vazio) or '—'} /\n")` |
| `tools/inventory_config.yml:4` | `synthetic` | risco de contaminação controlado por rótulo | `claim_boundary: "No synthetic claim without repository-measured evidence. TOKEN_VAZIO preserves unmeasured gaps."` |
