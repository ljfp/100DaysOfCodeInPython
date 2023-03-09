'''
Blind Auction.
This is a program to run a First-price sealed-bid auction.
See: https://en.wikipedia.org/wiki/First-price_sealed-bid_auction
'''

from getpass import getpass
import os
import pickle
import sys

with open(os.path.join(os.path.dirname(__file__), "hammer_logo.pickle"), "rb") as logo_file:
    logo = pickle.load(logo_file)

print("Welcome to the Blind Auction!")

bids = {}
bidders_remaining = True # pylint: disable=C0103
while bidders_remaining:
    name = input("Please state your name: ")
    price = int(getpass("Now state your bid: $"))
    bids[name] = price
    bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if bidders == "yes":
        continue
    if bidders == "no":
        bidders_remaining = False # pylint: disable=C0103
    else:
        sys.exit(f"{bidders} is not a valid input.")

winning_bid = 0 # pylint: disable=C0103
winner = ["", 0]
for bidder in bids: # pylint: disable=C0206
    if bids[bidder] > winning_bid:
        winning_bid = bids[bidder]
        winner[0] = bidder
        winner[1] = bids[bidder]

print(f"The winner is {winner[0]} with a bid of {winner[1]}!")
