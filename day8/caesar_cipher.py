'''
Caesar Cipher program.
Given a message (or code) and a shift number,
the program will encrypt (or decrypt) the content.
'''

import os
import pickle
import string
import sys

ALPHABET = list(string.ascii_lowercase)


def main():
    '''
    Minimal CLI wrapper for the decode and encode functions in this module.
    '''
    with open(os.path.join(os.path.dirname(__file__), "logo.pickle"), "rb") as logo_file:
        logo = pickle.load(logo_file)
    print(logo)

    operation = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if operation == "encode":
        message = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        encoded_message = encode(message, shift)
        print(f"This is your encoded message:\n{encoded_message}")

    elif operation == "decode":
        code = input("Type your encoded message:\n")
        shift = int(input("Type the shift number:\n"))
        original_message = decode(code, shift)
        print(f"The message says: \n{original_message}")

    else:
        print(f"{operation} is not a valid input.")
        sys.exit()


def decode(code, shift):
    '''
    Given an encoded message (encoded with Caesar's Cipher)
    and a shift number, decode the message and return it.
    '''
    decoded_message = ""
    for letter in code:
        position = ALPHABET.index(letter)
        new_position = position - (shift % 26)
        new_letter  = ALPHABET[new_position]
        decoded_message += new_letter
    return decoded_message


def encode(message, shift):
    '''
    Given a message and a shift number, encode the message
    using Caesar's Cipher and return it.
    '''
    encoded_message = ""
    for letter in message:
        position = ALPHABET.index(letter)
        new_position = position + (shift % 26)
        new_letter  = ALPHABET[new_position]
        encoded_message += new_letter
    return encoded_message


if __name__ == "__main__":
    main()
