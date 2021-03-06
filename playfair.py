from util import *
from string import ascii_lowercase
import re

def clean_string(text):
    """Delete space character and lower all letter"""
    text = re.sub(r"[\s]+", "", text)
    text = text.lower()
    return text

def normalize_bigram(text):
    """
    Insert 'x' in the middle bigram that consist of one letter.
    example: aa -> axa
    """
    text = re.sub(r"(.)(?=\1)", r"\1x", text)
    return text

def normalize_text(text):
    """Add 'x' the end of text if length of text is odd"""
    return text if len(text)%2 == 0 else text+"x"

def make_key(key):
    key = clean_string(key)
    key = key + ascii_lowercase
    find_j =  re.compile("j")
    key = find_j.sub("", key)
    alphabet = find_j.sub("", ascii_lowercase)
    index = 0
    new_key = ""
    while alphabet != "":
        new_char = key[index]
        if new_char in alphabet:
            new_key += new_char
            alphabet = re.sub(new_char, "", alphabet)
        index += 1
    return new_key

def generate_matrix_key(key):
    key = make_key(key)
    matrix = [key[i:i+5] for i in range(0, 25, 5)]
    return matrix

def generate_alphabet_dict(matrix_key):
    dict = {}
    for i in range(len(matrix_key)):
        for j in range(len(matrix_key[0])):
            char = matrix_key[i][j]
            dict[char] = [i, j]
    return dict

def split_to_bigram(text):
    return [text[2*i: 2*i+2] for i in range(len(text)//2)]    

def coordinate_encrypt_bigram(bigram, alphabet_coor):
    char1 = alphabet_coor[bigram[0]]
    char2 = alphabet_coor[bigram[1]]
    if char1[0] == char2[0]:
        new_char1 = [char1[0], char1[1]+1]
        new_char2 = [char2[0], char2[1]+1]
    elif char1[1] == char2[1]:
        new_char1 = [char1[0]+1, char1[1]]
        new_char2 = [char2[0]+1, char2[1]]
    else:
        new_char1 = [char1[0], char2[1]]
        new_char2 = [char2[0], char1[1]]

    new_char1 = [i%5 for i in new_char1]
    new_char2 = [i%5 for i in new_char2]   
    return new_char1, new_char2

def coordinate_decrypt_bigram(bigram, alphabet_coor):
    char1 = alphabet_coor[bigram[0]]
    char2 = alphabet_coor[bigram[1]]
    if char1[0] == char2[0]:
        new_char1 = [char1[0], char1[1]-1]
        new_char2 = [char2[0], char2[1]-1]
    elif char1[1] == char2[1]:
        new_char1 = [char1[0]-1, char1[1]]
        new_char2 = [char2[0]-1, char2[1]]
    else:
        new_char1 = [char1[0], char2[1]]
        new_char2 = [char2[0], char1[1]]

    new_char1 = [i%5 for i in new_char1]
    new_char2 = [i%5 for i in new_char2]   
    return new_char1, new_char2

def encrypt(plaintext, key):
    if not check_input(plaintext):
        sys.exit("Massage must be only consist: alphabet and space character")

    matrix_key = generate_matrix_key(key)
    dict = generate_alphabet_dict(matrix_key)
    plaintext = clean_string(plaintext)
    plaintext = normalize_bigram(plaintext)
    plaintext = normalize_text(plaintext)
    plaintext = re.sub("j", "i", plaintext)
    ciphertext = ""
    for i in split_to_bigram(plaintext):
        index1, index2 = coordinate_encrypt_bigram(i, dict)
        ciphertext += matrix_key[index1[0]][index1[1]]
        ciphertext += matrix_key[index2[0]][index2[1]]
    return ciphertext

def decrypt(ciphertext, key):
    if not check_input(ciphertext) and "j" not in ciphertext:
        sys.exit("Ciphertext must only consist: alphabet, except j, and space character")

    matrix_key = generate_matrix_key(key)
    dict = generate_alphabet_dict(matrix_key)
    ciphertext = clean_string(ciphertext)
    plaintext = ""
    for i in split_to_bigram(ciphertext):
        index1, index2 = coordinate_decrypt_bigram(i, dict)
        plaintext += matrix_key[index1[0]][index1[1]]
        plaintext += matrix_key[index2[0]][index2[1]]
    return plaintext

def main():
    type = input("[e,d]?")
    if type == "d":
        dir = input("Directory file to decrypt: ")
        ciphertext = read_file(dir)
        key = input("key: ")
        plaintext = decrypt(ciphertext, key)
        print(plaintext)
    elif type == "e":
        plaintext = input("plainteks: ")
        key = input("key: ")
        ciphertext = encrypt(plaintext, key)
        to_file("caeshar_cipher_result.txt", ciphertext)
    else:
        print("Input doesn't match")

if __name__ == "__main__":
    main()

    











