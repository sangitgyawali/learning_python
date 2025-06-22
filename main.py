# Rock Paper Scissors Game

import random

choices = ['rock', 'paper', 'scissors']
computer = random.choice(choices)
user = input("Enter rock, paper, or scissors: ").lower()

if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print(f"You win! Computer chose {computer}")
else:
    print(f"You lose! Computer chose {computer}")
