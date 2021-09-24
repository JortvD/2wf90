import math
from mymodule import datatypes

def multiply(x, y):
    sign = 0
    if x.is_negative ^ y.is_negative:
        sign = 1

    z = datatypes.LargeInteger(None, radix=x.radix)

    m = x.num_digits
    n = y.num_digits

    for i in range(n + m + 1):
        z.append(0)

    x.invert_digits()
    y.invert_digits()
    for i in range(0, m):
        carry = 0
        for j in range(0, n):
            t = z[i+j] + (x[i]*y[j]) + carry
            carry = math.floor(t / x.radix)
            z[i+j] = t - (carry*x.radix)
        z[i+n] = carry
    if z[m+n-1] == 0:
        k = m + n - 2
    else:
        k = m + n - 1

    z.invert_digits()
    if sign == 1:
        z.make_negative()
    return z