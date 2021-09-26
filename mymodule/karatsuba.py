from mymodule.datatypes import LargeInteger
from mymodule import profiler

def karatsuba_recursive(x, y, b):
    """
    @param b The radix
    """
    # If either x or y are 0 then return 0.
    if((len(x) == 0) | (len(y) == 0)): return LargeInteger('0', b)

    # Check if result should be negative. This data is not given through recursively, as it is not needed.
    negative = (bool(x.is_positive) ^ bool(y.is_positive))

    # If x and y are 1 then
    if(len(x) == 1 & len(y) == 1):
        # Multiply x[0] and y[0]
        profiler.count_operation('Multiply')
        mult = x[0] * y[0]

        # Return a LargeInteger of the two digits of the multiplication
        xy = LargeInteger([1 if negative else 0, mult//b, int(mult%b)], b)
        xy.strip_leading_zeroes()
        return xy

    # If the length of x or is uneven make it even by adding a lead 0
    if(len(x) % 2 == 1):
        x.prepend_zeroes(1)
    if(len(y) % 2 == 1):
        y.prepend_zeroes(1)

    n = max(len(x), len(y))

    # Add leading 0's to x and y to make them the same length
    x = LargeInteger([0] + [0] * (n - len(x)) + x.slice(0, len(x)), b)
    y = LargeInteger([0] + [0] * (n - len(y)) + y.slice(0, len(y)), b)

    xhi = LargeInteger([0] + x.slice(0, len(x)//2), b)
    xlo = LargeInteger([0] + x.slice(len(x)//2, len(x)), b)
    yhi = LargeInteger([0] + y.slice(0, len(y)//2), b)
    ylo = LargeInteger([0] + y.slice(len(y)//2, len(y)), b)

    # The high part of the karatsuba multiplication
    xhiyhi = karatsuba_recursive(xhi, yhi, b)
    # The low part of the karatsuba multiplcation
    xloylo = karatsuba_recursive(xlo, ylo, b)
    # The mid part of the mid part of the karatsuba multiplication
    mid = karatsuba_recursive(xhi + xlo, yhi + ylo, b)
    # The full mid part of the karatsuba multiplication
    xymid = mid - xhiyhi - xloylo
    xymid.strip_leading_zeroes()

    # The summation part of the karatsuba algorithm
    profiler.count_operation('Add')
    xy = xhiyhi.lshift(n) + xymid.lshift(n//2) + xloylo
    xy.strip_leading_zeroes()

    # Make negative if the result should be nagative
    if negative: xy.make_negative()

    return xy
