# Hangman Game in Python
import random

words = ("apple", "orange", "banana", "coconut", "pineapple")

hangman_art = {
    0: ("  ", "  ", "  "),
    1: (" o ", "  ", "  "),
    2: (" o ", " | ", "  "),
    3: (" o ", "/| ", "  "),
    4: (" o ", "/|\\", "  "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\")
}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print("Word: " + " ".join(hint))

def display_answer(answer):
    print("The word was: " + answer)

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    max_wrong = 6
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for idx, letter in enumerate(answer):
                if letter == guess:
                    hint[idx] = guess
            if "_" not in hint:
                print("\nCongratulations! You guessed the word!")
                display_hint(hint)
                is_running = False
        else:
            wrong_guesses += 1
            print("Wrong guess!")
            if wrong_guesses == max_wrong:
                display_man(wrong_guesses)
                print("\nGame Over!")
                display_answer(answer)
                is_running = False

if __name__ == "__main__":
    main()
