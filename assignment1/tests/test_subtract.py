import unittest
import subtract
import common

class TestSubtract(unittest.TestCase):

    def test_subtract(self):
        x = common.split('1337', 10)
        y = common.split('1', 10)
        res = subtract.subtract(x, y, 10)
        print(res)

        y = common.split('1338', 10)
        res = subtract.subtract(x, y, 10)
        print(res)

        x = common.split('-1337', 10)
        y = common.split('-1338', 10)
        res = subtract.subtract(x, y, 10)
        print(res)

if __name__ == '__main__':
    unittest.main()
