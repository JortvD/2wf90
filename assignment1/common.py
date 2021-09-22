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

def num_digits(x):
    return len(x) -  1

# Shifts the array arr by adding n zeros at the end of the arr.
def radixShift(arr, n):
    for n in range(n):
        arr.append(0)

    return arr

def is_negative(x):
    return x[0] == 1

def smaller(x, y):
    if is_negative(x) and not is_negative(y):
        return True

    if len(x) != len(y):
        return len(x) < len(y)

    for i in range(len(x)):
        if x[i] < y[i]:
            return True
    return False

def makeNegative(arr):
    arr[0] = 1
    return arr
