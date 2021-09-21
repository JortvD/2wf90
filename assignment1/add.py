import common
from subtract import subtract


def add(x, y, b, params):
    neg, sign = common.negativeInput(x,y)
    if neg:
        return subtract(x, y, b, params)
    else:
        carry = 0
        z = []
        z.append(0)
        for i in range(1, max(len(x), len(y))):
            z.append(x[i] + y[i] + carry)
            if z[i-1] >= b:
                z[i-1] = z[i-1] - b
                carry = 1
            else:
                carry = 0

        if carry == 1:
            k = max(len(x), len(y)) + 1
            z.append(1)
        else:
            k = max(len(x), len(y))

        z[0] = sign
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