import copy

from mymodule import datatypes


def div_with_r(x, y):

    pos_r = x.is_positive
    pos_q = (x.is_positive and y.is_positive) or (x.is_negative and y.is_negative)

    a = copy.deepcopy(x)
    b = copy.deepcopy(y)
    a.make_positive()
    b.make_positive()

    q = datatypes.LargeInteger('0', x.get_radix())
    r = a

    while r >= b:
        r = r - b
        q = q + datatypes.LargeInteger('1', x.get_radix())

    if not pos_q:
        q.make_negative()

    if not pos_r:
        r.make_negative()

    return [q, r]



