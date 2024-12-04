def get_operand(which_operand):
    while True:
        raw = input(f"Please enter {which_operand} number: ")
        try:
            return int(raw)
        except ValueError:
            try:
                return float(raw)
            except ValueError:
                print("Number invalid.")


def get_operation():
    valid_operations = ["+", "-", "*", "/"]
    while True:
        raw = input(f"Please enter operation (+, -, *, /): ")
        if raw in valid_operations:
            return raw
        print("Operator invalid.")


def calculate(operand_one, operand_two, action):
    actions = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }
    return actions[action](operand_one, operand_two)


def calculate_again():
    valid_responses = ["y", "n"]
    while True:
        raw = input("Continue? (y/n): ")
        if raw.isalpha() and raw.lower() in valid_responses:
            return True if raw == "y" else False
        print("Input is invalid.")


repeat = False
first_operand = 0
while True:
    first_operand = first_operand if repeat else get_operand("first")
    second_operand = get_operand("second")
    operation = get_operation()

    result = calculate(first_operand, second_operand, operation)
    print(f"Result: {'{:.2f}'.format(result) if result is float else result}")

    if not calculate_again():
        break
    first_operand = result
    repeat = True
