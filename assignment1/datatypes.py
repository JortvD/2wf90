import addsub
import multiply

class LargeInteger(object):

    def __init__(self, val, radix=10):
        """
        @param val a large string containing the integer
        @param radix The radix (default 10)
        """
        self.radix = radix

        if val is None:
            self._val = [0]
        else:
            self._val = LargeInteger.from_str(val, radix)

    def __getitem__(self, i):
        # To abstract away the sign bit
        return self._val[i+1]

    def __add__(self, y):
        return addsub.add(self, y)

    def __sub__(self, y):
        return addsub.subtract(self, y)

    def __mul__(self, y):
        return multiply.multiply(self, y)

    def __lshift(self, y):
        self._val.extend([0 * y])
        return self

    def __str__(self):
        LOOKUP_TABLE = '0123456789abcdef'
        # TODO
        s = ''
        if self._val[0] == 1:
            s+='-'

        found_digits = False
        for i in range(1, len(self._val)):
            x_i = self._val[i]
            if not found_digits:
                found_digits = (x_i != 0)
            if found_digits:
                s += LOOKUP_TABLE[x_i]
        return s

    def __lt__(self, y):
        if self.is_negative and not y.is_negative:
            return True

        if self.num_digits != y.num_digits:
            return self.num_digits < y.num_digits

        for i in range(0, self.num_digits):
            if self._val[i+1] < y[i]:
                return True
        return False

    def make_negative(self):
        self._val[0] = 1

    def make_positive(self):
        self._val[0] = 0

    def invert_digits(self):
        self._val = [self._val[0]] + self._val[1:][::-1]

    def prepend_zeroes(self, amount):
        self._val = [self._val[0]] + [0 for i in range(amount)] + self._val[1:]

    def flip_sign(self):
        self._val[0] ^= 1

    def append(self, digit):
        """
        @summary Appends a digits to the integer
        """
        self._val.append(digit)

    @property
    def num_digits(self):
        return len(self._val) -  1

    @property
    def is_negative(self):
        return self._val[0] == 1

    @property
    def is_positive(self):
        return self._val[0] == 0

    @staticmethod
    def from_str(s, radix):
        if radix > 16:
            raise ValueError('Base > 16 not supported')
        is_negative = s.lstrip()[0] == '-'
        allowed_chars = '0123456789'
        allowed_chars += 'abcdef'[:max(radix - 10,0)]
        digits = [int(c,radix) for c in s if c in allowed_chars]
        return [1 if is_negative else 0] + digits
