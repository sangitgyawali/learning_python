# Random numbers in Python

import random

low = 1
high = 10
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

random.shuffle(cards)
cards = cards[low - 1:high]

print(cards)