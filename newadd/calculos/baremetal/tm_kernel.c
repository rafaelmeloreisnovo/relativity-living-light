/* tm_kernel.c
 * Núcleo determinístico para T_M sem chamadas de libc.
 * Compilação sugerida (objeto freestanding):
 *   cc -std=c11 -ffreestanding -fno-builtin -c tm_kernel.c
 */

typedef unsigned long long u64;
typedef long long i64;

typedef struct {
    double rc0_gv;
    double beta;
    double gamma_sw;
    double kappa_gv_inv;
    double m0;
} TMParams;

static double absd(double x) {
    return (x < 0.0) ? -x : x;
}

/* Aproximação racional para exp(x) em faixa operacional curta [-8,8]. */
static double exp_approx(double x) {
    double y = x;
    if (y > 8.0) y = 8.0;
    if (y < -8.0) y = -8.0;

    /* Pade-like simples: exp(y) ≈ (1 + y/2 + y^2/10 + y^3/120) / (1 - y/2 + y^2/10 - y^3/120) */
    double y2 = y * y;
    double y3 = y2 * y;
    double num = 1.0 + 0.5 * y + 0.1 * y2 + (1.0 / 120.0) * y3;
    double den = 1.0 - 0.5 * y + 0.1 * y2 - (1.0 / 120.0) * y3;

    if (absd(den) < 1.0e-12) {
        den = (den < 0.0) ? -1.0e-12 : 1.0e-12;
    }

    return num / den;
}

/* Potência inteira positiva para manter determinismo sem libm. */
static double powi(double base, i64 exp) {
    double result = 1.0;
    i64 n = exp;
    while (n > 0) {
        if (n & 1LL) result *= base;
        base *= base;
        n >>= 1;
    }
    return result;
}

/* Aproximação para (m/m0)^beta com beta≈1 no primeiro paper.
 * Para beta não-inteiro, usar linearização local.
 */
static double ratio_pow_beta(double ratio, double beta) {
    i64 ibeta = (i64)(beta + 0.5);
    double delta = beta - (double)ibeta;
    double core = powi(ratio, (ibeta > 0) ? ibeta : 1);
    /* linearização: ratio^(ibeta+delta) ≈ core * (1 + delta*(ratio-1)) */
    return core * (1.0 + delta * (ratio - 1.0));
}

double tm_rc_gv(double m, double sw, const TMParams* p) {
    double ratio = (p->m0 != 0.0) ? (m / p->m0) : 1.0;
    double mag = ratio_pow_beta(ratio, p->beta);
    double sw_term = 1.0 + p->gamma_sw * sw;
    return p->rc0_gv * mag * sw_term;
}

double tm_transmittance(double rigidity_gv, double m, double sw, const TMParams* p) {
    double rc = tm_rc_gv(m, sw, p);
    double arg = -p->kappa_gv_inv * (rigidity_gv - rc);
    double e = exp_approx(arg);
    return 1.0 / (1.0 + e);
}
