# Ponte AGN Feedback ↔ Cosmologia (para “ganhar” do ΛCDM)

## Hipótese operacional
Quasares/AGN aquecem o gás e reduzem a formação estelar em vizinhas (escala ~Mpc),
o que pode se refletir como **supressão efetiva** do crescimento observado (especialmente em medidas tardias e não-lineares).

## Implementação mínima (fenomenológica)
Definimos um termo de supressão dependente de redshift:

- Densidade efetiva de AGN/quasar:  ρ_AGN(z)
- Energia injetada:                E(z) ∝ ρ_AGN(z) · ⟨L⟩
- Supressão:                       S(z) = 1 - α · g(z)

onde g(z) é uma janela (ex.: pico em z~2) e α é a eficiência.

No pipeline:
- `code/feedback_agn.py` define `suppression_factor(z, alpha, z_peak, width)`
- `code/growth.py` aplica isso em σ8_eff(z) ou em um proxy de fσ8(z)

## O que medir para discriminar modelos
- fσ8(z) (RSD)
- weak lensing (S8)
- clustering em ambientes de quasar
- história de SFR (JWST + levantamentos)

## Critério de vitória
Mesmo se χ² for parecido, o modelo só “ganha” se:
- reduzir parâmetros (k menor), **ou**
- baixar χ² o suficiente para superar a penalidade em AIC/BIC.
