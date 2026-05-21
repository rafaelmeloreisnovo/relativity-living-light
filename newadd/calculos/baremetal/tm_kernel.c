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
    u32 bittrail_head;
    u32 bittrail_hash;
    u8 route_idx[4];
    u8 lane_mask;
    u8 reserved[3];
} TMControlState;

typedef struct {
    double u;
    double v;
    double psi;
    double chi;
    double rho;
    double delta;
    double sigma;
} TMToroidalState;

typedef struct {
    u8 cpu_class;
    u8 simd_class;
    u8 kvm_hint;
    u8 gpu_hint;
    u8 route_matrix[10][10][10][4];
} TMRouteMap;

typedef struct {
    u32 seq;
    u32 event_code;
    u32 route_id;
    u32 hash_chain;
} TMAuditEvent;

typedef struct {
    u32 version;
    u32 abi_flags;
    u32 route_cap;
    u32 audit_cap;
    u32 crc_mode;
    u32 interoperability_tag;
} TMBootstrapConfig;

typedef struct {
    u32 ticks_total;
    u32 ticks_ok;
    u32 ticks_fail;
    u32 rollback_total;
    u32 audit_events;
    u32 route_entropy_xor;
    u32 reliability_ppm;
    u32 interoperability_score;
} TMKernelMetrics;

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

static u32 tm_control_crc(const TMControlState* s) {
    u32 crc = 0xFFFFFFFFU;
    const u8* b = (const u8*)s;
    u32 i = 0;
    while (i < (u32)sizeof(TMControlState)) {
        if ((i >= 24U && i < 28U) || (i >= 28U && i < 32U)) {
            i++;
            continue;
        }
        crc = tm_crc32_step(crc, b[i]);
        i++;
    }
    return ~crc;
}

static u32 tm_fnv1a_step(u32 h, u32 x) {
    h ^= x;
    h *= 0x01000193U;
    return h;
}

static void tm_audit_event_write(TMAuditEvent* trail, u32 cap, TMControlState* s, u32 event_code, u32 route_id) {
    u32 pos;
    TMAuditEvent e;
    u32 h;
    if (cap == 0U) return;
    pos = s->bittrail_head % cap;
    e.seq = s->tick;
    e.event_code = event_code;
    e.route_id = route_id;
    h = s->bittrail_hash;
    h = tm_fnv1a_step(h, e.seq);
    h = tm_fnv1a_step(h, e.event_code);
    h = tm_fnv1a_step(h, e.route_id);
    e.hash_chain = h;
    trail[pos] = e;
    s->bittrail_hash = h;
    s->bittrail_head += 1U;
}

u32 tm_bootstrap_config(TMBootstrapConfig* cfg, TMControlState* state, TMKernelMetrics* metrics) {
    if (cfg == (void*)0 || state == (void*)0 || metrics == (void*)0) return 0U;
    cfg->version = 1U;
    cfg->abi_flags = 0x01U;
    cfg->crc_mode = 1U;
    cfg->interoperability_tag = 0x524C4C31U; /* "RLL1" */
    if (cfg->route_cap == 0U) cfg->route_cap = 4000U;
    if (cfg->audit_cap == 0U) cfg->audit_cap = 256U;

    state->generation += 1U;
    state->tick = 0U;
    state->watchdog_counter = 0U;
    state->rollback_count = 0U;
    state->failsafe_code = 0U;
    state->bittrail_head = 0U;
    state->bittrail_hash = 0x811C9DC5U;
    state->crc32_sw = tm_control_crc(state);

    metrics->ticks_total = 0U;
    metrics->ticks_ok = 0U;
    metrics->ticks_fail = 0U;
    metrics->rollback_total = 0U;
    metrics->audit_events = 0U;
    metrics->route_entropy_xor = 0U;
    metrics->reliability_ppm = 1000000U;
    metrics->interoperability_score = 100U;
    return 1U;
}

