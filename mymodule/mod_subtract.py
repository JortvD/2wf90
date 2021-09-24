from mymodule.datatypes import LargeInteger
from mymodule.reduce import reduce


def mod_subtract(x, y, m):
    x = reduce(x, m)
    y = reduce(y, m)
    z = x - y

    if z < 0:
        z += m

    return z


def calc(params):
    b = int(params['radix'])
    x = LargeInteger(params['x'], b)
    y = LargeInteger(params['y'], b)
    m = LargeInteger(params['m'], b)

    params['answer'] = str(mod_subtract(x, y, m))

    return params



