# Temperature Converter
# This program converts temperatures between Celsius and Fahrenheit.

unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ").strip().upper()
temp = float(input("Enter the temperature value: "))

if unit == 'C':
    converted_temp = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {converted_temp:.2f}°F")
elif unit == 'F':
    converted_temp = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {converted_temp:.2f}°C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

