from steno import *
import unittest

class Playfair_cipher_test(unittest.TestCase):
    def test_TextToBin(self):
        text = "hii"
        bin_text = "011010000110100101101001"
        self.assertEqual(TextToBin(text), bin_text)
    
    def test_BinToText(self):
        text = "hii"
        bin_text = "011010000110100101101001"
        self.assertEqual(BinToText(bin_text), text)

    def test_Encode(self):
        fp = "condition.jpg"
        text = "message"
        img = Encode(fp, text)
        img.show()

    def test_Decode(self):
        fp = "result.png"
        text = "message"
        self.assertEqual(Decode(fp), text)

if __name__ == "__main__":
    unittest.main()