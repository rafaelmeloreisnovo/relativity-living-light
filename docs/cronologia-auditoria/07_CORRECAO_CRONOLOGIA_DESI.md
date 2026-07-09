# RLL — Errata: Correção da Cronologia DESI

**Gerado**: 2026-07-05  
**Tipo**: Errata formal — correção factual de documentos anteriores  
**Documentos afetados**: `02_CRONOLOGIA_DETALHADA.md`, `03_AUDITORIA_TECNICA_PRIMEIRA_ORDEM.md`  
**Descoberta por**: Auditoria de segunda ordem (Fase 2) — comando `git log -S "DESI" | tac`

---

## Resumo da Correção

Os documentos merged em PR #499 afirmavam que DESI estava **ausente** na tag v1.0.0 e entrou **apenas em julho de 2026**. Isso está factualmente incorreto.

A auditoria de segunda ordem, usando ordem cronológica correta (`| tac`), revelou que DESI aparece desde setembro de 2025.

---

## Afirmações Incorretas (Documentos 02 e 03)

### Em `02_CRONOLOGIA_DETALHADA.md`:

> **"DESI: ❌ Ausente"** (seção "Epoch 1: Núcleo Matemático Cristalizado")

> **"Primeira Menção: DESI — Commit: 207013741... Data: 2026-07-03T16:05:22 UTC"**

> **"Estágio 0: Ausência (Setembro 2025) — Status na tag v1.0.0: ❌ Não mencionado"**

### Em `03_AUDITORIA_TECNICA_PRIMEIRA_ORDEM.md`:

> **"Primeiro commit com DESI: 2026-07-03 16:05:22 (hash: 20701374...)"**

---

## Correção Factual

### Erro Metodológico

O `git log -S` lista commits do mais recente ao mais antigo (padrão git). Ler o output sem `tac` (ou `--reverse`) produz o commit MAIS RECENTE que contém "DESI" — não o mais antigo.

Os documentos 02/03 tomaram o **topo** da lista como "primeiro", quando na verdade é o **último** cronologicamente.

### Cronologia DESI Correta

| Data | Commit | Hash | Evidência |
|------|--------|------|-----------|
| **2025-09-05** | Update README.md | `535720cb` | `"surveys como Pantheon+, DESI → observável"` |
| **2025-09-05** | Update README.md | `fbbe9697` | Itens adicionados ao README |
| **2025-09-19** | Update README.md (v1.0.0) | `0b3f4cb` | `"comparável a BOSS/DESI"`, `"f σ₈(z) para BOSS/DESI"` |
| **2026-05-31** | Add DESI DR2 BAO materialization | `b833caba` | `desi_dr2_bao_primary_points.csv` adicionado |
| **2026-07-02/03** | Auditoria + watcher | múltiplos | DESI integrado em falsificadores e watcher |

### Verificação

```bash
# Primeiro commit com "DESI" (cronologicamente)
git log --all --format="%H %ci %s" -S "DESI" | tac | head -1
# Resultado: 535720cb 2025-09-05 14:57:59 -0300 Update README.md

# Conteúdo: DESI em v1.0.0
git show v1.0.0:README.md | grep -i "DESI"
# Resultado:
# "comparável a BOSS/DESI"
# "f σ₈(z), comparável a BOSS/DESI"
# "Pantheon+, DESI → observável"
# "calibrar em BOSS/DESI"
```

---

## Interpretação Corrigida

### O Que Mudou na Interpretação

**Antes (incorreto)**:
- DESI ausente em v1.0.0
- DESI entrou como dataset em jul/2026
- Modelo desenvolvido independentemente de dados DESI

**Depois (correto)**:
- DESI mencionado como validator futuro desde set/2025 (antes de v1.0.0)
- DESI como dataset físico adicionado em mai/2026 (commit b833caba)
- Modelo validado contra DESI em jul/2026

### Impacto na Narrativa do Modelo

A correção é **favorável** à credibilidade do RLL:

1. ✅ **Antecipação de validator**: O autor nomeou DESI como referência futura em set/2025
2. ✅ **Dados posteriores**: Os dados DESI DR2 foram publicados em 2024; integração em mai/2026 é natural
3. ✅ **Sem retrofitting**: O modelo matemático não mudou quando DESI chegou
4. ✅ **Padrão científico honesto**: Previsão → Dados → Comparação

---

## Tabela de Evolução Semântica (Corrigida)

| Período | Função de DESI | Evidência |
|---------|---------------|-----------|
| set/2025 (pré-v1.0.0) | Referência de validação futura | "DESI → observável" no README |
| set/2025 (v1.0.0) | Mencionado 4× no README | Comparativo com BOSS/DESI |
| mai/2026 | Dataset físico adicionado | `desi_dr2_bao_primary_points.csv` |
| jul/2026 | Protocolo de falsificação | watcher + falsificadores C01-C10 |

---

## TOKEN_VAZIO Preservado

Mesmo com a correção, mantemos honestidade:

❌ NÃO afirmamos que mencionar DESI em 2025 prova que o modelo foi construído para DESI  
❌ NÃO afirmamos que DESI valida o RLL (χ² = 93.81 vs ΛCDM = 28.97 para parâmetros nominais)  
✅ AFIRMAMOS que DESI foi antecipado como validator antes de v1.0.0

---

## Ação Recomendada

Os documentos 02 e 03 permanecem no repositório como registro da Fase 1. Esta errata (documento 07) é o registro formal da correção.

Futura revisão dos documentos 02/03 deve atualizar:
- Seção "Epoch 1" em 02: remover "DESI: ❌ Ausente"
- Tabela final em 02: corrigir coluna DESI da linha "set/2025"
- Seção "Interpretação" em 03 (gap 1): corrigir "Primeiro commit com DESI"

---

*Este documento demonstra que o protocolo TOKEN_VAZIO funciona: a lacuna marcada foi investigada e o fato foi corrigido.*

*"Correção documentada é melhor que silêncio sobre erro." — RAFAELIA*
