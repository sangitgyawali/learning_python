# Dice rollar program in Python

import random

def roll_dice():
    print("Welcome to the Dice Roller!")
    while True:
        try:
            sides = int(input("Enter the number of sides on the dice (6, 10, 20, etc.): "))
            if sides < 1:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    roll = random.randint(1, sides)
    print(f"You rolled a {roll} on a {sides}-sided dice.")

if __name__ == "__main__":
    roll_dice()

