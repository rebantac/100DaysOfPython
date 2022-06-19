from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

items = Menu()
cm_obj = CoffeeMaker()
mm_obj = MoneyMachine()

flag = True
while flag:
    choice = input(f"What would you like? ({items.get_items()}): ")

    if choice == "off":
        flag = False
    elif choice == "report":
        cm_obj.report()
        mm_obj.report()
    else:
        drink = items.find_drink(choice)
        
        if cm_obj.is_resource_sufficient(drink) and mm_obj.make_payment(drink.cost):
            cm_obj.make_coffee(drink)
            