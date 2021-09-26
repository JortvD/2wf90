from unittest import TestCase

from mymodule import datatypes, mod_multiply


class Test(TestCase):
    def test_mod_multiply(self):
        x = datatypes.LargeInteger('100', 10)
        y = datatypes.LargeInteger('302', 10)
        m = datatypes.LargeInteger('11', 10)
        res = mod_multiply.mod_multiply(x, y, m)
        self.assertEqual(str(res), '5')

        x = datatypes.LargeInteger('95', 10)
        y = datatypes.LargeInteger('-27', 10)
        m = datatypes.LargeInteger('14', 10)
        res = mod_multiply.mod_multiply(x, y, m)
        self.assertEqual(str(res), '11')

        x = datatypes.LargeInteger('-4', 10)
        y = datatypes.LargeInteger('-71', 10)
        m = datatypes.LargeInteger('12', 10)
        res = mod_multiply.mod_multiply(x, y, m)
        self.assertEqual(str(res), '8')
