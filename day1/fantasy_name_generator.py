''''
Fantasy Name Generator.
Based on the original Dungeon Master Screen released for D&D 5th Edition.
You need to perform three rolls with a D20 in order to generate a name.
'''

import sys


beginning_dict = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: "A",
    6: "Be",
    7: "De",
    8: "El",
    9: "Fa",
    10: "Jo",
    11: "Ki",
    12: "La",
    13: "Ma",
    14: "Na",
    15: "O",
    16: "Pa",
    17: "Re",
    18: "Si",
    19: "Ta",
    20: "Va"
}

middle_dict = {
    1: "bar",
    2: "ched",
    3: "dell",
    4: "far",
    5: "gran",
    6: "hal",
    7: "jen",
    8: "kel",
    9: "lim",
    10: "mor",
    11: "net",
    12: "penn",
    13: "quil",
    14: "rond",
    15: "sark",
    16: "shen",
    17: "tur",
    18: "vash",
    19: "yor",
    20: "zen"
}

end_dict = {
    1: "",
    2: "a",
    3: "ac",
    4: "ai",
    5: "al",
    6: "am",
    7: "an",
    8: "ar",
    9: "ea",
    10: "el",
    11: "er",
    12: "ess",
    13: "ett",
    14: "ic",
    15: "id",
    16: "il",
    17: "in",
    18: "is",
    19: "or",
    20: "us"
}


def fantasy_name_generator():
    ''''
    Prompts the user to roll a D20 three times 
    and generates a fantasy name based on the results and
    a lookup table.
    '''
    print("Welcome to the Fantasy Name Generator!\n")

    # First roll
    first_roll = input("Please, throw a D20 and write the result of your roll here: ")
    try:
        beginning_key = int(first_roll)
    except ValueError:
        sys.exit(f"{first_roll} is not a number.")
    check_if_key_is_valid(beginning_key, beginning_dict)

    # Second roll
    second_roll = input("Throw a D20 again and write the result of the here: ")
    try:
        middle_key = int(second_roll)
    except ValueError:
        sys.exit(f"{second_roll} is not a number.")
    check_if_key_is_valid(middle_key, middle_dict)

    # Third roll
    third_roll = input("One last time, throw a D20 and write the result of the roll here: ")
    try:
        end_key = int(third_roll)
    except ValueError:
        sys.exit(f"{third_roll} is not a number.")
    check_if_key_is_valid(end_key, end_dict)

    # Generate and print the fantasy name
    capitalize_if_beginning_is_empty(beginning_key, beginning_dict, middle_key, middle_dict)
    fantasy_name = beginning_dict[beginning_key] + middle_dict[middle_key] + end_dict[end_key]

    print(f"Your name is: {fantasy_name}!")

    # End the execution
    return 0

def check_if_key_is_valid(key, dictionary):
    ''''
    Checks if the given key exists in the given dictionary.
    If it doesn't exists, quit the program gracefully.
    '''
    value = dictionary.get(key)
    if value is None:
        sys.exit("Insert valid number (i.e: an integer from 1 to 20).")


def capitalize_if_beginning_is_empty(first_key, first_dict, second_key, second_dict):
    ''''
    If the first part of the name is an empty string, 
    capitalize the syllable of the second part. 
    '''
    if first_dict[first_key] == "":
        second_dict[second_key] = second_dict[second_key].capitalize()


if __name__ == "__main__":
    fantasy_name_generator()
