# Guia de Artefatos do Pipeline RLL/MCRP

## Execução manual
1. Abra **Actions** no GitHub.
2. Selecione **RLL Data Pipeline**.
3. Clique em **Run workflow** e escolha os inputs.

## dataset_group
- `geomagnetic`: M(t), m(t), T_M e caso AMAS/SAA local.
- `heliophysics`: Φ_ext, SW, T_M, Φ_eff.
- `cosmology`: E²(a), f(z), w(z), comparação RLL vs ΛCDM/w0waCDM.
- `all`: executa os três grupos.

## Modos
- `metadata_only`: só catálogo/manifesto e auditoria documental.
- `dry_run`: simula pipeline sem ingestão pesada.
- `fetch`: habilita busca controlada quando permitido.
- `compute`: reservado para cálculo; pode operar como stub sem dados reais processáveis.

## Artifact
- O workflow sempre gera artifact, inclusive em `metadata_only`.
- Download: Actions → execução → **Artifacts** → baixar pacote `rll-pipeline-...`.

## commit_artifacts
Use apenas para persistir resultados pequenos em `results/pipeline-runs/<run_id>/`:
- `*.md`, `*.json`, `*.txt`, `*.sha256`.

Dados brutos pesados não devem ser commitados por padrão para evitar crescimento indevido do Git e quebra de reprodutibilidade operacional.

## CHECKSUMS.sha256
- Lista hash SHA-256 de cada arquivo do artifact.
- Permite verificar integridade e detectar alterações entre execuções.

## Guardrails científicos
- Nenhuma claim deve subir para **Real validado** sem dados reais processados e métricas reproduzíveis.
- AMAS/SAA permanece marcado como caso observacional local.
