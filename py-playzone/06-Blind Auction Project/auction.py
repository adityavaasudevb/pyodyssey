# TODO-1: Ask the user for input

# TODO-2: Save data into dictionary {name: price}

# TODO-3: Whether if new bids need to be added

# TODO-4: Compare bids in dictionary

import art
print(art.logo)

def compare(bids):
    max_bid=0
    winner=''
    for bidder in bids:
        bid_amount=bids[bidder]
        if bid_amount>max_bid:
            max_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of ${max_bid}")

bids = {}
while(1):
    name = input("What is your name?:")
    price = int(input("What is your bid?: $"))

    bids[name] = price

    choice = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if choice=="no":
        compare(bids)
        break
    else:
        print("\n" * 20)

