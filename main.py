# File Writing in Python

employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

file_path = "output.txt"


try:
    with open(file_path, "w") as file:
        for employee in employees:


except FileExistsError:
    print("That file already exists!")