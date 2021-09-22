import common

def add(x, y, b, params):
    if common.isNegative(x) and common.isNegative(y):
        x[0] = 0
        y[0] = 0
        res = add(x, y, b, params)
        res[0] = 1
        return res
    elif common.isNegative(x):
        x[0] = 0
        res = subtract(y, x, b, params)
        return res
    elif common.isNegative(y):
        y[0] = 0
        res = subtract(x, y, b, params)
        return res

    # Assumption that x and y > 0
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

    return z

def subtract(x, y, b):
    carry = 0
    flip_carry = False

    if common.is_negative(x) and common.is_negative(y):
        # both negative
        # -x - -y => -x + y => y - x
        old_x = x
        x = y
        y = old_x
    elif common.is_negative(y):
        # x - -y = x + y
        # TODO call add function
        return add.add(x,y,b)
    elif common.is_negative(x):
        # -x - y => -(x - y)
        flip_carry = not flip_carry

    if common.smaller(x,y):
        old_x = x
        x = y
        y = old_x
        flip_carry = not flip_carry
    # negative numbers

    # x is negative, y is negative or both

    m = common.num_digits(x)
    n = common.num_digits(y)
    y_i = [0 for i in range(m - n)] + y
    # TODO adjust sign
    z = list()
    for i in range(m, 0, -1):
        z_i = x[i] - y_i[i] - carry
        if z_i < 0:
            z_i += b
            carry = 1
        else:
            carry = 0
        z.append(z_i)

    if flip_carry:
        carry ^= 1
    res = [carry] + z[::-1]
    return res

def calc(operation, params):
    # Parses the base b from the params
    b = int(params['radix'])
    # Parses the x value from the params
    x = common.split(params['x'], b)
    # Parses the y value from the params
    y = common.split(params['y'], b)

    # Calculates and parses the answer
    if operation == 'add':
        params['answer'] = common.concat(add(x, y, b, params))
    if operation == 'subtract':
        params['answer'] = common.concat(subtract(x, y, b, params))

    return params
