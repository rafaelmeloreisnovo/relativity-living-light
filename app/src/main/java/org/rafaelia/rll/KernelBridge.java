package org.rafaelia.rll;

public final class KernelBridge {
    private KernelBridge() {}

    static {
        System.loadLibrary("rll_kernel_bridge");
    }

    public static native int archDetect();
    public static native int kernelScore(int x, int y);
}
