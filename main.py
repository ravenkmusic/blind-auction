from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

other_bidder = True

while other_bidder:
  name = input("What is your name? ")
  bid_price = input("How much do you wanna bid? $")

  all_bidders = []

  def add_bidders_info(bidder, price):
    bidders_info = {}
    bidders_info["name"] = bidder
    bidders_info["bid"] = price
    
    all_bidders.append(bidders_info)

  add_bidders_info(name, bid_price)

  more_bidders = input("Are there other users who would like to bid? Enter yes or no. ")
  
  if more_bidders == "no":
    other_bidder = False
    