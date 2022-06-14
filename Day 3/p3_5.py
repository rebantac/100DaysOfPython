print("Welcome!")
name1 = input("Enter your name: ").lower()
name2 = input("Enter their name: ").lower()

count1 = (name1 + name2).count("t")+(name1 + name2).count("r") + (name1 + name2).count("u") +(name1 + name2).count("e")
count2 = (name1 + name2).count("l")+(name1 + name2).count("o") + (name1 + name2).count("v") +(name1 + name2).count("e")

print(f"Love score is {count1}{count2}%.")