import common
from add_sub import add, subtract
# from subtract import subtract

def modAdd(x, y, m, b, params):
    z = add(x, y)

    if(common.smaller(z, m)):
        return z
    else:
        return subtract(z, m)

def calc(params):
    b = int(params['radix'])
    x = common.split(params['x'], b)
    y = common.split(params['y'], b)
    m = common.split(params['m'], b)

    params['answer'] = common.concat(modAdd(x, y, m, b, params))
    
    return params