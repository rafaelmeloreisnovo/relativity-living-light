# RLL — Observational Data Implementation Review

**Status date:** 2026-06-27  
**Scope:** implantação documental e revisão estrutural de dados reais/observacionais  
**Claim level:** `claim_allowed=false`

---

## 1. Frase CEO / SYSLOG humano

```text
[PARCIAL] A base de dados reais existe em estrutura e alguns arquivos com hash já estão presentes; claims científicos fortes continuam bloqueados até fechar raw data + checksum + baseline + incerteza.
```

---

## 2. Implantação realizada

```text
[OK] Documento-mestre de cruzamentos implantado.
[OK] Revisão operacional de dados observacionais criada.
[OK] Nenhum workflow novo foi criado.
[OK] Nenhuma claim foi promovida.
[OK] claim_allowed=false preservado como política de segurança.
```

Arquivo implantado:

```text
docs/science/RLL_CRUZAMENTOS_COMPLETOS.md
```

Função:

```text
Mapa de cruzamentos entre RLL, CPL/w0waCDM, DESI/BAO, fσ8, crescimento, buracos negros andantes, MVICS e roadmap executável.
```

---

## 3. Condição estrutural dos dados observacionais

| Camada | Arquivo / rota | Estado | Leitura operacional |
|---|---|---|---|
| Manifesto bruto | `data/raw/RAW_DATA_MANIFEST.yml` | PARCIAL | Já define política de custódia, campos obrigatórios e registros pendentes/presentes. |
| Dados locais com hash | JPL Horizons Mars samples | OK parcial | Existem amostras locais com `sha256`, `bytes` e `raw_data_local=true`. |
| Cosmologia BAO | `scripts/compute_desi_dr2_bao_zml.py` | OK estrutural | Calcula comparação DESI DR2 BAO e gera JSON/CSV/YML. |
| Joint likelihood | `scripts/run_structure_d_joint_likelihood.py` | OK estrutural | Wrapper seguro para rodar likelihood sem sobrescrever artefato canônico. |
| Crescimento/fσ8 | `src/rll/rll_perturbation_kernel.py` | PARCIAL | Kernel interno existe; backend CLASS/CAMB ainda é lacuna para claim forte. |
| Relatório real | `scripts/build_real_validation_report.py` | OK estrutural | Renderiza tabela de chi²/AIC/BIC quando o pipeline real já gerou JSON. |
| Buracos negros andantes | `wandering_black_hole_sources.yml` | BLOQUEADO | Documento aponta necessidade, mas a fonte local com checksum ainda não está consolidada. |

---

## 4. Verificação de aplicação no trabalho

### 4.1 O que está bem aplicado

```text
[OK] Separação epistemológica [E]/[C]/[H]/[VAZIO] está correta.
[OK] Documento não afirma vitória do RLL.
[OK] CPL/w0waCDM é tratado como adversário/baseline forte.
[OK] H₀=60 é marcado como artefato de grid, não resultado físico.
[OK] fσ8 é bloqueado enquanto CLASS/CAMB não estiver disponível.
[OK] dados observacionais reais são tratados como cadeia de custódia, não como retórica.
```

### 4.2 O que ainda precisa de implantação real

```text
[BLOQUEADO] Expandir grid H₀ e gravar resultado auditável.
[BLOQUEADO] Criar mapper w0_eff/wa_eff do RLL contra CPL.
[BLOQUEADO] Preencher fonte real de buracos negros andantes com source_url, access_date_utc, license_or_terms, local_path e sha256.
[BLOQUEADO] Rodar crescimento com backend externo confiável ou declarar formalmente que é aproximação interna.
[BLOQUEADO] Criar artifact de resultado negativo quando RLL não melhorar o baseline.
```

---

## 5. Fluxo mínimo necessário para novato

```text
1. Escolha: quero testar RLL com dados reais.
2. O sistema confere se os dados têm fonte e hash.
3. O sistema roda o menor cálculo necessário.
4. O sistema gera artifact.
5. O sistema diz: OK, BLOQUEADO, TOKEN_VAZIO ou PRÓXIMO.
```

Saída desejada:

```text
[OK] cálculo executado e artifact gerado.
[BLOQUEADO] falta dado local com checksum.
[TOKEN_VAZIO] lacuna conhecida; não inventar.
[PRÓXIMO] executar grid H₀ ampliado ou mapear w0_eff/wa_eff.
```

---

## 6. Critérios para transformar hipótese em dado aplicado

Um cruzamento só pode subir de `[H]` para `[C]` quando existir:

```text
[ ] script ou notebook versionado
[ ] entrada observacional com fonte
[ ] local_path ou external-only boundary explícito
[ ] sha256 se houver arquivo local
[ ] baseline/adversário
[ ] métrica de comparação
[ ] incerteza ou limite declarado
[ ] artifact salvo em data/results/ ou results/
[ ] claim_allowed explicitamente definido
```

Um cruzamento só pode subir para `[E]` quando houver:

```text
[ ] reprodução em commit limpo
[ ] baseline vencido com métrica pré-definida
[ ] falsificador preservado
[ ] resultado negativo registrado quando aplicável
[ ] revisão humana ou externa possível sem interpretar metáfora como prova
```

---

## 7. Próximo patch mínimo recomendado

```text
P1 — Custódia observacional:
  criar ou completar data/real/compact_objects/wandering_black_hole_sources.yml
  preencher cada caso com source_url, access_date_utc, license_or_terms, local_path, sha256, status, claim_allowed=false

P2 — Cosmologia:
  criar script de grid H₀ ampliado [65,73] e output JSON/CSV
  manter H₀=60 marcado como boundary artifact

P3 — CPL bridge:
  criar mapper w0_eff/wa_eff para RLL
  comparar contra CPL/w0waCDM sem claim de superioridade

P4 — Growth:
  rodar kernel interno como aproximação ou integrar CLASS/CAMB
  marcar backend_status em cada artifact
```

---

## 8. Conclusão segura

```text
[OK] A implantação documental está coerente com a política de dados reais.
[OK] O trabalho está estruturado para observação e refutação.
[PARCIAL] Dados reais locais ainda existem de forma parcial, com JPL Horizons como melhor exemplo já hash-ready.
[BLOQUEADO] Claims fortes continuam bloqueadas até completar raw-data custody, baseline, incerteza e artifact reproduzível.
```

---

*F_ok: documento-mestre implantado, política de claim preservada, cadeia observacional revisada.*  
*F_gap: fontes compact-object/BH e growth backend ainda não fecham claim.*  
*F_next: completar manifesto observacional e gerar artifacts mínimos para H₀ grid + w0_eff/wa_eff.*
