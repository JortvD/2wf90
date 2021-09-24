import unittest
from mymodule import datatypes

class TestSubtract(unittest.TestCase):

    def test_subtract(self):
        x = datatypes.LargeInteger('1337', 10)
        y = datatypes.LargeInteger('1', 10)
        res = x - y
        self.assertEqual(str(res), '1336')

        x = datatypes.LargeInteger('1337', 10)
        y = datatypes.LargeInteger('1338', 10)
        res = x - y
        self.assertEqual(str(res), '-1')

        x = datatypes.LargeInteger('-1337', 10)
        y = datatypes.LargeInteger('1338', 10)
        res = x - y
        self.assertEqual(str(res), '-2675')

        x = datatypes.LargeInteger('-1337', 10)
        y = datatypes.LargeInteger('-1338', 10)
        res = x - y
        self.assertEqual(str(res), '1')

        x = datatypes.LargeInteger('1', 10)
        y = datatypes.LargeInteger('-3', 10)
        res = x - y
        self.assertEqual(str(res), '4')

        x = datatypes.LargeInteger('11', 10)
        # Test leading zeroes
        y = datatypes.LargeInteger('06', 10)
        y.prepend_zeroes(1)
        res = x - y
        self.assertEqual(str(res), '5')

        x = datatypes.LargeInteger('6', 10)
        y = datatypes.LargeInteger('5', 10)
        res = x - y
        self.assertEqual(str(res), '1')

if __name__ == '__main__':
    unittest.main()
