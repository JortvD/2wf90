import copy


def reduce(x, m):
    neg = x.is_negative

    r = copy.deepcopy(x)

    if neg:
        r.make_positive()

    while r >= m:
        r = r - m

    if neg:
        r.make_negative()

    return r
