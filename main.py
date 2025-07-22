# File Reading in Python

file_path = "input.txt"

try:  
    with open (file_path, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have permission to read that file")
    