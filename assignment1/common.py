# Splits the string str into a list of integers with base b.
def split(i_str, b):
    if b > 16:
        raise ValueError('Base > 16 not supported')
    is_negative = i_str.lstrip()[0] == '-'
    allowed_chars = '0123456789'
    allowed_chars += 'abcdef'[:max(b - 10,0)]
    digits = [int(c,b) for c in i_str if c in allowed_chars]
    return [1 if is_negative else 0] + digits

# Maps the integer n to a string that goes until the hexadecimals.
def baseToString(n):
    return ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'][n]

# Concatinates the array arr of integers into a string using the baseToString function.
def concat(arr):
    return ''.join([baseToString(i) for i in arr])

def num_bits(x):
    return len(x) -  1

# Shifts the array arr by adding n zeros at the end of the arr.
def radixShift(arr, n):
    for n in range(n):
        arr.append(0)

    return arr

def smaller(x, y):
    n = max(len(x), len(y))

    for i in range(n):
        if(i + len(x) < n):
            if(y[i] > 0): return True
            else: pass
        else:
            if(x[i] == y[i]): pass
            else: return x[i] < y[i]

    return False
