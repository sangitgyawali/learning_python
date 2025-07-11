# Encryption Program in Python

import random
import string

chars = " " + string.whitespace + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

print(f"chars: {chars}")
print(f"key: {key}")


print(chars)