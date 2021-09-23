import unittest
import addsub
import common
import datatypes

class TestAdd(unittest.TestCase):

    def test_add(self):
        x = datatypes.LargeInteger('1337', 10)
        y = datatypes.LargeInteger('1', 10)
        res1 = x + y
        self.assertEqual(str(res1), '1338')

        x = datatypes.LargeInteger('1', 10)
        y = datatypes.LargeInteger('1337', 10)
        res2 = x + y
        self.assertEqual(str(res1),str(res2))

        x = datatypes.LargeInteger('1337', 10)
        y = datatypes.LargeInteger('1338', 10)
        res2 = x + y
        self.assertEqual(str(res2), '2675')

if __name__ == '__main__':
    unittest.main()
