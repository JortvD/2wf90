import common


def add(x, y, b, params):
    carry = 0
    z = []

    for i in range(len(x), max(len(x), len(y))):
            x[i] = 0

    for i in range(len(y), max(len(x), len(y))):
            y[i] = 0

    for i in range(0, max(len(x), len(y))):
        z.append(x[i] + y[i] + carry)
        if z[i] >= b:
            z[i] = z[i] - b
            carry = 1
        else:
            carry = 0

    if carry == 1:
        k = max(len(x), len(y)) + 1
        z.append(1)
    else:
        k = max(len(x), len(y))

    return z


def calc(params):
    # Parses the base b from the params
    b = int(params['radix'])
    # Parses the x value from the params
    x = common.split(params['x'], b)
    # Parses the y value from the params
    y = common.split(params['y'], b)

    # Calculates and parses the answer
    params['answer'] = common.concat(add(x, y, b, params))

    return params