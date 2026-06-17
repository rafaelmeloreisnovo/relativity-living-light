# REAL / SYNTHETIC / MOCK BOUNDARY AUDIT

Gerado em: `2026-06-13T06:12:53Z`  
Commit auditado: `c8eb1047ada81ee2a1f6eb4c917ae707fdee8e4f`

## Escopo e comando

FATO_VERIFICADO: varredura YAML/YML por parser e varredura textual de fronteira executadas.  
Comando equivalente amplo solicitado, executado com `rg` por diretriz do ambiente: `rg -n -i "mock|synthetic|sintetico|sintético|placeholder|example|TOKEN_VAZIO|fake|sample|demo" .`.  
Total amplo medido por `wc -l`: `1730`.

## Regra de promoção

RISCO: termos `mock`, `synthetic`, `example`, `placeholder` e `demo` existem no repositório.  
FATO_VERIFICADO: nenhum YAML auditado contém promoção textual direta `real_validated` associada na mesma linha a mock/synthetic/example/placeholder/demo.  
ACAO_RECOMENDADA: manter `real_validated` BLOQUEADO sem dados reais identificados, fonte externa, checksum, comando executado, commit, métrica, baseline, covariância/erro quando aplicável, artefato final e claim boundary.

## Ocorrências em YAML/YML

| arquivo:linha | termo | classificação | trecho |
|---|---|---|---|
| `.github/workflows/START_MANUAL_HERE.yml:37` | `sintético` | risco de contaminação controlado por rótulo | `description: Fonte dos dados reais não sintéticos para cálculo` |
| `.github/workflows/dha-fisher-ci.yml:37` | `mock` | risco de contaminação controlado por rótulo | `- name: Build mock catalog for ln(1+z) extraction` |
| `.github/workflows/dha-fisher-ci.yml:46` | `mock` | risco de contaminação controlado por rótulo | `pd.DataFrame({'z': z, 'pk_obs': pk_obs, 'pk_baseline': pk_baseline}).to_csv('results/dha/mock_catalog.csv', index=False)` |
| `.github/workflows/dha-fisher-ci.yml:50` | `mock` | risco de contaminação controlado por rótulo | `run: python scripts/run_ln1pz_extractor.py --input results/dha/mock_catalog.csv --output results/dha/ln1pz_fit.csv --summary results/dha/ln1pz_fit_summary.json` |
| `.github/workflows/iml_artifact.yml:40` | `example` | placeholder/exemplo honesto | `cp data/iml/daise_input.example.json data/iml/daise_input.json` |
| `.github/workflows/real-data-complete-execution.yml:102` | `mock` | risco de contaminação controlado por rótulo | `- Never promote mock/synthetic/example/placeholder files as real data.` |
| `.github/workflows/real-data-complete-execution.yml:133` | `mock` | risco de contaminação controlado por rótulo | `for term in ['dado real', 'checksum', 'mock', 'synthetic', 'Pantheon+SH0ES', 'DESI DR2 BAO']:` |
| `.github/workflows/real-data-complete-execution.yml:217` | `synthetic` | risco de contaminação controlado por rótulo | `'no synthetic promotion',` |
| `.github/workflows/repo-real-inventory.yml:89` | `sample` | risco de contaminação controlado por rótulo | `def flags(p: str, sample: str) -> list[str]:` |
| `.github/workflows/repo-real-inventory.yml:90` | `sample` | risco de contaminação controlado por rótulo | `s = sample.lower()` |
| `.github/workflows/repo-real-inventory.yml:92` | `synthetic` | risco de contaminação controlado por rótulo | `if 'synthetic' in s: out.append('mentions_synthetic')` |
| `.github/workflows/repo-real-inventory.yml:93` | `mock` | risco de contaminação controlado por rótulo | `if 'mock' in s or 'placeholder' in s: out.append('mentions_mock_or_placeholder')` |
| `.github/workflows/repo-real-inventory.yml:94` | `token_vazio` | TOKEN_VAZIO protegido | `if 'token_vazio' in s: out.append('token_vazio_declared')` |
| `.github/workflows/repo-real-inventory.yml:106` | `sample` | risco de contaminação controlado por rótulo | `sample = path.read_text('utf-8', errors='replace')[:12000] if text else ''` |
| `.github/workflows/repo-real-inventory.yml:115` | `sample` | risco de contaminação controlado por rótulo | `'risk_flags': flags(p, sample),` |
| `.github/workflows/repo-real-inventory.yml:133` | `synthetic` | risco de contaminação controlado por rótulo | `payload={'generated_at':now,'git_commit':commit,'summary':summary,'counts_by_ext':dict(extc),'counts_by_kind':dict(kindc),'flags':dict(flagc),'files':rows,'erro` |
| `data/observational_sources.yml:31` | `real_validated` | placeholder/exemplo honesto | `evidence_level: real_validated` |
| `data/observational_sources.yml:52` | `real_validated` | placeholder/exemplo honesto | `evidence_level: real_validated` |
| `data/real/rll_real_sources_manifest_2026.yml:13` | `fake` | risco de contaminação controlado por rótulo | `- "Permitir que scripts futuros baixem, verifiquem hashes e normalizem cada dataset sem fake-fill."` |
| `data/real/rll_real_sources_manifest_2026.yml:81` | `sample` | risco de contaminação controlado por rótulo | `dynamic_dark_energy_context: "DESI BAO plus CMB favors w0-wa over LCDM at 3.1 sigma; with SNe the preference ranges from 2.8 to 4.2 sigma depending on sample, p` |
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
| `rll_equation_registry.yml:58` | `placeholder` | placeholder/exemplo honesto | `claim_boundary: "placeholder metric; formula depends on code implementation"` |
| `tools/inventory_config.yml:4` | `synthetic` | risco de contaminação controlado por rótulo | `claim_boundary: "No synthetic claim without repository-measured evidence. TOKEN_VAZIO preserves unmeasured gaps."` |
