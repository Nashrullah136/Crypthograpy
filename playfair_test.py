from unittest.case import TestCase
from playfair import *
import unittest

class Playfair_cipher_test(unittest.TestCase):
    def test_clean_string(self):
        testcase = "Key Kneel   Certain Company        Earwax"
        expect = "keykneelcertaincompanyearwax"
        self.assertEqual(clean_string(testcase), expect)
    
    def test_normalize_bigram(self):
        testcase = "aaassddpp"
        self.assertNotRegex(normalize_bigram(testcase), r"(.)\1")

    def test_make_key(self):
        testcase = "bishopthank"
        expect = "bishoptankcdefglmqruvwxyz"
        self.assertEqual(make_key(testcase), expect)
    
    def test_encrypt(self):
        plaintext = "jangan sampai lepas"
        key = "bishopthank"
        ciphertext = "stkfnkaelttsqctnas"
        self.assertEqual(encrypt(plaintext, key), ciphertext)

    def test_decrypt(self):
        plaintext = "iangansampailepasx"
        key = "bishopthank"
        ciphertext = "stkfnkaelttsqctnas"
        self.assertEqual(decrypt(ciphertext, key), plaintext)

if __name__ == "__main__":
    unittest.main()