import unittest
from mymodule import datatypes
from mymodule import multiply

class TestMultiply(unittest.TestCase):

    def test_subtract(self):
        x = datatypes.LargeInteger('23', 10)
        y = datatypes.LargeInteger('17', 10)
        res = x * y
        self.assertEqual(str(res), '391')
        self.assertEqual(len(res), 3)

        x = datatypes.LargeInteger('17', 10)
        y = datatypes.LargeInteger('23', 10)
        res = x * y
        self.assertEqual(str(res), '391')
        self.assertEqual(len(res), 3)

        x = datatypes.LargeInteger('-23', 10)
        y = datatypes.LargeInteger('17', 10)
        res = x * y
        self.assertEqual(str(res), '-391')
        self.assertEqual(len(res), 3)

        x = datatypes.LargeInteger('-23', 10)
        y = datatypes.LargeInteger('-17', 10)
        res = x * y
        self.assertEqual(str(res), '391')
        self.assertEqual(len(res), 3)

        x = datatypes.LargeInteger('0', 10)
        y = datatypes.LargeInteger('0', 10)
        res = x * y
        self.assertEqual(str(res), '0')
        self.assertEqual(len(res), 1)

        x = datatypes.LargeInteger('11', 10)
        # Test leading zeroes
        y = datatypes.LargeInteger('06', 10)
        y.prepend_zeroes(1)
        res = x * y
        self.assertEqual(str(res), '66')
        self.assertEqual(len(res), 2)

if __name__ == '__main__':
    unittest.main()
