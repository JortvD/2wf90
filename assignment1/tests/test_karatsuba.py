import unittest
import sys
sys.path.append("..")
import karatsuba

def test(test, x, y, b, ans):
    params = {"x": x, "y": y, "radix": b}
    res = karatsuba.calc(params)
    test.assertEqual(res['answer'], ans)

class TestKaratsuba(unittest.TestCase):

    def test_karatsuba(self):
        test(self, '82a4d3f8bfab54bb3011', 'cb95aa820d14888e48c3', 16, '67e5150972e817d639ac0f8795213f07e18864f3')
        test(self, '1010100001110101001010001100101110111101101110000101011100111000000000010111010010110000001101011100', '1001100111111111001111101100000011100001111100100001001001011000101111111010011111010011010101000110', 2, '1100101010101011111101101100000101100111100001101011011001011101000111010100011101110100001111110001110111001101101001100110001110010110011001111000100110110011011010101100010001000001111011100101000')
        test(self, '2020111212202021100001212221022010021001', '1202222101212012211022202222112120020101', 3, '10222112100001022222012101100012020101212101011201011110022221012121011022211101')
        test(self, '255250226011363161263502222556', '153556502550413362430240350510', 7, '50303335051551042446540232630332141424231165632644465060060')
        test(self, '-123234234', '567575467567', 10, '-69944727982811088678')

if __name__ == '__main__':
    unittest.main()
