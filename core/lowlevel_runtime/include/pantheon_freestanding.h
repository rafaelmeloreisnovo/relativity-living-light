#ifndef RLL_PANTHEON_FREESTANDING_H
#define RLL_PANTHEON_FREESTANDING_H

#ifdef __cplusplus
extern "C" {
#endif

/* Tipos explícitos sem dependência de stdlib/libc. */
typedef unsigned char rll_u8;
typedef unsigned int rll_u32;
typedef unsigned long long rll_u64;
typedef long long rll_i64;

#define RLL_SQRT3_2_Q16 56756u
#define RLL_ONE_Q16 65536u

typedef struct rll_hex_q16 {
    rll_i64 x_q16;
    rll_i64 y_q16;
} rll_hex_q16;

typedef struct rll_sqrt3_2_pivot_q16 {
    rll_u32 a_q16;
    rll_u32 z_q16;
} rll_sqrt3_2_pivot_q16;

typedef struct rll_sqrt3_2_spiral_q16 {
    rll_i64 radius_q16;
    rll_i64 x_q16;
    rll_i64 y_q16;
    rll_i64 equilateral_height_q16;
    rll_u32 sector60;
} rll_sqrt3_2_spiral_q16;

/* RAFAELIA sqrt(3)/2 Q16.16 kernels: sem heap, sem libc, rota de rollback explícita. */
rll_i64 rll_sqrt3_2_project_q16(rll_i64 x_q16);
rll_i64 rll_sqrt3_2_reverse_q16(rll_i64 x_q16);
rll_i64 rll_sqrt3_2_decay_q16(rll_i64 state_q16, rll_i64 input_q16);
rll_hex_q16 rll_sqrt3_2_hex_grid_q16(rll_i64 row, rll_i64 col, rll_i64 side_q16);
rll_sqrt3_2_pivot_q16 rll_sqrt3_2_cosmo_pivot_q16(void);
rll_sqrt3_2_spiral_q16 rll_sqrt3_2_spiral_step_q16(rll_u32 step, rll_i64 radius0_q16);

/*
 * Pantheon freestanding low-level runtime (não é dataset Pantheon+ cosmológico).
 * - sem heap/malloc
 * - sem stdlib/stdio/string
 * - FNV-1a 64-bit: hash NÃO criptográfico
 * - CRC-32 IEEE (poly reversed 0xEDB88320)
 */

rll_u64 rll_fnv1a64(const rll_u8 *data, rll_u64 len);
rll_u32 rll_crc32(const rll_u8 *data, rll_u64 len);
rll_i64 rll_sys_write1(const void *buf, rll_u64 len);

#ifdef __cplusplus
}
#endif

#endif
