''''
Choose Your Own Adventure-like game.
You followed a treasure map and arrived at Treasure Island.
That's how far the map took you. Now you're on your own.
Good luck finding the treasure.
'''

import sys
import os

# Python is not smart enough to find relative paths. So, this trick is needed
# in order to execute the script from root of the repository.
with open(os.path.join(os.path.dirname(__file__), 'treasure.txt'), 'r', encoding='utf-8') as f:
    TREASURE = f.read()

with open(os.path.join(os.path.dirname(__file__),'tombstone.txt'), 'r', encoding='utf-8') as f:
    TOMBSTONE = f.read()

print(TREASURE)
print('Welcome to Treasure Island.\n Your mission is to find the treasure.')

choice = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
if choice == "right":
    print("You fall into a hole.\nGame Over.")
    print(TOMBSTONE)
    sys.exit()
elif choice == "left":
    choice = input(''.join((
        'You come to a lake. There is an island in the middle of the lake. ',
        'Type "wait" to wait for a boat. Type "swim" to swim across.\n'))
        ).lower()
    if choice == "swim":
        print("You are attacked by a trout.\nGame Over.")
        print(TOMBSTONE)
        sys.exit()
    elif choice == "wait":
        choice = input(''.join((
            'You arrive at the island unharmed. There is a house with 3 doors. ',
            'One red, one yellow, and one blue. Which door do you open? ',
            'Type "red", "yellow" or "blue".\n'))
            ).lower()
        if choice == "red":
            print("You are burned by fire.\nGame Over.")
            print(TOMBSTONE)
            sys.exit()
        elif choice == "blue":
            print("You are eaten by beasts.\nGame Over.")
            print(TOMBSTONE)
            sys.exit()
        elif choice == "yellow":
            print("You find the treasure.\nYou win!")
            sys.exit()
        else:
            print(f"{choice} is not a valid input.")
            sys.exit()
    else:
        print(f"{choice} is not a valid input.")
        sys.exit()
else:
    print(f"{choice} is not a valid input.")
    sys.exit()
