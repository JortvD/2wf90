import copy

from mymodule import datatypes


def reduce(x, m):
    neg = x.is_negative
    x_1 = copy.deepcopy(x)

    k = len(x)
    n = len(m)

    for i in range(k-n, -1, -1):
        b_i = datatypes.LargeInteger('1', x_1.get_radix())
        for j in range(i):
            # b is always represented as 10 in radix b
            b_i = b_i * datatypes.LargeInteger('10', x_1.get_radix())

        bm = m * b_i

        if neg:
            # if x was negative then we have to look at the negative value of b_i * m
            bm.make_negative()
            # the while-loop stops when x_1 is larger than the neg value of b_i * m
            while x_1 <= bm:
                x_1 = x_1 - bm
        else:
            # the while-loop stops when x_1 is smaller than value of b_i * m
            while x_1 >= bm:
                x_1 = x_1 - bm

    if x_1 >= datatypes.LargeInteger('0') or x_1 == datatypes.LargeInteger('0'):
        x_1 = x_1
    else:
        if neg:
            # if x was negative then we add instead of subtract
            x_1 = m + x_1
        else:
            x_1 = m - x_1

    return x_1
