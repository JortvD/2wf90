import copy

from mymodule import datatypes


def div_with_r(x, y):
    if (x.is_positive and y.is_negative) or (x.is_negative and y.is_positive):
        neg = True
    else:
        neg = False

    a = copy.deepcopy(x)
    b = copy.deepcopy(y)
    a.make_positive()
    b.make_positive()

    q = datatypes.LargeInteger('0', x.get_radix())
    r = a

    while r >= b:
        r = r - b
        q = q + datatypes.LargeInteger('1', x.get_radix())

    if neg:
        r.make_negative()

    return [q, r]



