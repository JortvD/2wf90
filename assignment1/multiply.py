import common
import math

def multiply(x, y):
    z = []
    m = x.num_digits
    n = y.num_digits
    for i in range(m + n):
        z.append(0)

    for i in range(1, m):
        carry = 0
        for j in range(1, n):
            t = z[(i+j) - 1] + (x[i]*y[j]) + carry
            carry = math.floor(t / x.radix)
            z[(i+j) - 1] = t - (carry*x.radix)
        z[(i+n) - 1] = carry
        if z[(m+n) -2] == 0:
            k = (m + n) - 2
        else:
            k = (m + n) - 1

    return z
