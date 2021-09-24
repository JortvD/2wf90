from mymodule.reduce import reduce


def mod_subtract(x, y, m):
    x = reduce(x, m)
    y = reduce(y, m)
    z = x - y

    if z < 0:
        z += m

    return z


