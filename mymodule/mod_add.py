from mymodule.datatypes import LargeInteger
from mymodule.reduce import reduce

def mod_add(x, y, m, b, params):
    x = reduce(x, m)
    y = reduce(y, m)
    z = x + y

    if(z < m):
        return z
    else:
        return z - m

def calc(params):
    b = int(params['radix'])
    x = LargeInteger(params['x'], b)
    y = LargeInteger(params['y'], b)
    m = LargeInteger(params['m'], b)

    params['answer'] = str(mod_add(x, y, m, b, params))
    
    return params
