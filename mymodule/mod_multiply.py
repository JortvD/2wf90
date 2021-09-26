def mod_multiply(x, y, m):
    x_1 = x % m
    y_1 = y % m

    z = (x_1 * y_1) % m

    return z

