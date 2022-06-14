height = float(input("Enter height: "))
weight = float(input("Enter weight: "))

bmi = round(weight / height ** 2, 1)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi > 18.5 and bmi < 25:
    print(f"Your bmi is {bmi}, you have normal height")
elif bmi > 25 and bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight")
elif bmi > 30 and bmi < 35:
    print(f"Your bmi is {bmi}, you are obese")
else:
    print(f"Your bmi is {bmi}, you are clinically obese")