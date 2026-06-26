# RLL Parameter Origin Table — Rafael/RLL versus literatura externa

Esta tabela é a versão humana do registro `data/inputs/cosmology_joint/parameter_origin_registry.json`. O objetivo é impedir que parâmetros autorais do RLL, parâmetros de literatura externa, parâmetros ajustados e parâmetros nuisance sejam misturados em AIC/AICc/BIC.

| parâmetro | modelo(s) | origem | papel na comparação | status para `k` | referência/dependência | regra operacional |
|---|---|---|---|---|---|---|
| `H0` | LCDM, wCDM, CPL, RLL | literatura externa ou ajuste local | livre ou prior externo | contar se ajustado; declarar se fixo/prior | Planck2018, SH0ES ou fit local | Usar a mesma política em todos os modelos. |
| `Om` | LCDM, wCDM, CPL, RLL | literatura externa ou ajuste local | livre ou prior externo | contar se ajustado | Planck2018 ou fit local | Entra em `E(z)`, BAO, CMB, crescimento e S8. |
| `Ok` | LCDM, wCDM, CPL, RLL | hipótese FLRW/ajuste | fixo ou livre | contar se liberado | convenção de curvatura FLRW | Default plano; se liberar curvatura, liberar para todos os modelos comparados. |
| `Ob_h2` | LCDM, wCDM, CPL, RLL | literatura externa ou ajuste local | nuisance de `r_d` | contar se ajustado | calibração de horizonte de arrasto | Necessário quando `r_d` é derivado. |
| `rd` | LCDM, wCDM, CPL, RLL | derivado ou fixo de literatura | derivado/nuisance | declarar política; contar se ajustado diretamente | BAO drag horizon | Não misturar `r_d` fixo em um modelo e derivado em outro. |
| `w` | wCDM | baseline padrão de energia escura | livre | contar | fenomenologia constant-w | Baseline obrigatório antes de atribuir ganho ao RLL. |
| `w0` | CPL/w0waCDM | baseline padrão de energia escura dinâmica | livre | contar | parametrização CPL | Deve ser fitado como baseline independente. |
| `wa` | CPL/w0waCDM | baseline padrão de energia escura dinâmica | livre | contar | parametrização CPL | Deve ser fitado como baseline independente. |
| `Os0` | RLL | Rafael/RLL autoral efetivo | livre | contar | ansatz logístico RLL | Não rotular como parâmetro de literatura externa. |
| `zt` | RLL | Rafael/RLL autoral efetivo | livre | contar | transição logística RLL | Exigir limites/prior e teste de sensibilidade. |
| `wt` | RLL | Rafael/RLL autoral efetivo | livre | contar | transição logística RLL | Deve permanecer positivo e reportado. |
| `sigma8` | LCDM, wCDM, CPL, RLL | literatura externa ou ajuste local | amplitude de crescimento | contar se ajustado | RSD/lensing/Planck | Necessário para `fσ8` e S8; não é equivalente a S8. |
| `M_abs` | LCDM, wCDM, CPL, RLL | nuisance de supernovas | calibração SN | contar se ajustado | Pantheon+/SN Ia | Não é parâmetro físico RLL. |

## Regras de coerência científica

1. Todo parâmetro livre, nuisance ajustado ou prior efetivamente variado precisa aparecer em `k`.
2. Parâmetros Rafael/RLL (`Os0`, `zt`, `wt`) não devem ser apresentados como valores medidos pela literatura externa.
3. Parâmetros de literatura externa usados como fixos/prior devem ter fonte, versão e política declaradas.
4. `rd` deve ter a mesma política em todos os modelos: fixo para todos ou derivado para todos.
5. Uma claim RLL × ΛCDM só é academicamente justa quando wCDM e CPL/w0waCDM forem executados no mesmo vetor de dados e covariância.

## Failsafe / rollback

- Este arquivo e o JSON pareado são apenas metadados; não alteram `data/real/**`.
- Se uma validação falhar, reverta esta tabela/JSON sem tocar datasets brutos.
- TOKEN_VAZIO continua obrigatório para qualquer parâmetro sem origem, prior ou política de `k` documentada.
