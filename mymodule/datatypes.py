from mymodule import addsub, multiply, reduce, division_with_remainder


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
        return self._val[i + 1]

    def __setitem__(self, i, value):
        # To abstract away the sign bit
        self._val[i + 1] = value
        return self._val

    def __add__(self, y):
        return addsub.add(self, y)

    def __sub__(self, y):
        return addsub.subtract(self, y)

    def __mul__(self, y):
        return multiply.multiply(self, y)

    def __truediv__(self, y):
        return division_with_remainder.div_with_r(self, y)

    def __mod__(self, m):
        return reduce.reduce(self, m)

    def __floordiv__(self, y):
        return division_with_remainder.div_with_r(self, y)[0]

    def __lshift__(self, y):
        self._val.extend([0 * y])
        return self

    def __str__(self):
        LOOKUP_TABLE = '0123456789abcdef'
        # TODO
        s = ''
        if self._val[0] == 1:
            s += '-'

        found_digits = False
        for i in range(1, len(self._val)):
            x_i = self._val[i]
            if not found_digits:
                found_digits = (x_i != 0)

            if found_digits:
                s += LOOKUP_TABLE[x_i]

        if not found_digits:
            s = '0'

        return s

    def __len__(self):
        return self.num_digits

    def get_digit(self, i):
        return self.__getitem__(i)

    def __gt__(self, y):
        if self.is_negative and not y.is_negative:
            return False
        elif y.is_negative and not self.is_negative:
            return True
        elif self.__len__() > len(y):
            return self.is_positive
        elif self.__len__() < len(y):
            return self.is_negative

        for i in range(0, self.__len__()):
            if self.__getitem__(i) > y.get_digit(i):
                return self.is_positive
            elif self.__getitem__(i) < y.get_digit(i):
                return self.is_negative

        return False

    def __lt__(self, y):
        return not self.__ge__(y)

    def __eq__(self, y):
        if self.is_negative and not y.is_negative:
            return False
        elif y.is_negative and not self.is_negative:
            return False
        elif self.__len__() != len(y):
            return False

        for i in range(0, self.__len__()):
            if self.__getitem__(i) != y.get_digit(i):
                return False
        return True

    def __ge__(self, y):
        return self.__gt__(y) or self.__eq__(y)

    def __le__(self, y):
        return not self.__gt__(y)

    def get_radix(self):
        return self.radix

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

        self._val = [self._val[0]] + self._val[1 + strip_amount:]

    def flip_sign(self):
        self._val[0] ^= 1

    def slice(self, i, j):
        return self._val[i + 1:j + 1]

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
        return len(self._val) - 1

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
        allowed_chars += 'abcdef'[:max(radix - 10, 0)]
        digits = [int(c, radix) for c in s if c in allowed_chars]
        return [1 if is_negative else 0] + digits
