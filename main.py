# Fibonacci Series Generator using Python

n = int(input("Enter how many terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
