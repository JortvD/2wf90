from unittest import TestCase
from mymodule import datatypes, euclid


class Test(TestCase):
    def test_euclid(self):
        x = datatypes.LargeInteger('26', 10)
        y = datatypes.LargeInteger('5', 10)
        res = euclid.euclid(x, y)
        self.assertEqual(str(res[0]), '1')
        d = x * res[1] + y * res[2]
        self.assertEqual(str(d), '1')

        x = datatypes.LargeInteger('1001', 2)
        y = datatypes.LargeInteger('1001', 2)
        res = euclid.euclid(x, y)
        self.assertEqual(str(res[0]), '1001')
        d = x * res[1] + y * res[2]
        self.assertEqual(str(d), '1001')

        x = datatypes.LargeInteger('23', 16)
        y = datatypes.LargeInteger('28', 16)
        res = euclid.euclid(x, y)
        self.assertEqual(str(res[0]), '5')
        d = x * res[1] + y * res[2]
        self.assertEqual(str(d), '5')

        r = 16
        x = datatypes.LargeInteger('c1b715933d2d1dcb0e23', r)
        y = datatypes.LargeInteger('157f77a46f4c796bb774', r)
        d = datatypes.LargeInteger('1', r)
        a = datatypes.LargeInteger('8bb87443ec917fa3e87', r)
        b = datatypes.LargeInteger('-4eb01402d28cbe3588c1', r)
        res = euclid.euclid(x, y)
        self.assertEqual(str(res[0]), str(d))
        self.assertEqual(str(res[1]), str(a))
        self.assertEqual(str(res[2]), str(b))
