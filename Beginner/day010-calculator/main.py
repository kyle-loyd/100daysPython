import arithmetic
import art

def get_number(which_number):
  while True:
    number_input = input(f"{which_number} number: ")
    try:
      return float(number_input)
    except ValueError:
      print("Invalid input.")  

def get_operator():
  while True:
    operator = input("Operator (+, -, *, /): ")
    if operator in arithmetic.operations.keys():
      return operator
    print("Invalid input.")

def continue_calculation():
  user_input = input("Continue?: ").lower()
  if user_input == "y" or user_input == "n":
    return True if user_input == "y" else False
  print("Invalid input.")

def calculator():
  first_run = True
  carryover = None
  print(art.logo)
  while True:
    if first_run:
      num_one = get_number("First")
    else:
      num_one = carryover
      print(f"First number: {num_one}")
    num_two = get_number("Second")
    operator = get_operator()
    solution = arithmetic.operations[operator](num_one, num_two)
    print(f"Solution: {num_one} {operator} {num_two} = {solution}")
    if continue_calculation():
      first_run = False
      carryover = solution
    else:
      first_run = True
      carryover = None
      calculator()

calculator()