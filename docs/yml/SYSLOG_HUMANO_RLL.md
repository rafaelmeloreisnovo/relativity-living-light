# SYSLOG Humano — RLL YAML/CI

Status: operacional  
Data: 2026-06-27  
Claim: `claim_allowed=false`

---

## Frase-mãe

```text
Escolha o objetivo; o sistema encontra o menor caminho seguro, executa, registra o artifact e traduz o resultado.
```

---

## Estados

```text
[OK] Pode seguir.
[PARCIAL] Existe estrutura, mas falta uma peça real.
[BLOQUEADO] Não pode promover claim.
[TOKEN_VAZIO] Lacuna conhecida; não inventar.
[PROXIMO] Menor ação segura agora.
```

---

## Logs padrão

### Inventário

```text
[OK] Inventário regenerado no runner.
[OK] Inventário conferido depois da regeneração.
[PROXIMO] Continuar para fetch/compute.
```

### Dados reais

```text
[PARCIAL] Manifesto existe.
[BLOQUEADO] Falta raw file ou checksum.
[PROXIMO] Materializar fonte primária e medir SHA256.
```

### Pantheon+

```text
[OK] Arquivos Pantheon+ presentes.
[OK] Alias de coluna de erro aplicado quando necessário.
[PROXIMO] Rodar comparação RLL × ΛCDM.
```

### H0 grid

```text
[PARCIAL] H0 anterior bateu na borda.
[PROXIMO] Rodar grid corrigido em [64,74].
[BLOQUEADO] Não tratar H0 de borda como resultado físico.
```

### w0/wa mapper

```text
[OK] RLL convertido para w0_eff/wa_eff.
[PROXIMO] Comparar contra CPL/w0waCDM.
[BLOQUEADO] Não afirmar superioridade sem métrica real e baseline.
```

---

## Regra de uso

Todo workflow deve produzir uma linha humana para cada etapa crítica:

```text
[STATUS] O que aconteceu.
[POR_QUE] Causa simples.
[PROXIMO] Menor ação segura.
```

---

## Conclusão

```text
[OK] SYSLOG humano reduz ruído.
[PARCIAL] Ele não substitui teste nem artifact.
[BLOQUEADO] Ele não libera claim científico.
```
