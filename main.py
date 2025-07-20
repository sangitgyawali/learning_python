# File Detection in Python

import os

file_path = "test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif ps.path.isdir(file_path):
        print("This is a directory")
else:
    print("That location doesn't exist")