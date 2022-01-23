from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

all_bidders = {}
auction_over = False
  
def highest_bidder(bids):
  highest_bid = 0
  winner = ""
  for bidder in bids:
    bid_amount = bids[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"{winner} is the winner with a bid of {highest_bid} dollars.")  

while auction_over == False:
  name = input("What is your name? ")
  bid_price = int(input("How much do you wanna bid? $"))
  all_bidders[name] = bid_price

  more_bidders = input("Are there other users who would like to bid? Enter yes or no. ").lower
  
  if more_bidders == "no":
    auction_over = True
    highest_bidder(all_bidders)
  elif more_bidders == "yes":
    clear()