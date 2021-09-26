from mymodule.datatypes import LargeInteger
from mymodule.reduce import reduce


def mod_add(x, y, m):
    x_1 = x % m
    y_1 = y % m

    z = x_1 + y_1

    if z < m:
        return z
    else:
        return z - m


def calc(params):
    b = int(params['radix'])
    x = LargeInteger(params['x'], b)
    y = LargeInteger(params['y'], b)
    m = LargeInteger(params['m'], b)

    params['answer'] = str(mod_add(x, y, m))

    return params
