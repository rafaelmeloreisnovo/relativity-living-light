/**
 * TMKernel.java
 * Variante determinística de baixa alocação para T_M em fixed-point Q32.32.
 */
public final class TMKernel {
    private TMKernel() {}

    private static final long ONE_Q32 = 1L << 32;

    private static long mulQ32(long a, long b) {
        return (a * b) >> 32;
    }

    /**
     * Aproximação logística simples em Q32.32 com faixa de estabilidade curta.
     * xQ32 = -kappa*(R-Rc)
     */
    private static long logisticQ32(long xQ32) {
        final long clamp = 8L << 32;
        long x = xQ32;
        if (x > clamp) x = clamp;
        if (x < -clamp) x = -clamp;

        /* exp(-x) aproximado por 1 - x + x²/2 em Q32.32 */
        long x2 = mulQ32(x, x);
        long expNegX = ONE_Q32 - x + (x2 >> 1);
        long den = ONE_Q32 + expNegX;
        if (den == 0L) den = 1L;
        return (ONE_Q32 << 32) / den;
    }

    public static long transmittanceQ32(long rigidityQ32, long rcQ32, long kappaQ32) {
        long delta = rigidityQ32 - rcQ32;
        long arg = -mulQ32(kappaQ32, delta);
        return logisticQ32(arg);
    }
}
