# Weight Calculator
# This program converts weight between kilograms and pounds.

weight = float(input("Enter your weight: "))
unit = input("Enter the unit (kg/lb): ").strip().lower()

if unit == "kg":
    converted = weight * 2.20462
    print(f"Your weight is {converted:.2f} lb.")
elif unit == "lb":
    converted = weight / 2.20462
    print(f"Your weight is {converted:.2f} kg.")
else:
    print("Invalid unit. Please enter 'kg' or 'lb'.")
    exit(1)

