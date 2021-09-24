from mymodule import datatypes

def add(x, y):
    make_negative = False
    if x.is_negative and y.is_negative:
        make_negative = True
    elif y.is_negative:
        y.make_positive()
        res = x - y
        return res
    elif x.is_negative:
        res = x - y
        res.make_negative()
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
    flip_carry = False

    if x.is_negative and y.is_negative:
        # both negative
        # -x - -y => -x + y => y - x
        old_x = x
        x = y
        y = old_x
    elif y.is_negative:
        # x - -y = x + y
        y.make_positive()
        return x + y
    elif x.is_negative:
        # add(x, y), flip carry
        x.make_positive()
        res = x + y
        res.make_negative()
        return res

    if x < y:
        old_x = x
        x = y
        y = old_x
        flip_carry = not flip_carry

    m = x.num_digits
    n = y.num_digits
    y.prepend_zeroes(m - n)
    z = datatypes.LargeInteger(None, radix=x.radix)
    for i in range(m-1, -1, -1):
        z_i = x[i] - y[i] - carry
        if z_i < 0:
            z_i += x.radix
            carry = 1
        else:
            carry = 0
        z.append(z_i)

    if flip_carry:
        carry ^= 1
    
    if carry == 1:
        z.make_negative()
    z.invert_digits()
    z.strip_leading_zeroes()
    return z
