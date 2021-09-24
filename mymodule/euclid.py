def euclid(a, b):
    a_1 = abs(a)
    b_1 = abs(b)
    x_1 = 1
    x_2 = 0
    y_1 = 0
    y_2 = 1

    while b_1 > 0:
        q = 0  # division needed
        r = a_1 - q * b_1

        a_1 = b_1
        b_1 = r

        x_3 = x_1 - q * x_2
        y_3 = y_1 - q * y_2

        x_1 = x_2
        y_1 = y_2

        x_2 = x_3
        y_2 = y_3

    d = a_1

    if a >= 0:
        x = x_1
    else:
        x = -x_1

    if b >= 0:
        y = y_1
    else:
        y = -y_1

    return d, x, y
