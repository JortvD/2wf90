from mymodule.datatypes import LargeInteger
from mymodule.euclid import euclid

def inverse(a, m):
    res = euclid(a, m)
    a_ = res[0]
    x1 = res[1]

    if a_ == LargeInteger('1', radix=a.radix):
        return x1
    else:
        return "inverse does not exist"
