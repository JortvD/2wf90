import copy

from mymodule import datatypes


def reduce(x, m):
    neg = x.is_negative
    x_1 = copy.deepcopy(x)

    if neg:
        x_1.make_positive()

    k = len(x)
    n = len(m)

    for i in range(k-n, -1, -1):
        b_i = datatypes.LargeInteger('1', 10)
        for j in range(i):
            # b is always represented as 10 in radix b
            b_i = b_i * datatypes.LargeInteger('10', x_1.get_radix())

        bm = m * b_i

        while x_1 >= bm:
            x_1 = x_1 - bm

    if x_1 >= datatypes.LargeInteger('0') or x_1 == datatypes.LargeInteger('0'):
        x_1 = x_1
    else:
        x_1 = m - x_1

    if neg:
        x_1.make_negative()

    return x_1
