import common
import math

def multiply(x, y, b, params):
    z = []
    for i in range(len(x) + len(y) - 1):
        z.append(0)

    for i in range(1, len(x)):
        carry = 0
        for j in range(1, len(y)):
            t = z[(i+j) - 1] + (x[i]*y[j]) + carry
            carry = math.floor(t / b)
            z[(i+j) - 1] = t - (carry*b)
        z[(i+len(y)) - 1] = carry
        if z[(len(x)+len(y)) -2] == 0:
            k = (len(x) + len(y)) - 2
        else:
            k = (len(x) + len(y)) - 1

    return z


def calc(params):
    # Parses the base b from the params
    b = int(params['radix'])
    # Parses the x value from the params
    x = common.split(params['x'], b)
    # Parses the y value from the params
    y = common.split(params['y'], b)

    # Calculates and parses the answer
    params['answer'] = common.concat(multiply(x, y, b, params))


    return params