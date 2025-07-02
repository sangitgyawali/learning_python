# Args and kwargs in Python
# Kwargs

def shipping_label(*args , **kwargs):
    for arg in args:
        print(arg, end = " ")
        print()
        for key, value in kwargs.items():
            print(f"{key}: {value}")


shipping_label(
    "1234 Elm St",
    city="Anytown",
    state="CA",
    zip="12345"
)
