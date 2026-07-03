#include <stdio.h>
#include <math.h>

typedef struct {
    double x, y, z;
} Vec3;

double log_base(double n, double b) {
    return log(n) / log(b);
}

Vec3 torus(double R, double r, double theta, double phi) {
    Vec3 v;
    v.x = (R + r * cos(theta)) * cos(phi);
    v.y = (R + r * cos(theta)) * sin(phi);
    v.z = r * sin(theta);
    return v;
}

Vec3 spiral(Vec3 v, double t) {
    Vec3 out;
    double angle = t;

    out.x = v.x * cos(angle) - v.y * sin(angle);
    out.y = v.x * sin(angle) + v.y * cos(angle);
    out.z = v.z + 0.1 * t;

    return out;
}

int main() {
    double R = 3.0, r = 1.0;

    for (int i = 0; i < 100; i++) {
        double t = i * 0.1;

        Vec3 v = torus(R, r, t, t * 0.5);
        Vec3 s = spiral(v, t);

        double curv = log_base(i + 1, 7);

        printf("%d | %.3f %.3f %.3f | curv=%.3f\n",
               i, s.x, s.y, s.z, curv);
    }

    return 0;
}
