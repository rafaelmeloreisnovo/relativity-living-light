#include <jni.h>
#include "kernel_bridge.h"

JNIEXPORT jint JNICALL
Java_org_rafaelia_rll_KernelBridge_archDetect(JNIEnv *env, jclass clazz) {
    (void)env;
    (void)clazz;
    return (jint)rll_arch_detect();
}

JNIEXPORT jint JNICALL
Java_org_rafaelia_rll_KernelBridge_kernelScore(JNIEnv *env, jclass clazz, jint x, jint y) {
    (void)env;
    (void)clazz;
    return (jint)rll_kernel_score((int)x, (int)y);
}
