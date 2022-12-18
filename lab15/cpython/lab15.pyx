from cython.cimports.libc.math import cos, exp

cdef double f(double x):
    return cos(x + x * x * x) if x <= 1.0 else exp(-x * x) - x * x + 2.0 * x


cpdef integrate(double a, double b):
    cdef int n = 100000000
    cdef double h = (b - a) / n
    cdef double h2 = h * 0.5
    cdef double s = 0.0
    for i in range(n):
        s += f(a + i * h + h2)
    return s * h

## это сами
# def sum_array(a):
#     cdef int s = 0
#     for i in a:
#         s += i
#     return s