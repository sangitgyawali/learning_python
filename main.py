# Functions in python

def create_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return f"{first_name} {last_name}"

full_name = create_name("john", "doe")
print(full_name)