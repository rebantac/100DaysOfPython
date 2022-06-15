import os
from p10_art import logo

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations ={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
        
def calculator():
    os.system('cls')
    print(logo)

    for operator in operations:
        print(operator)

    num1 = float(input("Enter first number: "))

    flag = "y"
    while flag == "y":
        num2 = float(input("Enter next number: "))
        operator = input("Enter operator: ")

        function = operations[operator]
        answer = round(function(num1, num2), 1)

        print(f"{num1} {operator} {num2} = {answer}")

        flag = input(f"Countinue with {answer}? Type 'y' to continue, 'r' to restart with new value and 'n' to exit:  ")
        
        if flag == "y":
            num1 = answer
        elif flag == "r":
            calculator() # Recursion

calculator()
