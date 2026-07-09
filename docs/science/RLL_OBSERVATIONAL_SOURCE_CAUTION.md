# RLL — Observational Source Caution

**Status date:** 2026-06-27  
**Scope:** cautela bibliográfica para cruzamentos observacionais recentes  
**Claim level:** `claim_allowed=false`

---

## 1. Frase curta

```text
[ATENÇÃO] O mapa de cruzamentos é útil como roteiro de pesquisa, mas objetos observacionais recentes precisam de normalização bibliográfica antes de subir para [E].
```

---

## 2. Por que este cuidado existe

Algumas entradas recentes sobre buracos negros andantes, contrails galácticos e objetos compactos deslocados aparecem em preprints, notícias científicas e versões posteriores com números levemente diferentes.

Portanto, antes de usar esses objetos como dado estabelecido no RLL, cada caso precisa de:

```text
[ ] fonte primária ou catálogo oficial
[ ] DOI/arXiv/ADS normalizado
[ ] access_date_utc
[ ] license_or_terms
[ ] valor numérico com unidade
[ ] incerteza, quando existir
[ ] local_path ou external-only boundary
[ ] sha256 quando houver arquivo local
[ ] claim_allowed=false até baseline e métrica
```

---

## 3. Regra de implantação

```text
Documento de cruzamento pode usar [H] para propor rota.
Manifesto observacional só deve usar [E] quando a fonte primária estiver normalizada.
Pipeline só deve gerar claim se houver raw-data custody + baseline + incerteza + artifact.
```

---

## 4. Aplicação aos cruzamentos atuais

| Tema | Uso permitido agora | Bloqueio |
|---|---|---|
| RBH-1 / runaway SMBH | rota observacional e hipótese de teste | não usar como prova RLL |
| MaNGA 12772-12704 | candidato para jato/off-nuclear BH | precisa fonte primária normalizada |
| NGC 3627 contrail | rota de massive compact object / flyby | números devem ser reconciliados por fonte |
| Liu et al. 2025 | referência candidata | confirmar DOI/arXiv/versão antes de manifesto |
| Faraday / VLBI / MeerKAT | plano de observação | falta dataset local |

---

## 5. Conclusão segura

```text
[OK] Os cruzamentos podem ficar como mapa de pesquisa.
[PARCIAL] A camada bibliográfica ainda precisa ser normalizada.
[BLOQUEADO] Nenhuma afirmação observacional recente deve virar [E] sem fonte primária e cadeia de custódia.
```

---

*F_ok: cautela bibliográfica registrada.*  
*F_gap: normalização DOI/arXiv/ADS por objeto ainda pendente.*  
*F_next: criar/atualizar `data/real/compact_objects/wandering_black_hole_sources.yml` com fonte primária e status por caso.*
