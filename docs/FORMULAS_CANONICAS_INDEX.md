# Índice Canônico de Fórmulas

> Referência oficial e padronizada de fórmulas usadas no projeto **Relativity Living Light**.

## Tabela canônica

| ID | Expressão (texto/LaTeX) | Variáveis | Unidade | Domínio de validade | Arquivo-fonte canônico |
|---|---|---|---|---|---|
| FCL-001 | Densidade de superposição fotônica: `\(\rho_{\text{sup}}(a)=\rho_0\left[f_{\text{ext}}a^{-n_{\text{ext}}}+(1-f_{\text{ext}})a^{-n_{\text{col}}}\right]\)` | `\(\rho_{\text{sup}}\)` (densidade efetiva), `\(a\)` (fator de escala), `\(\rho_0\)` (normalização), `\(f_{\text{ext}}\)` (fração estendida), `\(n_{\text{ext}}, n_{\text{col}}\)` (índices de escala) | Densidade de energia (ex.: kg·m⁻³ ou GeV·cm⁻³, conforme convenção adotada) | Modelo fenomenológico do setor escuro unificado; ansatz com `\(n_{\text{ext}}\approx 0\)` e `\(n_{\text{col}}\approx 3\)` | [`docs/Relativity_Living_Light.md`](Relativity_Living_Light.md) |
| FCL-002 | Friedmann modificado (setor de superposição): `\[H(z)^2 = H_0^2\left[\Omega_m(1+z)^3 + \Omega_r(1+z)^4 + \Omega_\Lambda + \Omega_{\text{sup}}a^{-n}\right]\]` | `\(H(z),H_0\)` (taxa de expansão), `\(\Omega_m,\Omega_r,\Omega_\Lambda,\Omega_{\text{sup}}\)` (densidades adimensionais), `\(z\)` (redshift), `\(a\)` (fator de escala) | `\(H\)` em s⁻¹ ou km·s⁻¹·Mpc⁻¹; `\(\Omega_i\)` adimensional | Cosmologia homogênea/isotrópica (FRW), parametrização fenomenológica do termo extra | [`docs/Relativity_Living_Light.md`](Relativity_Living_Light.md) |
| FCL-003 | Friedmann com feedback efetivo: `\[H^2(z)=H_0^2\Big[\Omega_m(1+z)^3+\Omega_r(1+z)^4+\Omega_\Lambda+\Omega_f(z)\Big]\]` | `\(H(z),H_0\)`, `\(\Omega_m,\Omega_r,\Omega_\Lambda\)`, `\(\Omega_f(z)\)` (termo efetivo) | `\(H\)` em s⁻¹ ou km·s⁻¹·Mpc⁻¹; `\(\Omega\)` adimensional | Extensão fenomenológica de ΛCDM para capturar processos energéticos efetivos | [`docs/modules/structure_d_equations.md`](modules/structure_d_equations.md) |
| FCL-004 | Taxa de crescimento linear: `\[f(z) \equiv \frac{d\ln D}{d\ln a} \approx \Omega_m(z)^\gamma\]` | `\(f(z)\)` (growth rate), `\(D(a)\)` (fator de crescimento), `\(a\)`, `\(\Omega_m(z)\)`, `\(\gamma\)` (índice de crescimento) | Adimensional | Regime linear; aproximação prática para inferir `\(f\sigma_8(z)\)` | [`docs/modules/structure_d_equations.md`](modules/structure_d_equations.md) |
| FCL-005 | Qui-quadrado: `\[\chi^2 = \sum_i \left(\frac{x_i^{obs}-x_i^{mod}}{\sigma_i}\right)^2\]` | `\(x_i^{obs},x_i^{mod}\)`, `\(\sigma_i\)` | Adimensional | Ajuste estatístico com erros gaussianos independentes (aprox.) | [`docs/modules/structure_d_equations.md`](modules/structure_d_equations.md) |
| FCL-006 | Critérios de informação: `\[AIC=\chi^2+2k\]` e `\[BIC=\chi^2+k\ln N\]` | `\(\chi^2\)`, `\(k\)` (nº de parâmetros), `\(N\)` (nº de dados) | Adimensional | Comparação relativa de modelos sob hipóteses usuais de máxima verossimilhança | [`docs/modules/structure_d_equations.md`](modules/structure_d_equations.md) |

## Referência histórica (não-canônica)

- O arquivo [`RAFAELIA_COSMO_STRUCTURE_D/core/equations.md`](../RAFAELIA_COSMO_STRUCTURE_D/core/equations.md) preserva as mesmas formas-base de expansão, crescimento e estatística por rastreabilidade histórica.
- Para uso oficial e manutenção corrente, considerar **canônico** o conteúdo em `docs/modules/structure_d_equations.md` e neste índice.
