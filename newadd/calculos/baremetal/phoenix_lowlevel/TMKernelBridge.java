public final class TMKernelBridge {
    static {
        System.loadLibrary("phxcore");
    }

    private TMKernelBridge() {}

    public static native int detectCaps();
}
