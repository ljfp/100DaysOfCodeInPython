''''
Rock-Paper-Scissors game.
It's a simple implementation of an old classic.
You play against the computer. Type 0 to pick Rock,
type 1 to pick Paper, or type 2 to pick Scissors
'''

import os
import random
import sys


with open(os.path.join(os.path.dirname(__file__), 'rock.txt'), 'r', encoding='utf-8') as f:
    ROCK = f.read()

with open(os.path.join(os.path.dirname(__file__), 'paper.txt'), 'r', encoding='utf-8') as f:
    PAPER = f.read()

with open(os.path.join(os.path.dirname(__file__), 'scissors.txt'), 'r', encoding='utf-8') as f:
    SCISSORS = f.read()

RPS = [ROCK, PAPER, SCISSORS]

print("Welcome to Rock, Paper, Scissors!")

PLAYER_CHOICE = None
while PLAYER_CHOICE not in (0, 1, 2):
    PLAYER_CHOICE = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
    try:
        PLAYER_CHOICE = int(PLAYER_CHOICE)
    except ValueError:
        print(f"{PLAYER_CHOICE} is not a number. Try again.\n")
    if isinstance(PLAYER_CHOICE, int) and PLAYER_CHOICE not in (0, 1, 2):
        print(f"{PLAYER_CHOICE} is not 0, 1 or 2\n")

print(RPS[PLAYER_CHOICE] + "\n")

computer_choice = random.randint(0, 2)

print("Compute chose: \n" + RPS[computer_choice] + "\n")

# If both pick the same option it's a draw
if PLAYER_CHOICE == computer_choice:
    print("It's a draw.")
    # Exit early
    sys.exit()

if PLAYER_CHOICE == 0:
    # Rock lose to Paper
    if computer_choice == 1:
        print("You lose!\n")

    # Rock beats Scissors
    else:
        print("You win!\n")

elif PLAYER_CHOICE == 1:
    # Paper beats Rock
    if computer_choice == 0:
        print("You win!\n")

    # Paper lose to Scissors:
    else:
        print("You lose!\n")

else:
    # Scissors lose to Rock
    if computer_choice == 0:
        print("You lose!\n")
    # Scissors beat Paper
    else:
        print("You win!\n")
