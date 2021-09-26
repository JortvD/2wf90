from unittest import TestCase

from mymodule import datatypes, mod_subtract


class Test(TestCase):
    def test_mod_subtract(self):
        x = datatypes.LargeInteger('100', 10)
        y = datatypes.LargeInteger('302', 10)
        m = datatypes.LargeInteger('13', 10)
        res = mod_subtract.mod_subtract(x, y, m)
        self.assertEqual(str(res), '6')

        x = datatypes.LargeInteger('95', 10)
        y = datatypes.LargeInteger('-27', 10)
        m = datatypes.LargeInteger('11', 10)
        res = mod_subtract.mod_subtract(x, y, m)
        self.assertEqual(str(res), '1')

        x = datatypes.LargeInteger('-4', 10)
        y = datatypes.LargeInteger('-52', 10)
        m = datatypes.LargeInteger('7', 10)
        res = mod_subtract.mod_subtract(x, y, m)
        self.assertEqual(str(res), '6')
