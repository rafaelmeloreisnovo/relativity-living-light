#include "kernel_bridge.h"

#if defined(__x86_64__) || defined(_M_X64)
extern int rll_arch_detect_x86_64(void);
#endif

int rll_arch_detect(void) {
#if defined(__x86_64__) || defined(_M_X64)
    return rll_arch_detect_x86_64();
#elif defined(__aarch64__)
    return 64;
#elif defined(__arm__)
    return 32;
#else
    return 0;
#endif
}

int rll_kernel_score(int x, int y) {
    int arch = rll_arch_detect();
    int mix = (x * 31) ^ (y * 17);
    return mix + arch;
}
