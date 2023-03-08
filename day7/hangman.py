''''
Hangman game.
You have to guess the hidden word in 7 tries or you get hanged!
You can see how many characters are in the hidden word.
And you can guess which letters are in the word. But if you guess
wrong, you'll lose a try.
'''

import os
import pickle
import random


# This byte stream was created using Pickle Protocol 5.
# You'll at least Python 3.8 to de-serialize it.
with open(os.path.join(os.path.dirname(__file__), "words.pickle"), "rb") as f:
    WORDS = pickle.load(f)
with open(os.path.join(os.path.dirname(__file__), "hangman_art.pickle"), "rb") as f:
    HANGMAN_ART = pickle.load(f)
with open(os.path.join(os.path.dirname(__file__), "hangman_title.pickle"), "rb") as f:
    HANGMAN_TITLE = pickle.load(f)


WORD = random.choice(WORDS)
word_hidden = ["-" for letter in WORD]
word_bool_array = [False for letter in WORD]
failed_guesses = 0 # pylint: disable=C0103

print(HANGMAN_TITLE)
print("Welcome to the Hangman game!")


while not all(word_bool_array) and failed_guesses < 7:
    print("".join(word_hidden))
    print(HANGMAN_ART[failed_guesses])
    is_a_success = False # pylint: disable=C0103
    guess = input("\nGuess a letter:\n")
    for index, character in enumerate(WORD):
        if character == guess:
            word_hidden[index] = character
            word_bool_array[index] = True
            is_a_success = True # pylint: disable=C0103

    if is_a_success:
        is_a_success = False # pylint: disable=C0103
    else:
        failed_guesses += 1



if all(word_bool_array):
    print("\nCongratulations. You won!")
else:
    print("\nSorry, you lose!")
    print(f"The word was {WORD}")
