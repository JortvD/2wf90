# it is assumed that a and b are positive integers
# returns a list [d, x, y] such that d = gcd(a, b) = x * a + y * b
from mymodule import datatypes


def euclid(a, b):
    x_1 = datatypes.LargeInteger('1', a.get_radix())
    x_2 = datatypes.LargeInteger('0', a.get_radix())
    y_1 = datatypes.LargeInteger('0', a.get_radix())
    y_2 = datatypes.LargeInteger('1', a.get_radix())

    while b > datatypes.LargeInteger('0', a.get_radix()):
        q = a // b
        r = a - q * b

        a = b
        b = r

        x_3 = x_1 - q * x_2
        y_3 = y_1 - q * y_2

        x_1 = x_2
        y_1 = y_2

        x_2 = x_3
        y_2 = y_3

    d = a

    return [d, x_1, y_1]
