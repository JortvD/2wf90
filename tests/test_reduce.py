from unittest import TestCase
from mymodule import datatypes


class Test(TestCase):
    def test_reduce(self):
        x = datatypes.LargeInteger('26', 10)
        y = datatypes.LargeInteger('5', 10)
        res = x % y
        self.assertEqual(str(res), '1')

        x = datatypes.LargeInteger('-76', 10)
        y = datatypes.LargeInteger('5', 10)
        res = x % y
        self.assertEqual(str(res), '-1')

        x = datatypes.LargeInteger('1010', 2)
        y = datatypes.LargeInteger('1010', 2)
        res = x % y
        self.assertEqual(str(res), '0')

        x = datatypes.LargeInteger('100110', 2)
        y = datatypes.LargeInteger('1110', 2)
        res = x % y
        self.assertEqual(str(res), '1010')
