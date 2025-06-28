# Concession stand program

menu = {
    "hot_dog": 3.50,
    "hamburger": 4.00,
    "fries": 2.50,
    "drink": 1.50
}

cart = []
total = 0

print("------ Menu ------")
for key, value in menu.items():
    print(f"{key:10 }: ${value:.2f}")
print("-------------------")