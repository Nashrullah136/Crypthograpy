import util
import re
import sys

def fpb(a, b):
    while a%b != 0:
        a, b = b, a%b
    return b

def m_invers(key_m):
    i = 1
    while (key_m*i)%26 != 1:
        i += 1
    return i

def clean_string(text):
    return text.lower()

def is_space(char):
    result = re.search(r"[\s]", char)
    return result != None

def encrypt_char(char, m, b):
    indeks = ord(char)-97
    enc_indeks = (indeks*m + b) % 26
    return chr(enc_indeks+97)

def decrypt_char(char, m, b):
    indeks = ord(char)-97
    m_inv = m_invers(m)
    enc_indeks = (m_inv * (indeks - b)) % 26
    return chr(enc_indeks+97)

def encrypt(plaintext, m, b):
    if not util.check_input(plaintext):
        sys.exit("Plaintext must only consist alphabet and space character ")

    plaintext = clean_string(plaintext)
    ciphertext = ""
    for i in plaintext:
        if not is_space(i):
            ciphertext += encrypt_char(i, m, b)
        else:
            ciphertext += i
    return ciphertext

def decrypt(ciphertext, m, b):
    if not util.check_input(ciphertext):
        sys.exit("Plaintext must only consist alphabet and space character ")
    
    ciphertext = clean_string(ciphertext)
    plaintext = ""
    for i in ciphertext:
        if not is_space(i):
            plaintext += decrypt_char(i, m, b)
        else:
            plaintext += i
    return plaintext

def main():
    type = input("[e,d]?")
    if type == "d":
        dir = input("Directory file to decrypt: ")
        ciphertext = util.read_file(dir)
        m = input("key m: ")
        b = input("key b: ")
        plaintext = decrypt(ciphertext, m, b)
        print(plaintext)
    elif type == "e":
        plaintext = input("plainteks: ")
        m = input("key m: ")
        b = input("key b: ")
        ciphertext = encrypt(plaintext, m, b)
        util.to_file("caeshar_cipher_result.txt", ciphertext)
    else:
        print("Input doesn't match")

if __name__ == "__main__":
    main()