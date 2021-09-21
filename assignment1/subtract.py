import add
import common

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

def calc(params):
    # Parses the base b from the params
    b = int(params['radix'])
    # Parses the x value from the params
    x = common.split(params['x'], b)
    # Parses the y value from the params
    y = common.split(params['y'], b)

    # Calculates and parses the answer
    params['answer'] = common.concat(subtract(x, y, b))

    return params
