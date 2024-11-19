from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system

# '{:.2f}'.format(VAR)
def enter_to_continue():
    input("Press <ENTER> to continue..")

while True:
    system("cls||clear")
    current_menu = Menu()
    current_coffee_maker = CoffeeMaker()
    current_money_machine = MoneyMachine()
    menu_input = None
    while True:
        valid_menu_input = current_menu.get_items().split('/') + ["report", "off"]        
        menu_input = input(f"Select product ({current_menu.get_items()}): ")
        if menu_input in valid_menu_input:
            break
        print("Invalid input.")
        enter_to_continue()
        system("cls||clear")
    if menu_input == "report":
        current_coffee_maker.report()
        current_money_machine.report()
        enter_to_continue()
        continue
    elif menu_input == "off":
        break
    else:
        menu_item = current_menu.find_drink(menu_input)
        if not current_coffee_maker.is_resource_sufficient(menu_item):
            print(f"Insufficient resources to make {menu_item.name}.")
            enter_to_continue()
            continue
        print(f"Your {menu_item.name} costs ${'{:.2f}'.format(menu_item.cost)}.")
        if not current_money_machine.make_payment(menu_item.cost):
            print(f"Insufficient funding provided.")
            enter_to_continue()
            continue
        current_coffee_maker.make_coffee(menu_item)
        print(f"Enjoy your {menu_item.name}!")
        enter_to_continue()
