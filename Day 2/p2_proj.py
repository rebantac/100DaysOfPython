# Tip Calculator

print("Welcome to the Tip Calculator!")

amount = float(input("What was the total bill? Rs."))
tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How mnay people to split the bill? "))

amount_per_person = amount * (1 + tip_percent / 100) / people

amount_per_person = "{:.2f}".format(round(amount_per_person, 2))
# format() is used so that there is compulsarily two points after decimal point if even if output is eg. 1.2 => 1.20

print(f"\nEach person should pay: Rs.{amount_per_person}")