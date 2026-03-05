#ifndef RLL_KERNEL_BRIDGE_H
#define RLL_KERNEL_BRIDGE_H

#ifdef __cplusplus
extern "C" {
#endif

int rll_arch_detect(void);
int rll_kernel_score(int x, int y);

#ifdef __cplusplus
}
#endif

#endif
