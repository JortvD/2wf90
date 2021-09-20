from add import add
from subtract import subtract
import common

def karatsubaRecursive(x, y, b, params):
    # If the length of x or y is uneven 
    if(len(x) % 2 == 1): 
        x.insert(0, 0)
    if(len(y) % 2 == 1): 
        y.insert(0, 0)

    n = max(len(x), len(y))

    if(n == 1): 
        params['count_mul'] += 1
        mult = x[0] * y[0]
        
        return [mult//b, mult%b]

    xhi = x[1:len(x)//2]
    xlo = x[len(x)//2:]
    yhi = y[1:len(y)//2]
    ylo = y[len(y)//2:]

    xhiyhi = karatsubaRecursive(xhi, yhi, b, params)
    xloylo = karatsubaRecursive(xlo, ylo, b, params)
    mid = karatsubaRecursive(add(xhi, xlo, params), add(yhi, ylo, params), b, params)
    xymid = subtract(subtract(mid, xhiyhi, params), xloylo, params)

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