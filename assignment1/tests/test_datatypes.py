import unittest
import datatypes

class TestSubtract(unittest.TestCase):

    def test_lessthan(self):
        x = datatypes.LargeInteger('11', 10)
        # Test leading zeroes
        y = datatypes.LargeInteger('06', 10)
        self.assertFalse(x < y)

        # Test leading zeroes
        x = datatypes.LargeInteger('06', 10)
        y = datatypes.LargeInteger('11', 10)
        self.assertTrue(x < y)

if __name__ == '__main__':
    unittest.main()
