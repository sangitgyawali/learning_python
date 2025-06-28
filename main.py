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
    print(f"{key:10}: ${value:.2f}")

print("-------------------")

while True:
    food = input("Enter food item to add to cart (or 'done' to finish): ").strip().lower()
    if food == 'done':
        break
    elif food in menu:
        cart.append(food)
        total += menu[food]
        print(f"Added {food} to cart. Current total: ${total:.2f}")
    else:
        print("Item not found in menu. Please try again.")

print("\n------ Cart ------")
for item in cart:
    print(f"{item:10 }: ${menu[item]:.2f}")
print("-------------------")
print(f"Total amount due: ${total:.2f}")    

