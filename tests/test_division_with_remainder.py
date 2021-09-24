from unittest import TestCase

from mymodule import datatypes


class Test(TestCase):
    def test_div_with_r(self):
        x = datatypes.LargeInteger('-26', 10)
        y = datatypes.LargeInteger('-5', 10)
        res = x / y
        self.assertEqual(str(res[0]), '5')
        self.assertEqual(str(res[1]), '1')

        x = datatypes.LargeInteger('-76', 10)
        y = datatypes.LargeInteger('5', 10)
        res = x / y
        self.assertEqual(str(res[0]), '15')
        self.assertEqual(str(res[1]), '-1')

        x = datatypes.LargeInteger('1010', 2)
        y = datatypes.LargeInteger('1010', 2)
        res = x / y
        self.assertEqual(str(res[0]), '1')
        self.assertEqual(str(res[1]), '0')

        x = datatypes.LargeInteger('100110', 2)
        y = datatypes.LargeInteger('1110', 2)
        res = x / y
        self.assertEqual(str(res[0]), '10')
        self.assertEqual(str(res[1]), '1010')
