import os


def get_bidder_name():
    while True:
        raw_name = input("Please enter bidder name: ")
        if raw_name.isalpha():
            return raw_name.capitalize()
        print("Name entered is invalid.")


def get_bid():
    while True:
        raw_bid = input("Please enter bid: $")
        if raw_bid.isnumeric() and float(raw_bid) > 0:
            return float(raw_bid)
        print("Bid entered is invalid.")


def more_bids():
    valid_responses = ["y", "n"]
    while True:
        raw_response = input("Are there more bids? (y/n): ")
        if raw_response.isalpha() and raw_response.lower() in valid_responses:
            return True if raw_response == "y" else False
        print("Input is invalid.")


def clear():
    command = 'cls' if os.name in ('nt', 'dos') else 'clear'
    os.system(command)


bids = {}
while True:
    name = get_bidder_name()
    bid = get_bid()
    bids[name] = bid
    if not more_bids():
        break
    clear()

winning_key = ""
for key in bids:
    if winning_key == "":
        winning_key = key
        continue
    if bids[key] > bids[winning_key]:
        winning_key = key
winning_bid = "{:.2f}".format(bids[winning_key])
print(f"The winner is {winning_key} with a bid of ${winning_bid}!")
