# File Detection in Python

import os

file_path = "test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

else:
    print("That location doesn't exist")