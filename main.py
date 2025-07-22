# File Reading in Python

file_path = "input.txt"

with open (file_path, "r") as file:
    content = file.read()
    print(content)
    