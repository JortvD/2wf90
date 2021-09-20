import common

def modAdd(x, y, m, b, params):
    return

def calc(params):
    b = int(params['radix'])
    x = common.split(params['x'], b)
    y = common.split(params['y'], b)
    m = common.split(params['m'], b)

    params['answer'] = common.concat(modAdd(x, y, m, b, params))
    
    return params