#include "pantheon_freestanding.h"

#define RLL_FNV_OFFSET 14695981039346656037ull
#define RLL_FNV_PRIME  1099511628211ull

#define RLL_CRC32_INIT 0xFFFFFFFFu
#define RLL_CRC32_POLY_REV 0xEDB88320u
#define RLL_CRC32_FINAL_XOR 0xFFFFFFFFu

#define RLL_ENOSYS_NEG (-38ll)
#define RLL_EINVAL_NEG (-22ll)

#define RLL_ONE_Q16_I64 65536ll
#define RLL_SQRT3_2_Q16_I64 56756ll
#define RLL_INV_SQRT3_2_Q16_I64 75674ll
#define RLL_COSMO_Z_H_Q16 10138u

rll_i64 rll_sqrt3_2_project_q16(rll_i64 x_q16) {
    return (x_q16 * RLL_SQRT3_2_Q16_I64) >> 16;
}

rll_i64 rll_sqrt3_2_reverse_q16(rll_i64 x_q16) {
    return (x_q16 * RLL_INV_SQRT3_2_Q16_I64) >> 16;
}

rll_i64 rll_sqrt3_2_decay_q16(rll_i64 state_q16, rll_i64 input_q16) {
    return input_q16 + rll_sqrt3_2_project_q16(state_q16);
}

rll_hex_q16 rll_sqrt3_2_hex_grid_q16(rll_i64 row, rll_i64 col, rll_i64 side_q16) {
    rll_hex_q16 p;
    rll_i64 half_shift = (row & 1ll) * (side_q16 >> 1);
    p.x_q16 = (col * side_q16) + half_shift;
    p.y_q16 = rll_sqrt3_2_project_q16(row * side_q16);
    return p;
}

rll_sqrt3_2_pivot_q16 rll_sqrt3_2_cosmo_pivot_q16(void) {
    rll_sqrt3_2_pivot_q16 p;
    p.a_q16 = RLL_SQRT3_2_Q16;
    p.z_q16 = RLL_COSMO_Z_H_Q16;
    return p;
}


#if defined(__linux__) && defined(__x86_64__)
#define RLL_SYS_WRITE 1ull
#endif

rll_u64 rll_fnv1a64(const rll_u8 *data, rll_u64 len) {
    rll_u64 h = RLL_FNV_OFFSET;
    rll_u64 i = 0ull;
    if ((data == (const rll_u8 *)0) && (len != 0ull)) {
        return h;
    }
    while (i < len) {
        h ^= (rll_u64)data[i];
        h *= RLL_FNV_PRIME;
        i++;
    }
    return h;
}

rll_u32 rll_crc32(const rll_u8 *data, rll_u64 len) {
    rll_u32 crc = RLL_CRC32_INIT;
    rll_u64 i = 0ull;
    if ((data == (const rll_u8 *)0) && (len != 0ull)) {
        return (rll_u32)(crc ^ RLL_CRC32_FINAL_XOR);
    }
    while (i < len) {
        rll_u32 x = (crc ^ (rll_u32)data[i]) & 0xFFu;
        rll_u32 j = 0u;
        while (j < 8u) {
            rll_u32 mask = (rll_u32)(-(rll_i64)(x & 1u));
            x = (x >> 1u) ^ (RLL_CRC32_POLY_REV & mask);
            j++;
        }
        crc = (crc >> 8u) ^ x;
        i++;
    }
    return (rll_u32)(crc ^ RLL_CRC32_FINAL_XOR);
}

rll_i64 rll_sys_write1(const void *buf, rll_u64 len) {
    if ((buf == (const void *)0) && (len != 0ull)) {
        return RLL_EINVAL_NEG;
    }
#if defined(__linux__) && defined(__x86_64__)
    rll_u64 ret;
    __asm__ volatile(
        "syscall"
        : "=a"(ret)
        : "a"(RLL_SYS_WRITE), "D"(1ull), "S"(buf), "d"(len)
        : "rcx", "r11", "memory"
    );
    return (rll_i64)ret;
#elif defined(__linux__) && (defined(__aarch64__) || defined(__arm__) || defined(__riscv) || defined(__riscv__))
    (void)buf;
    (void)len;
    return RLL_ENOSYS_NEG;
#else
    (void)buf;
    (void)len;
    return RLL_ENOSYS_NEG;
#endif
}
