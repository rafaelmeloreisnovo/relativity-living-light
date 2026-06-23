#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define RLL_OK 0
#define RLL_ERR 1

typedef struct {
    double omega_m;
    double omega_s0;
    double z_t;
    double w_t;
} rll_bg_params;

typedef struct {
    double z;
    double a;
    double f;
    double rho_factor;
    double e2;
    double h_over_h0;
    double w_eff;
    double omega_m_a;
    double omega_s_a;
    double dlnh_dlna;
} rll_bg_state;

static double rll_clip(double x, double lo, double hi) {
    if (x < lo) return lo;
    if (x > hi) return hi;
    return x;
}

double rll_transition_f_z(double z, double z_t, double w_t) {
    double arg = rll_clip((z - z_t) / w_t, -700.0, 700.0);
    return 1.0 / (1.0 + exp(arg));
}

double rll_df_dlna_z(double z, double z_t, double w_t) {
    double f = rll_transition_f_z(z, z_t, w_t);
    return f * (1.0 - f) * (1.0 + z) / w_t;
}

double rll_rho_factor_z(double z, double z_t, double w_t) {
    double a = 1.0 / (1.0 + z);
    double a_m3 = 1.0 / (a * a * a);
    double f = rll_transition_f_z(z, z_t, w_t);
    return f + (1.0 - f) * a_m3;
}

double rll_drho_factor_dlna_z(double z, double z_t, double w_t) {
    double a = 1.0 / (1.0 + z);
    double a_m3 = 1.0 / (a * a * a);
    double f = rll_transition_f_z(z, z_t, w_t);
    double df = rll_df_dlna_z(z, z_t, w_t);
    return df * (1.0 - a_m3) - 3.0 * (1.0 - f) * a_m3;
}

double rll_e2_z(double z, const rll_bg_params *p) {
    double a = 1.0 / (1.0 + z);
    double a_m3 = 1.0 / (a * a * a);
    double omega_lambda = 1.0 - p->omega_m - p->omega_s0;
    return p->omega_m * a_m3 + omega_lambda + p->omega_s0 * rll_rho_factor_z(z, p->z_t, p->w_t);
}

double rll_dlnh_dlna_z(double z, const rll_bg_params *p) {
    double a = 1.0 / (1.0 + z);
    double a_m3 = 1.0 / (a * a * a);
    double de2 = -3.0 * p->omega_m * a_m3 + p->omega_s0 * rll_drho_factor_dlna_z(z, p->z_t, p->w_t);
    double e2 = rll_e2_z(z, p);
    return 0.5 * de2 / e2;
}

int rll_background_eval_z(double z, const rll_bg_params *p, rll_bg_state *out) {
    double a, a_m3, e2, rf;
    if (p == NULL || out == NULL) return RLL_ERR;
    if (p->w_t <= 0.0 || z < -0.999999999) return RLL_ERR;
    a = 1.0 / (1.0 + z);
    a_m3 = 1.0 / (a * a * a);
    e2 = rll_e2_z(z, p);
    rf = rll_rho_factor_z(z, p->z_t, p->w_t);
    if (!(e2 > 0.0)) return RLL_ERR;
    out->z = z;
    out->a = a;
    out->f = rll_transition_f_z(z, p->z_t, p->w_t);
    out->rho_factor = rf;
    out->e2 = e2;
    out->h_over_h0 = sqrt(e2);
    out->w_eff = -out->f / rf;
    out->omega_m_a = p->omega_m * a_m3 / e2;
    out->omega_s_a = p->omega_s0 * rf / e2;
    out->dlnh_dlna = rll_dlnh_dlna_z(z, p);
    return RLL_OK;
}

#ifdef RLL_BACKGROUND_STANDALONE
static double arg_value(int argc, char **argv, const char *name, double fallback) {
    int i;
    for (i = 1; i + 1 < argc; ++i) {
        if (argv[i] && argv[i + 1] && strcmp(argv[i], name) == 0) return atof(argv[i + 1]);
    }
    return fallback;
}

static int arg_int_value(int argc, char **argv, const char *name, int fallback) {
    int i;
    for (i = 1; i + 1 < argc; ++i) {
        if (argv[i] && argv[i + 1] && strcmp(argv[i], name) == 0) return atoi(argv[i + 1]);
    }
    return fallback;
}

int main(int argc, char **argv) {
    rll_bg_params p;
    int i, n;
    double zmax;
    p.omega_m = arg_value(argc, argv, "--omega-m", 0.315);
    p.omega_s0 = arg_value(argc, argv, "--omega-s0", 0.059);
    p.z_t = arg_value(argc, argv, "--zt", 1.164);
    p.w_t = arg_value(argc, argv, "--wt", 0.405);
    zmax = arg_value(argc, argv, "--z-max", 10.0);
    n = arg_int_value(argc, argv, "--n", 501);
    if (n < 2) n = 2;
    printf("z,a,f,rho_factor,E2,H_over_H0,w_eff,Omega_m_a,Omega_s_a,dlnH_dlna\n");
    for (i = 0; i < n; ++i) {
        rll_bg_state s;
        double z = zmax * ((double)i) / ((double)(n - 1));
        if (rll_background_eval_z(z, &p, &s) != RLL_OK) return RLL_ERR;
        printf("%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g\n", s.z, s.a, s.f, s.rho_factor, s.e2, s.h_over_h0, s.w_eff, s.omega_m_a, s.omega_s_a, s.dlnh_dlna);
    }
    return RLL_OK;
}
#endif
