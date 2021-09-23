import copy
from addsub import add, subtract
from datatypes import LargeInteger

def karatsuba_recursive(x, y, b, params):
    # If either x or y are 0 then return 0.
    if((len(x) == 0) | (len(y) == 0)): return LargeInteger('0', b)

    negative = (bool(x.is_positive) ^ bool(y.is_positive))

    # If x and y are 1 then
    if(len(x) == 1 & len(y) == 1):
        # Add 1 to the multiplication counter
        params['count_mul'] += 1
        # Multiply x[0] and y[0]
        mult = x[0] * y[0]
        
        # Return an array of the two digits of the multiplication, both mod b
        xy = LargeInteger([1 if negative else 0, int(mult//b), int(mult%b)], b)
        xy.strip_leading_zeroes()
        return xy
    
    # If the length of x is uneven 
    if(len(x) % 2 == 1): 
        # then add a 0 at the beginning of x
        x.insert(0, 0)
    if(len(y) % 2 == 1): 
        # then add a 0 at the beginning of y
        y.insert(0, 0)

    # Here we take that n is the largest length of either x and y
    n = max(len(x), len(y))
    x = LargeInteger([0] + [0] * (n - len(x)) + x.slice(0, len(x)), b)
    y = LargeInteger([0] + [0] * (n - len(y)) + y.slice(0, len(y)), b)

    # The high part of x
    xhi = LargeInteger([0] + x.slice(0, len(x)//2), b)
    # The low part of x
    xlo = LargeInteger([0] + x.slice(len(x)//2, len(x)), b)
    # The high part of y
    yhi = LargeInteger([0] + y.slice(0, len(y)//2), b)
    # The low part of y
    ylo = LargeInteger([0] + y.slice(len(y)//2, len(y)), b)

    # The high part of the karatsuba multiplication
    xhiyhi = karatsuba_recursive(xhi, yhi, b, params)
    # The low part of the karatsuba multiplcation
    xloylo = karatsuba_recursive(xlo, ylo, b, params)
    # The mid part of the mid part of the karatsuba multiplication
    mid = karatsuba_recursive(xhi + xlo, yhi + ylo, b, params)
    # The full mid part of the karatsuba multiplication
    xymid = mid - xhiyhi - xloylo
    xymid.strip_leading_zeroes()

    # The summation part of the karatsuba algorithm
    xy = xhiyhi.lshift(n) + xymid.lshift(n//2) + xloylo
    xy.strip_leading_zeroes()

    if negative: xy.make_negative()

    return xy

# The karatsuba function that is called from the script. It starts the recursive function.
def calc(params):
    # Parses the base b from the params
    b = int(params['radix'])
    # Parses the x value from the params
    x = LargeInteger(params['x'], b)
    # Parses the y value from the params
    y = LargeInteger(params['y'], b)

    # Resets the multiplication counter
    params['count_mul'] = 0
    # Resets the addition counter
    params['count_add'] = 0
    # Calculates and parses the answer
    answer = karatsuba_recursive(x, y, b, params)
    params['answer'] = str(answer)

    return params
