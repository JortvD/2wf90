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
