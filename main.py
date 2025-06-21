# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food to buy (q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of a {food}: "))
        foods.append(food)
        prices.append(price)

print("\nYour shopping cart:")
for food in foods:
    print(f"{food} - ${prices[foods.index(food)]:.2f}")
total = sum(prices)
print(f"\nTotal: ${total:.2f}")
