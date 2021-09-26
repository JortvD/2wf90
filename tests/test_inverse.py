import unittest
from mymodule import datatypes
from mymodule.inverse import inverse

class TestInverse(unittest.TestCase):

    def test_inverse(self):
        a = datatypes.LargeInteger('11', 10)
        m = datatypes.LargeInteger('5', 10)
        res = inverse(a, m)
        self.assertEqual(str(res), '1')

        a = datatypes.LargeInteger('3', 10)
        m = datatypes.LargeInteger('5', 10)
        res = inverse(a, m)
        self.assertEqual(str(res), '2')

        a = datatypes.LargeInteger('14234', 10)
        m = datatypes.LargeInteger('13431', 10)
        res = inverse(a, m)
        self.assertEqual(str(res), 'inverse does not exist')

if __name__ == '__main__':
    unittest.main()
