from add import add
from subtract import subtract
import common

def karatsubaRecursive(x, y, b, params):
    # If either x or y are 0 then return 0.
    if(len(x) == 0 | len(y) == 0): return [0]

    # If x and y are 1 then
    if(len(x) == 1 & len(y) == 1):
        # Add 1 to the multiplication counter
        params['count_mul'] += 1
        # Multiply x[0] and y[0]
        mult = x[0] * y[0]
        
        # Return an array of the two digits of the multiplication, both mod b
        return [mult//b, mult%b]
    
    # If the length of x is uneven 
    if(len(x) % 2 == 1): 
        # then add a 0 at the beginning of x
        x.insert(0, 0)
    if(len(y) % 2 == 1): 
        # then add a 0 at the beginning of y
        y.insert(0, 0)

    # Here we take that n is the largest length of either x and y
    n = max(len(x), len(y))

    # The high part of x
    xhi = x[0:(len(x)-1)//2]
    # The low part of x
    xlo = x[(len(x)-1)//2:]
    # The high part of y
    yhi = y[0:(len(y)-1)//2]
    # The low part of y
    ylo = y[(len(y)-1)//2:]

    # The high part of the karatsuba multiplication
    xhiyhi = karatsubaRecursive(xhi, yhi, b, params)
    # The low part of the karatsuba multiplcation
    xloylo = karatsubaRecursive(xlo, ylo, b, params)
    # The mid part of the mid part of the karatsuba multiplication
    mid = karatsubaRecursive(add(xhi, xlo, params), add(yhi, ylo, params), b, params)
    # The full mid part of the karatsuba multiplication
    xymid = subtract(subtract(mid, xhiyhi, params), xloylo, params)

    # The summation part of the karatsuba algorithm
    xy = add(add(common.radixShift(xhiyhi, n), common.radixShift(xymid, n/2)), xloylo)

    return xy

# The karatsuba function that is called from the script. It starts the recursive function.
def calc(params):
    # Parses the base b from the params
    b = int(params['radix'])
    # Parses the x value from the params
    x = common.split(params['x'], b)
    # Parses the y value from the params
    y = common.split(params['y'], b)

    # Resets the multiplication counter
    params['count_mul'] = 0
    # Resets the addition counter
    params['count_add'] = 0
    # Calculates and parses the answer
    params['answer'] = common.concat(karatsubaRecursive(x, y, b, params))

    return params