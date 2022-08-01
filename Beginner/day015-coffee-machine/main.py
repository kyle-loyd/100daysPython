# TODO: Prompt user for their selection
# TODO: Add option to turn machine off
# TODO: Add option to print a report of stored money and product
# TODO: Check inventory to ensure drink can be made
# TODO: Process coin insertion
# TODO: Handle return of change
# TODO: Update inventory when coffee is made to reflect usage
import machine
from os import system

def selection_is_valid(selection):
    valid_selections = ["cappuccino", "espresso", "latte", "report", "off"]
    return selection in valid_selections

def get_selection():
    while True:
        selection = input("Please enter beverage selection (cappuccino, espresso, latte): ")
        valid = selection_is_valid(selection)
        if valid:
            return selection
        else:
            print("Invalid input.")

def process_payment(product_cost):
    coin_names = ["quarters", "dimes", "nickels", "pennies"]
    coin_values = {
        "quarters": 0.25,
        "dimes": 0.1,
        "nickels": 0.05,
        "pennies": 0.01
    }
    while True:
        paid_amount = 0
        print("Please provide payment: ")
        for coin in coin_names:
            if paid_amount > 0:
                print(f"Current Payment: ${'{:.2f}'.format(paid_amount)}")
            coin_count = input(f"# of {coin}: ")
            valid = coin_count_is_valid(coin_count)
            if valid:
                paid_amount += int(coin_count) * coin_values[coin]
        if paid_amount < product_cost:
            print("Insufficient funds provided.  Returning coins.  Please try again.")
        else:
            return paid_amount

def coin_count_is_valid(coin_count):
    try:
        is_a_number = coin_count.isdigit()
        return is_a_number
    except ValueError:
        print("Invalid input.")
        return False

def return_change(product_cost, amount_paid):
    change_due = amount_paid - product_cost
    print(f"Returning due change of ${'{:.2f}'.format(change_due)}")

def print_report(current_machine):
    print("Resource Report:")
    print(f"Water: {current_machine.ingredients['water']}")
    print(f"Milk: {current_machine.ingredients['milk']}")
    print(f"Coffee: {current_machine.ingredients['coffee']}")
    print(f"Available Funds: ${'{:.2f}'.format(current_machine.stored_funds)}")
    enter_to_continue()

def enter_to_continue():
    input("** Press <ENTER> to continue.. **")

def power_on():
    current_machine = machine.Machine()
    while True:
        system("cls||clear")
        print("Welcome to the Coffee Machine!")
        selection = get_selection()
        if selection == "off":
            return
        elif selection == "report":
            print_report(current_machine)
            continue
        product_cost = current_machine.get_product_cost(selection)
        print(f"The \"{selection}\" product costs ${'{:.2f}'.format(product_cost)}.")
        amount_paid = process_payment(product_cost)
        current_machine.order(selection)
        print(f"Here is your {selection}! Enjoy!")
        return_change(product_cost, amount_paid)
        enter_to_continue()

power_on()