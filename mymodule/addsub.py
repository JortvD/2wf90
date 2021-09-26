import copy
from mymodule import datatypes


def add(x, y):

    make_negative = False

    if x.is_negative and y.is_negative:
        make_negative = True
    elif y.is_negative:
        # x positive, y negative
        # y = - y'
        # x + y = x - y'
        # use subtraction(x, y') where y' is pos value of y
        y_1 = copy.deepcopy(y)
        y_1.make_positive()
        res = x - y_1
        return res
    elif x.is_negative:
        # x negative, y positive
        # x = - x'
        # x + y = y - x'
        # use subtraction(y, x') where x' is pos value of y
        x_1 = copy.deepcopy(x)
        x_1.make_positive()
        res = y - x_1
        return res

    # Assumption that x and y > 0
    carry = 0
    z = datatypes.LargeInteger(None, radix=x.radix)
    m = x.num_digits
    n = y.num_digits
    x.prepend_zeroes(max(n-m, 0))
    y.prepend_zeroes(max(m-n, 0))
    for i in range(max(m, n) - 1, -1, -1):
        z_i = x[i] + y[i] + carry
        if z_i >= x.radix:
            z_i -= x.radix
            carry = 1
        else:
            carry = 0
        z.append(z_i)

    if carry == 1:
        z.append(1)

    if make_negative:
        z.make_negative()

    z.invert_digits()
    return z


def subtract(x, y):
    carry = 0
    flip = False

    if x.is_negative and y.is_negative:
        # x = - x', y = - y'
        # x - y = - x' + y' = y' - x'
        # so we assign the pos value of y to x_1
        # and the pos value of x to y_1
        x_1 = copy.deepcopy(y)
        x_1.make_positive()
        y_1 = copy.deepcopy(x)
        y_1.make_positive()
    elif y.is_negative:
        # x positive, y negative
        # y = - y'
        # x - y = x + y'
        # turn use y' (pos value of y) and add it to x
        y_1 = copy.deepcopy(y)
        y_1.make_positive()
        return x + y_1
    elif x.is_negative:
        # x negative, y positive
        # x = - x'
        # x - y = - x' - y = - ( x' + y )
        # use x' (pos value of x), add it to y and take the neg value of the result
        x_1 = copy.deepcopy(x)
        x_1.make_positive()
        res = x_1 + y
        res.make_negative()
        return res
    else:
        x_1 = copy.deepcopy(x)
        y_1 = copy.deepcopy(y)

    if x_1 < y_1:
        # x_1 - y_1 = - (y_1 - x_1)
        # compute y_1 - x_1 instead and take the result with the opposite sign
        flip = True
        old_x = copy.deepcopy(x_1)
        x_1 = copy.deepcopy(y_1)
        y_1 = copy.deepcopy(old_x)

    m = x_1.num_digits
    n = y_1.num_digits
    y_1.prepend_zeroes(m - n)
    z = datatypes.LargeInteger(None, radix=x.radix)
    for i in range(m-1, -1, -1):
        z_i = x_1[i] - y_1[i] - carry
        if z_i < 0:
            z_i += x_1.radix
            carry = 1
        else:
            carry = 0
        z.append(z_i)
    
    if carry == 1:
        z.make_negative()

    if flip:
        z.flip_sign()

    z.invert_digits()
    z.strip_leading_zeroes()

    return z
