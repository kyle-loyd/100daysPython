import art
import game
import os

def print_round(current_game):
    print(art.logo)
    print_option(current_game.option_one)
    print(art.vs)
    print_option(current_game.option_two)
    return

def print_option(option):
    print(f"{option['name']}, a {option['description']} from {option['country']}, has {option['follower_count']} followers")
    return

def get_answer():
    while True:
        answer_input = input("Guess (1 or 2): ")
        valid = answer_is_valid(answer_input)
        if valid:
            return int(answer_input)
        else:
            print("Invalid input.")

def answer_is_valid(answer):
    valid_options = ["1", "2"]
    if answer in valid_options:
        return True
    else:
        return False

def print_result(number_correct, total_options):
    print(f"Game over!  You guessed {number_correct}/{total_options - 1} correctly!")
    return

def higher_or_lower():
    current_game = game.Game()
    while not current_game.is_over:
        os.system("cls||clear")
        print_round(current_game)
        user_answer = get_answer()
        correct = current_game.answer_is_correct(user_answer)
        if correct:
            current_game.new_round()
        else:
            print_result(current_game.number_correct, current_game.total_options)

# -- Start -- #
higher_or_lower() 
