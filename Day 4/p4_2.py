import random

string_names = input("Enter all the names separated by ',': ")
names_list = string_names.split(", ")

random_num = random.randint(0, len(names_list) - 1)

print(f"{names_list[random_num]} will pay the bill")