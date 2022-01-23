from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

name = input("What is your name? ")
bid_price = input("How much do you wanna bid? $")
other_bidder = input("Are there other users who would like to bid? Enter yes or no.")

all_bidders = []

def add_bidders_info(bidder, price):
  bidders_info = {}
  bidders_info["name"] = bidder
  bidders_info["bid"] = price
  
  all_bidders.append(bidders_info)

add_bidders_info(name, bid_price)

def find_highest_bid():


def other_bidders():
  if other_bidder == yes:
    clear()
    add_bidders_info()
  else:
    find_highest_bid()