public final class KernelBridge {
    private KernelBridge() {}

    static {
        // Exemplo: System.loadLibrary("rll_kernel_bridge");
    }

    public static native int archDetect();
    public static native int kernelScore(int x, int y);
}
