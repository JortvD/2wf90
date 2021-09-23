import unittest
import datatypes

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

if __name__ == '__main__':
    unittest.main()
