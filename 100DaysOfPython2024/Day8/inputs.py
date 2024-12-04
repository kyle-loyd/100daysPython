def get_action():
    while True:
        valid_actions = ["encode", "decode"]
        action = input("Please choose an action (encode/decode): ").lower()
        if action in valid_actions:
            return action
        print("Please enter a valid action.")


def get_shift():
    while True:
        shift = input("Shift by: ")
        if shift.isdigit():
            shift = int(shift)
            if shift > 0:
                return shift
            else:
                print("Please enter positive shift.")
        else:
            print("Please enter positive numeric shift.")


def run_again():
    while True:
        valid_answers = ["y", "n"]
        answer = input("Run the app again? (y/n): ")
        if answer in valid_answers:
            return answer
        print(f"Answer \"{answer}\" is invalid.")
