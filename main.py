# List comprehension in Python

fruits = ['apple', 'banana', 'cherry', 'date']
fruits = [fruit.upper() for fruit in fruits if 'a' in fruit]
print(fruits)