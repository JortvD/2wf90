from add import add
from subtract import subtract

def radixShift(arr, places):
    for n in range(places):
        arr.append(0)

    return arr

def karatsubaRecursive(x, y, b):
    if(len(x) % 2 == 1): 
        x.insert(0, 0)
    if(len(y) % 2 == 1): 
        y.insert(0, 0)

    n = min(len(x), len(y))

    if(n == 1): return [x[0] * y[0]]

    xhi = x[1:len(x)//2]
    xlo = x[len(x)//2:]
    yhi = y[1:len(y)//2]
    ylo = y[len(y)//2:]

    xhiyhi = karatsubaRecursive(xhi, yhi, b)
    xloylo = karatsubaRecursive(xlo, ylo, b)
    xymid = subtract(subtract(karatsubaRecursive(add(xhi, xlo), add(yhi, ylo), b), xhiyhi), xloylo)

    xy = add(add(radixShift(xhiyhi, n), radixShift(xymid, n/2)), xloylo)

    return xy

def karatsuba(params):
    
    pass