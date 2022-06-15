import os
import p9_art 

print(p9_art.logo)
print("Welcome to silent auction!")

auction_data = {}

flag = "yes"
while flag == "yes":
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: Rs."))

    auction_data[name] = bid

    flag = input("Are there any other bidders? Type 'yes' or 'no': ")
    
    os.system('cls')

max_bid = 0
max_bidder = ""

for name in auction_data:
    bid = auction_data[name]

    if max_bid < bid:
        max_bid = bid
        max_bidder = name

print(f"The item was sold at Rs.{max_bid} to {max_bidder}")