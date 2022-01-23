from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

auction_over = False

all_bidders = {}

highest_bidder = 0

def highest_bidder():
  for bid in all_bidders:
    if bid > highest_bidder:
      bid = highest_bidder
      print(f"{name} is the highest bidder! You win!")

while auction_over == False:
  name = input("What is your name? ")
  bid_price = input("How much do you wanna bid? $")
  all_bidders[name] = bid_price

  more_bidders = input("Are there other users who would like to bid? Enter yes or no. ")
  
  if more_bidders == "no":
    auction_over = True
  elif more_bidders == "yes":
    clear()
    highest_bidder()