import game

def prompt_for_difficulty():
    while True:
        difficulty_input = input("Please select \"easy\" or \"hard\" difficulty: ")
        valid = validate_difficulty_input(difficulty_input)
        if valid:
            return difficulty_input

def validate_difficulty_input(difficulty_input):
    valid_inputs = ["easy", "hard"]
    if difficulty_input not in valid_inputs:
        print(f"Invalid input. Valid inputs: [ {[option for option in valid_inputs]}")
        return False
    return True

def get_guess_input():
    while True:
        guess_input = input("Please guess a number [1-100]: ")
        valid = validate_guess_input(guess_input)
        if valid:
            return int(guess_input)

def validate_guess_input(guess_input):
    try:
        guess_input_int = int(guess_input)
        if 101 > guess_input_int > 0:
            return True
        print("Invalid input.  Valid inputs: [1-100]")
        return False
    except ValueError:
        return False

def print_game_result(player_won):
    result_message = "That's correct!  You win!" if player_won else "Out of guesses!  You lose!"
    print(f"{result_message}")

def guessing_game():
    current_game = game.Game()
    current_game.select_difficulty(prompt_for_difficulty())
    while not current_game.is_over:
        guess_input = get_guess_input()
        guess_evaluation = current_game.evaluate_guess(guess_input)
        if not guess_evaluation == None:
            print(guess_evaluation)
            print(f"You have {current_game.remaining_guesses} remaining.")
    print_game_result(current_game.player_won)

guessing_game()