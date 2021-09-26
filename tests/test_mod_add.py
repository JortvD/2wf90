import unittest
import sys
from mymodule import mod_add, datatypes


def test(test, x, y, m, b, ans):
    params = {"x": x, "y": y, "m": m,"radix": b}
    res = mod_add.calc(params)
    test.assertEqual(res['answer'], ans)

class TestModAdd(unittest.TestCase):

    def test_mod_add(self):
        test(self, '123', '22', '133', 10, '12')
        test(self, '-123', '22', '133', 10, '32')
        test(self, '-103', '-33', '13', 10, '7')

if __name__ == '__main__':
    unittest.main()
