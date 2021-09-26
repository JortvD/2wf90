import copy
import math
from mymodule import datatypes, profiler


def multiply(x, y):
    sign = 0

    if x.is_negative ^ y.is_negative:
        sign = 1

    z = datatypes.LargeInteger(None, radix=x.radix)

    m = x.num_digits
    n = y.num_digits

    for i in range(n + m + 1):
        z.append(0)

    x_1 = copy.deepcopy(x)
    y_1 = copy.deepcopy(y)

    x_1.invert_digits()
    y_1.invert_digits()

    for i in range(0, m):
        carry = 0
        for j in range(0, n):
            profiler.count_operation('Add', count=3)
            profiler.count_operation('Multiply', count=2)
            t = z[i+j] + x_1[i] * y_1[j] + carry
            carry = t // x_1.radix
            z[i+j] = t - (carry * x_1.radix)
        z[i+n] = carry

    z.invert_digits()

    if sign == 1:
        z.make_negative()

    z.strip_leading_zeroes()

    return z
