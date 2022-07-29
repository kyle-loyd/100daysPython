import constants
import game
import draw

game.start_game()
while not game.is_complete():
    draw.current_game()
    guess = input("Guess: ").lower()
    if not guess.isalpha():
        print(constants.invalid_input_message)
        input()
        continue
    else:
        game.check_guess(guess)
    if game.is_complete():
        draw.final()

print(constants.you_win_message if game.player_wins() else constants.you_lose_message)