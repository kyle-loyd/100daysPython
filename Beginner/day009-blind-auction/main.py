from os import system
import art

bids = {}
more_bidders = True

def get_valid_bidder():
  while True:
    bidder = input("Name of bidder: ")
    if bidder_is_valid(bidder):
      return bidder
    else:
      print("Invalid input.")  

def bidder_is_valid(bidder):
  for char in bidder:
    if not char.isalpha():
      return False
  return True

def get_valid_bid():
  while True:
    bid = input("Enter bid: ")
    if bid_is_valid(bid):
      return int(bid)
    else:
      print("Invalid input.  Positive integers only.") 

def bid_is_valid(bid):
  for char in bid:
    if not char.isdigit():
      return False
  return True

def register_bid(bidder, bid):
  global bids
  bids[bidder] = bid

def get_valid_add_bidder_input():
  while True:
    add_bidder_input = input("Add another bidder? (Y/N): ").lower()
    if add_bidder_input == "y" or add_bidder_input == "n":
      return True if add_bidder_input == "y" else False
    else:
      print("Invalid input.  Positive integers only.") 

def get_highest_bid():
  highest_bid = { "bidder": "", "bid": 0 }
  for bid in bids:
    if bids[bid] > highest_bid["bid"]:
      highest_bid["bidder"] = bid
      highest_bid["bid"] = bids[bid]
  return highest_bid

while more_bidders:
  print(art.logo)
  bidder = get_valid_bidder()
  bid = get_valid_bid()
  register_bid(bidder, bid)
  more_bidders = get_valid_add_bidder_input()
  system("cls||clear")
print(art.logo)
highest_bid = get_highest_bid()
print(f"The highest bidder, {highest_bid['bidder']}, has won the item at ${highest_bid['bid']}")