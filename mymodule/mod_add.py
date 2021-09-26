def mod_add(x, y, m):
    # reduce x and y
    x_1 = x % m
    y_1 = y % m

    # compute sum
    z = x_1 + y_1

    # reduce sum if it's greater or equal to m
    if z >= m:
        z = z - m

    return z
