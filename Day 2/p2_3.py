# Days, Weeks and Months left in your life 

age = input("Enter age: ")

age_in_int = int(age)
age_in_int = 90 - age_in_int

month = age_in_int * 12
week = age_in_int * 52
day = age_in_int * 365

print(f"You have {day} days, {week} weeks, {month} months left.")