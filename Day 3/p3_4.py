print("Welcome!")
size = input("What size pizza do you want? S, M or L: ")
add_pepperoni = input("Add pepperoni? Y or N: ")
extra_cheese = input("Add extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
else:
    bill = 25
    if add_pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Final Bill: Rs.{bill}")