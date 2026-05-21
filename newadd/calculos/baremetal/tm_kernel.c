/* tm_kernel.c
 * Núcleo determinístico para T_M sem chamadas de libc.
 * Compilação sugerida (objeto freestanding):
 *   cc -std=c11 -ffreestanding -fno-builtin -c tm_kernel.c
 */

typedef unsigned long long u64;
typedef long long i64;
typedef unsigned int u32;
typedef unsigned char u8;

typedef struct {
    double rc0_gv;
    double beta;
    double gamma_sw;
    double kappa_gv_inv;
    double m0;
} TMParams;

typedef struct {
    u32 generation;
    u32 tick;
    u32 watchdog_limit;
    u32 watchdog_counter;
    u32 rollback_count;
    u32 failsafe_code;
    u32 crc32_sw;
    u32 crc32_hw_hint;
    u8 route_idx[4];
    u8 lane_mask;
    u8 reserved[3];
} TMControlState;

typedef struct {
    u8 cpu_class;
    u8 simd_class;
    u8 kvm_hint;
    u8 gpu_hint;
    u8 route_matrix[10][10][10][4];
} TMRouteMap;

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

static u32 tm_crc32_step(u32 crc, u8 byte) {
    u32 c = crc ^ (u32)byte;
    u32 i = 0;
    while (i < 8U) {
        u32 mask = (u32)(-(i64)(c & 1U));
        c = (c >> 1) ^ (0xEDB88320U & mask);
        i++;
    }
    return c;
}

static u32 tm_crc32_buf(const u8* buf, u32 len) {
    u32 crc = 0xFFFFFFFFU;
    u32 i = 0;
    while (i < len) {
        crc = tm_crc32_step(crc, buf[i]);
        i++;
    }
    return ~crc;
}

static void tm_control_checkpoint(const TMControlState* in, TMControlState* out) {
    *out = *in;
}

static void tm_control_restore(const TMControlState* from, TMControlState* to) {
    *to = *from;
}

static u32 tm_route_compose_id(const TMControlState* s) {
    u32 a = (u32)s->route_idx[0] % 10U;
    u32 b = (u32)s->route_idx[1] % 10U;
    u32 c = (u32)s->route_idx[2] % 10U;
    u32 d = (u32)s->route_idx[3] % 4U;
    return (((a * 10U) + b) * 10U + c) * 4U + d;
}

static u32 tm_route_next_prime_stride(u32 route_id, u32 step) {
    const u32 dr = 7U;
    const u32 dc = 3U;
    return (route_id + dr * step + dc) % 4000U;
}

static u32 tm_failsafe_watchdog(TMControlState* cur, const TMControlState* stable) {
    u32 crc = tm_crc32_buf((const u8*)cur, (u32)sizeof(TMControlState));
    if (crc != cur->crc32_sw) {
        tm_control_restore(stable, cur);
        cur->rollback_count = stable->rollback_count + 1U;
        cur->failsafe_code = 0xE001U;
        cur->crc32_sw = tm_crc32_buf((const u8*)cur, (u32)sizeof(TMControlState));
        return 1U;
    }
    if (cur->watchdog_counter > cur->watchdog_limit) {
        tm_control_restore(stable, cur);
        cur->rollback_count = stable->rollback_count + 1U;
        cur->failsafe_code = 0xE002U;
        cur->crc32_sw = tm_crc32_buf((const u8*)cur, (u32)sizeof(TMControlState));
        return 1U;
    }
    return 0U;
}

u32 tm_control_tick(TMControlState* state, const TMRouteMap* route, u32 input_entropy) {
    TMControlState snapshot;
    u32 route_id;
    u32 next_id;

    tm_control_checkpoint(state, &snapshot);

    state->tick += 1U;
    state->watchdog_counter += 1U;
    route_id = tm_route_compose_id(state);
    next_id = tm_route_next_prime_stride(route_id, (state->tick ^ input_entropy) & 0x3FU);

    state->route_idx[0] = (u8)((next_id / 400U) % 10U);
    state->route_idx[1] = (u8)((next_id / 40U) % 10U);
    state->route_idx[2] = (u8)((next_id / 4U) % 10U);
    state->route_idx[3] = (u8)(next_id % 4U);

    state->lane_mask = route->route_matrix
        [state->route_idx[0]][state->route_idx[1]][state->route_idx[2]][state->route_idx[3]];

    state->crc32_hw_hint = (u32)route->simd_class;
    state->crc32_sw = tm_crc32_buf((const u8*)state, (u32)sizeof(TMControlState));
    if (tm_failsafe_watchdog(state, &snapshot)) {
        return 0U;
    }
    state->watchdog_counter = 0U;
    return 1U;
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
