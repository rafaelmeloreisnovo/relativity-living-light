# RLL Real Run Artifact Audit — 28287121163

Run analisado: `rll-real-run-28287121163.zip`  
Run UTC do artefato: `2026-06-27T10:56:00Z`  
Commit de origem do artefato: `7f73cd2f32499e6c4f6b7a764573659da02e47db`  
Status editorial declarado: `Parcial real em preparação`

## Síntese executiva

O artefato é útil como trilha de execução, inventário, diagnóstico e fronteira de claim. Ele **não** autoriza promoção científica de RLL como modelo vencedor. O resultado preserva a disciplina anti-alucinação: dados reais são diferenciados de materialização parcial, parsers pendentes e rotas bloqueadas.

## Integridade do pacote

- Arquivos no ZIP: `68`.
- Arquivos verificados por checksum: `67/68`.
- Único desvio: `CHECKSUMS.sha256` foi hasheado enquanto ainda estava vazio, gerando o digest de arquivo vazio (`e3b0...b855`) dentro do próprio manifesto.
- Correção aplicada no workflow: gerar arquivos mínimos antes do manifesto e excluir `CHECKSUMS.sha256` do próprio cálculo.

## Dados e status de fonte

| Grupo | Fonte | Estado no artefato | Uso científico imediato |
|---|---:|---|---|
| Geomagnetic | IGRF14 | fetched | parser real pendente |
| Geomagnetic | WMM2025 | fetched | parser real pendente |
| Heliophysics | OMNI/SPDF | fetched | parser/extração pendente |
| Cosmology | DESI DR2 | manual_materialization_required | não materializado em bulk |
| Cosmology | Pantheon+ | README fetched | não é likelihood Pantheon+ |
| Cosmology | Hz/BAO/CMB repo CSV/JSON | copied_from_repo / real_non_synthetic | usado em comparadores iniciais |

## Resultados cosmológicos do artefato

### Comparador rápido `model_comparison.csv`

| Modelo | chi² | AIC | BIC | Pontos |
|---|---:|---:|---:|---:|
| LCDM | 216.576529 | 220.576529 | 224.098929 | 43 |
| RLL | 238.492871 | 248.492871 | 257.298871 | 43 |

Diferenças: `Δχ²_RLL-LCDM = 21.916342`, `ΔAIC = 27.916342`, `ΔBIC = 33.199942`.

### Diagnóstico `h0_grid_expansion`

Melhor por modelo no grid pontual:

| Modelo | H0 | chi²_Hz | chi²_BAO | chi²_total | AIC | BIC |
|---|---:|---:|---:|---:|---:|---:|
| LCDM | 68.0 | 23.100943 | 15.386703 | 38.487646 | 44.487646 | 49.973570 |
| w0wa | 64.0 | 24.845103 | 53.913691 | 78.758794 | 88.758794 | 97.902001 |
| RLL | 67.0 | 36.765142 | 77.984582 | 114.749723 | 126.749723 | 137.721572 |

Gates:

- `gate_1_grid_lcdm_internal = true`
- `gate_1_grid_rll_internal = true`
- `gate_2_h0_degeneracy_lcdm_rll = false`
- `gate_3_delta_aic_rll_minus_lcdm_lt_4 = false`
- `gate_4_w0wa_adversary_present = true`

Status seguro: `claim_blocked_quality_gate_failed`.

## Principais resíduos BAO no comparador rápido

| Survey | z | Pull LCDM | Pull RLL |
|---|---:|---:|---:|
| DESI2024_LRG2 | 0.930 | -8.397869 | -8.690522 |
| DESI2024_QSO | 1.491 | -6.070832 | -6.379138 |
| DESI2024_ELG | 1.317 | -5.738118 | -6.021297 |
| DESI2024_BGS | 0.510 | -4.386964 | -4.444025 |
| BOSS_Lya | 2.330 | -4.328434 | -4.640141 |

Estes pulls indicam que a etapa rápida baseada em `DV_over_rs` legado não deve ser usada como conclusão final sem revisar definição observável, covariância e dataset DESI primário.

## Diagnóstico estrutural

1. `compute_rll_real_pipeline.py` e `run_h0_grid_expansion.py` não estão medindo exatamente a mesma coisa:
   - o comparador rápido usa constantes internas `H0=70.0`, `Ωm=0.30`, `ΩΛ=0.70`, `rd=147.09` e BAO legado DV/rs;
   - o grid usa `rll_vs_lcdm.py`, `Ωm=0.315`, `H0` varrido, DESI primary BAO e resumo de covariância.
2. O relatório de fórmulas encontrou `487` expressões, mas `FORMAL_ACADEMIC_REPORT.md` ainda só registra total; falta classificação por `COD/HIP/SIM`, unidade, observável e fonte.
3. O IML preserva custódia SHA256 e executa `42` passos, mas `cycle_42_verified=false`; logo é trilha simbólico-computacional, não endosso científico.
4. A migração `to_Add` validou como legado controlado, sem wrappers inválidos.
5. O scanner de placeholders/stubs retornou `0` achados, mas o artifact antigo não tinha arquivo `.status` para esse scan; o workflow foi ajustado para emitir status explícito.

## Próximas ações técnicas

1. Unificar o comparador rápido com `rll_vs_lcdm.evaluate()` ou marcar o CSV como `legacy_quickcheck`.
2. Rodar uma etapa dedicada DESI primary + covariância por observable (`DM/rd`, `DH/rd`, `DV/rd`) antes de qualquer leitura cosmológica.
3. Materializar Pantheon+ real além do README e ligar likelihood de supernovas.
4. Implementar parsers reais de IGRF14, WMM2025 e OMNI para sair de `fetched` e chegar em `computed` com tabela observável.
5. Ampliar `FORMAL_ACADEMIC_REPORT.md` para claim map: expressão, fonte, tipo, unidade, dado, teste, status.

## Conclusão segura

`F_ok`: pipeline executa, gera artefatos, preserva fronteira de claim e valida migração controlada.  
`F_gap`: checksums autocontidos foram corrigidos; comparadores ainda misturam modos; DESI/Pantheon/geomagnetismo precisam materialização/parsing real.  
`F_next`: próxima run deve confirmar checksum determinístico e produzir relatório de comparação unificado antes de qualquer promoção científica.

TOKEN_VAZIO protegido: sem dados/covariância/materialização completa, não há validação total.
