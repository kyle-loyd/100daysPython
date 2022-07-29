import game

def yesno_input(prompt):
    while True:
        user_input = input(prompt).lower()
        valid = yesno_input_is_valid(user_input)
        if not valid:
            print("Invalid input.")
            continue
        if valid and user_input == "y":
            return True
        return False

def yesno_input_is_valid(user_input):
    valid_input = ["y", "n"]
    if user_input not in valid_input:
        return False
    return True

def print_hand(target_player):
    name = "Your" if target_player.name == "human" else "CPU"
    hand = ', '.join([(card.name if not card.face_down else 'X') for card in target_player.hand])
    value = "?" if target_player.hand[0].face_down else target_player.hand_value
    print(f"{name} hand: [ {hand} ]; ({value})")

def print_game():
    print_hand(current_game.human)
    print_hand(current_game.cpu)

def play_turn():
    while True:
        current_game.evaluate()
        if current_game.is_over:
            return
        print_game()
        human_draw_condition = yesno_input
        cpu_draw_condition = current_game.cpu.hand_value < current_game.human.hand_value 
        draw_condition = human_draw_condition("Draw a card? (y/n): ") if current_game.current_turn.name == "human" else cpu_draw_condition 
        if draw_condition:
            current_game.draw(current_game.current_turn, face_down=False)
        else:
            current_game.next_turn()
            return

def blackjack():
    global current_game
    print("Welcome to Blackjack!")
    current_game = game.Game()
    play_turn()
    if not current_game.is_over:
        play_turn()
    else:
        current_game.next_turn()
    print_game()
    print(f"The winner is {current_game.winner}!")
    return yesno_input("Play again? (y/n): ")

current_game = None
while True:
    play_again = blackjack()
    if not play_again:
        break