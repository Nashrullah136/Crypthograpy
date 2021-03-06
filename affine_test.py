from affine import *
from unittest.case import TestCase
import unittest

class Affine_cipher_test(unittest.TestCase):
    def test_fpb(self):
        a = 70
        b = 120
        c = 10
        self.assertEqual(fpb(a, b), c)

    def test_m_invers(self):
        a = 11
        b = m_invers(a)
        self.assertEqual((a*b)%26, 1)
    
    def test_is_space(self):
        testcase = "a"
        expect = False
        self.assertEqual(is_space(testcase), expect)

    def test_is_space1(self):
        testcase = " "
        expect = True
        self.assertEqual(is_space(testcase), expect)

    def test_clean_string(self):
        testcase = "AasdasdA"
        expect = "aasdasda"
        self.assertEqual(clean_string(testcase), expect)
        
    def test_encrypt(self):
        plaintext = "jangan sampai lepas"
        m = 11
        b = 5
        ciphertext = "afstfs vfhofp wxofv"
        self.assertEqual(encrypt(plaintext, m, b), ciphertext)

    def test_decrypt(self):
        plaintext = "jangan sampai lepas"
        m = 11
        b = 5
        ciphertext = "afstfs vfhofp wxofv"
        self.assertEqual(decrypt(ciphertext, m, b), plaintext)

if __name__ == "__main__":
    unittest.main()