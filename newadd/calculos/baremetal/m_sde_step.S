/* m_sde_step.S
 * Passo Euler-Maruyama mínimo para m(t) em x86_64 SysV.
 * Entradas:
 *   xmm0 = m
 *   xmm1 = dt
 *   xmm2 = drift          ; -dV/dm + f_core + f_mantle
 *   xmm3 = eta
 *   xmm4 = xi             ; ruído já amostrado externamente
 * Saída:
 *   xmm0 = m_next
 */

    .text
    .globl m_sde_step
m_sde_step:
    /* drift_term = dt * drift */
    mulsd   %xmm1, %xmm2

    /* noise_term = eta * xi */
    mulsd   %xmm4, %xmm3

    /* noise_term = dt * noise_term */
    mulsd   %xmm1, %xmm3

    /* m_next = m + drift_term + noise_term */
    addsd   %xmm2, %xmm0
    addsd   %xmm3, %xmm0
    ret
