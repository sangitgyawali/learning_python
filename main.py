# Hangman Game in Python
import random

words = ("apple", "orange", "banana", "coconut", "pineapple")

#dictionary of key:()
hangman_art = {
    0: ("  ", "  ", "  "),
    1: (" o ", "  ", "  "),
    2: (" o ", " | ", "  "),
    3: (" o ", "/| ", "  "),
    4: (" o ", "/|\\", "  "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\")
}

for line in hangman_art[4]:
    print(line)
