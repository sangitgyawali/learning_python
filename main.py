# Number Guessing Game in python

import random

lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number, highest_number)
guess = 0
is_running = True

print("Welcome to the Number Guessing Game!")
print(f"Guess a number between {lowest_number} and {highest_number}.")

while is_running:
    guess = input("Make a guess: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    if guess < lowest_number or guess > highest_number:
        print(f"Your guess must be between {lowest_number} and {highest_number}.")
        continue

    if guess < answer:
        print("Too low! Try again.")
    elif guess > answer:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        is_running = False

print("Thanks for playing!")