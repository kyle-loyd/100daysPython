import inputs
import cipher

actions = {
    "encode": lambda m, s: cipher.encode(message=m, shift=s),
    "decode": lambda m, s: cipher.decode(message=m, shift=s)
}

exit_app = False
while not exit_app:
    print("Welcome to the Caesar Cypher Tool!")
    action = inputs.get_action()
    message = input("Please enter message: ")
    shift = inputs.get_shift()

    output = actions[action](m=message, s=shift)
    print(f"Your {action}d message: {output}")

    run_again = inputs.run_again()
    if run_again == "n":
        exit_app = True
