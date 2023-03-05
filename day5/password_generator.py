'''
Password Generator.
This program will generate a (pseudo)random string of letters, numbers, and symbols 
that you can use as a password.
'''

import random
import string
import sys

LETTERS = list(string.ascii_letters)
NUMBERS = list(string.digits)
#SYMBOLS = list(string.punctuation)
# We'll use a subset of string.punctuation since a lot of symbols
# are rejected by login apps.
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generator_with_prompt():
    '''
    An user interface for the password generator function.
    The interface will ask for a specific amount of letters,
    numbers, and symbols to include in the password and then it
    will print it to the stdout.
    '''
    print("Welcome to the Password Generator!")

    amount_of_letters = input(''.join((
        'How many letters would you like in your password? ',
        'Type an positive integer number.\n')))
    try:
        amount_of_letters = int(amount_of_letters)
    except ValueError:
        sys.exit(f"{amount_of_letters} is not a valid number.")
    if amount_of_letters < 0:
        sys.exit(f"{amount_of_letters} is not a positive number.")

    amount_of_numbers = input(''.join((
        'How many numbers would you like in your password? ',
        'Type an positive integer number.\n')))
    try:
        amount_of_numbers = int(amount_of_numbers)
    except ValueError:
        sys.exit(f"{amount_of_numbers} is not a valid number.")
    if amount_of_numbers < 0:
        sys.exit(f"{amount_of_numbers} is not a positive number.")

    amount_of_symbols = input(''.join((
        'How many symbols would you like in your password? ',
        'Type an positive integer number.\n')))
    try:
        amount_of_symbols = int(amount_of_symbols)
    except ValueError:
        sys.exit(f"{amount_of_symbols} is not a valid number.")
    if amount_of_symbols < 0:
        sys.exit(f"{amount_of_symbols} is not a positive number.")

    password = password_generator(amount_of_letters, amount_of_numbers, amount_of_symbols)

    print(f"Your password is: {password}")
    print("You should flush your stdout and clear your console history after copying this.")


def password_generator(letters=10, numbers=1, symbols=1):
    ''''
    Given a number of letters, digits, and symbols, this function
    will return a string of shuffled characters of each type, according
    to the amounts specified.
    '''
    password = []
    for _ in range(letters):
        password.append(random.choice(LETTERS))
    for _ in range(numbers):
        password.append(random.choice(NUMBERS))
    for _ in range(symbols):
        password.append(random.choice(SYMBOLS))

    random.shuffle(password)
    password = ''.join(password)

    return password


if __name__ == "__main__":
    password_generator_with_prompt()
