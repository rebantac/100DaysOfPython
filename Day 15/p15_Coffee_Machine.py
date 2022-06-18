MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
avail_money = 0


def make_coffee(drink, choice):
    ingredients = drink["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {choice}. Enjoy!")


def check_transaction(money, drink):
    if drink["cost"] <= money:
        change = round(money - drink["cost"], 2)
        print(f"Here is ${change} in change.")

        global avail_money
        avail_money += drink["cost"]
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def check_money():
    print("Insert Coins:")
    quarter = int(input("How many quarter? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total = quarter + dimes + nickles + pennies

    return total


def check_avail(ingredient):
    for item in ingredient:
        if ingredient[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${avail_money}")


flag = True
while flag:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        flag = False
    elif choice == "report":
        print_report()
    else:
        drink = MENU[choice]
        flag = check_avail(drink["ingredients"])
        if flag:
            total = check_money()
            if check_transaction(total, drink):
                make_coffee(drink, choice)
