# File Writing in Python

employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

file_path = "output.txt"

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")