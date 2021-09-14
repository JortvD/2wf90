# Splits the string str into a list of integers with base b.
def split(str, b):
    return [int(i, b) for i in list(str)]

# Maps the integer n to a string that goes until the hexadecimals.
def baseToString(n):
    return ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'][n]

# Concatinates the array arr of integers into a string using the baseToString function.
def concat(arr):
    return ''.join([baseToString(i) for i in arr])

# Shifts the array arr by adding n zeros at the end of the arr.
def radixShift(arr, n):
    for n in range(n):
        arr.append(0)

    return arr