static double tm_wrap01(double x) {
    double y = x;
    while (y >= 1.0) y -= 1.0;
    while (y < 0.0) y += 1.0;
    return y;
}

static u32 tm_attractor42_index(const TMToroidalState* s) {
    u32 a = (u32)(s->u * 7.0) % 7U;
    u32 b = (u32)(s->v * 6.0) % 6U;
    return (a * 6U + b) % 42U;
}

void tm_toroidal_map(TMToroidalState* s, u32 entropy_milli, u32 hash_mix) {
    const double alpha = 0.25;
    double hin = (double)(entropy_milli & 0xFFFFU) / 65535.0;
    double cin = (double)(hash_mix & 0xFFFFU) / 65535.0;
    double h = (1.0 - alpha) * s->rho + alpha * hin;
    double c = (1.0 - alpha) * s->delta + alpha * cin;
    double phi = (1.0 - h) * c;

    s->u = tm_wrap01(s->u + phi + 0.3819660112501051);
    s->v = tm_wrap01(s->v + h + 0.5 * phi);
    s->psi = tm_wrap01(s->psi + c + 0.3333333333333333 * phi);
    s->chi = tm_wrap01(s->chi + 0.75 * h + 0.25 * c);
    s->rho = tm_wrap01(h);
    s->delta = tm_wrap01(c);
    s->sigma = tm_wrap01((double)tm_attractor42_index(s) / 42.0);
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
    u32 crc = tm_control_crc(cur);
    if (crc != cur->crc32_sw) {
        tm_control_restore(stable, cur);
        cur->rollback_count = stable->rollback_count + 1U;
        cur->failsafe_code = 0xE001U;
        cur->crc32_sw = tm_control_crc(cur);
        return 1U;
    }
    if (cur->watchdog_counter > cur->watchdog_limit) {
        tm_control_restore(stable, cur);
        cur->rollback_count = stable->rollback_count + 1U;
        cur->failsafe_code = 0xE002U;
        cur->crc32_sw = tm_control_crc(cur);
        return 1U;
    }
    return 0U;
}

u32 tm_control_tick(TMControlState* state, const TMRouteMap* route, u32 input_entropy, TMAuditEvent* trail, u32 trail_cap) {
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
    state->crc32_sw = tm_control_crc(state);
    if (tm_failsafe_watchdog(state, &snapshot)) {
        tm_audit_event_write(trail, trail_cap, state, state->failsafe_code, route_id);
        return 0U;
    }
    tm_audit_event_write(trail, trail_cap, state, 0x9000U, next_id);
    state->watchdog_counter = 0U;
    return 1U;
}

u32 tm_benchmark_ticks(TMControlState* state,
                       const TMRouteMap* route,
                       TMAuditEvent* trail,
                       u32 trail_cap,
                       u32 iterations,
                       TMKernelMetrics* metrics) {
    u32 i = 0;
    u32 ok = 0;
    u32 fail = 0;
    if (state == (void*)0 || route == (void*)0 || metrics == (void*)0) return 0U;
    while (i < iterations) {
        u32 entropy = (i * 2654435761U) ^ state->bittrail_hash ^ state->generation;
        u32 step_ok = tm_control_tick(state, route, entropy, trail, trail_cap);
        metrics->ticks_total += 1U;
        metrics->route_entropy_xor ^= tm_route_compose_id(state) ^ entropy;
        if (step_ok) {
            ok += 1U;
            metrics->ticks_ok += 1U;
        } else {
            fail += 1U;
            metrics->ticks_fail += 1U;
        }
        metrics->rollback_total = state->rollback_count;
        i++;
    }
    metrics->audit_events = state->bittrail_head;
    metrics->reliability_ppm = (iterations == 0U) ? 0U : (ok * 1000000U) / iterations;
    metrics->interoperability_score = (fail == 0U) ? 100U : (100U - ((fail * 100U) / (iterations ? iterations : 1U)));
    return ok;
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
