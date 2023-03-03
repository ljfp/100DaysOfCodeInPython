''''
Tip Calculator.
This program will calculate how much money should each diner
contribute in order to pay bill plus the tip.
'''

# TODO: use Decimals for these type of calculations
#from decimal import getcontext, Decimal
#getcontext().prec = 2

print("Welcome to the tip calculator.")
bill = float(input("What was the bill? $"))
tip = int(input("What percentage tip would you like to give? "))
diners = int(input("How many people to split the bill? "))


def tip_calculator(bill, tip, diners):
    ''''
    given the bill, the desired tip percentage, and the amount
    of diners, calculate the total bill (including tip) and
    print how much should each diner contribute to pay the bill
    '''
    tip_as_percent = tip / 100
    total_tip = bill * tip_as_percent
    contribution_per_person = round(((bill + total_tip) / diners), 2)

    print(f"Each person should pay: {contribution_per_person}")
    return 0

if __name__ == "__main__":
    tip_calculator(bill, tip, diners)
