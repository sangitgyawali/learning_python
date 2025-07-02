# Args and kwargs in Python
# Kwargs

def print_address(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(
    street="123 Main St",
    city="Anytown",
    state="CA",
    zip="12345"
)

