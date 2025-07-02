# Args and kwargs in Python

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Alice", "Bob", "Charlie")
