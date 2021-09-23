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
        elif isinstance(val, list):
            self._val = val
        else:
            self._val = LargeInteger.from_str(val, radix)
            self.strip_leading_zeroes()

    def __getitem__(self, i):
        # To abstract away the sign bit
        return self._val[i+1]

    def __add__(self, y):
        return addsub.add(self, y)

    def __sub__(self, y):
        return addsub.subtract(self, y)

    def __mul__(self, y):
        return multiply.multiply(self, y)

    def __lshift__(self, y):
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
            x_i = int(self._val[i])
            if not found_digits:
                found_digits = (x_i != 0)

            if found_digits:
                s += LOOKUP_TABLE[x_i]

        if not found_digits:
            s = '0'

        return s

    def __lt__(self, y):
        if self.is_negative and not y.is_negative:
            return True

        # This optimization does not work, since we have leading zeroes
        # if self.num_digits != y.num_digits:
        #     return self.num_digits < y.num_digits
        x_start = 0
        for i in range(1, len(self._val) - 1):
            if self._val[i] != 0:
                break
            x_start += 1
        y_start = 0
        for i in range(0, y.num_digits - 1):
            if y[i] != 0:
                break
            y_start += 1
        
        x_left = self.num_digits - x_start
        y_left = y.num_digits - y_start
        if x_left != y_left:
             return x_left < y_left

        for i in range(0, x_left):
            if self._val[x_start + i +1] != y[y_start + i]:
                return self._val[x_start + i +1] < y[y_start + i]
        return False

    def __len__(self):
        return self.num_digits

    def make_negative(self):
        self._val[0] = 1

    def make_positive(self):
        self._val[0] = 0

    def invert_digits(self):
        self._val = [self._val[0]] + self._val[1:][::-1]

    def prepend_zeroes(self, amount):
        self._val = [self._val[0]] + [0 for i in range(amount)] + self._val[1:]

    def strip_leading_zeroes(self):
        strip_amount = 0
        # Always maintain one digit for the zero itself
        for i in range(1, len(self._val) - 1):
            if self._val[i] != 0:
                break
            strip_amount += 1

        self._val = [self._val[0]] + self._val[1+ strip_amount:]

    def flip_sign(self):
        self._val[0] ^= 1

    def slice(self, i, j):
        return self._val[i+1:j+1]

    def lshift(self, y):
        self._val.extend([0] * y)
        return self

    def append(self, digit):
        """
        @summary Appends a digits to the integer
        """
        self._val.append(digit)

    def insert(self, i, v):
        self._val.insert(i + 1, v)

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
