from mymodule import datatypes

def mod_subtract(x, y, m):
    x_1 = x % m
    y_1 = y % m
    z = x_1 - y_1

    if z < datatypes.LargeInteger('0'):
        z += m

    return z
