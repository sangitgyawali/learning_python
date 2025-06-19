#Logical Operators

temp = 30
is_sunny = True

if temp > 25 and is_sunny:
    print("It's a warm and sunny day!")
elif temp > 25 and not is_sunny:
    print("It's warm but not sunny.")
elif temp <= 25 and is_sunny:
    print("It's cool but sunny.")
else:
    print("It's a cool and cloudy day.")