# Decryption Program in Python

import random
import string

chars = " " + string.whitespace + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"key: {key}")

cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = chars.input(letter)
    plain_text += key[index]

print(f"Encrypted message: {plain_text}")
print(f"Original message: {cipher_text}")
