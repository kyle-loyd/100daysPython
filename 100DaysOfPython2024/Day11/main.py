import hand

player_hand = hand.Hand()
cpu_hand = hand.Hand()
game_over = False
player_turn_over = False
cpu_turn_over = False


def player_turn():
    valid_responses = ["1", "2"]
    while True:
        response = input("Your move (1: Hit, 2: Stay): ")
        if response.isnumeric() and response in valid_responses:
            return response
        print("Invalid input.")


def print_results():
    player_wins = (player_hand.value > cpu_hand.value or cpu_hand.bust) and not player_hand.bust
    draw = player_hand.value == cpu_hand.value

    print(f"\n\n** Game Results")
    print(f"CPU hand: {cpu_hand.cards}; {cpu_hand.value}")
    print(f"Your hand: {player_hand.cards}; Value: {player_hand.value}")
    if draw:
        print("Game draw!")
    else:
        print(f"{'You' if player_wins else 'CPU'} win{'s' if not player_wins else ''}!")


while not game_over:
    while not player_turn_over:
        print(f"\nCPU hand: [{cpu_hand.cards[0]}, X]")
        print(f"Your hand: {player_hand.cards}; Value: {player_hand.value}")
        move = player_turn()
        if move == "1":
            player_hand.add_card()
            print(f"** Player draws a {player_hand.cards[-1].name}.")
            if player_hand.bust:
                game_over = True
                player_turn_over = True
                cpu_turn_over = True
                continue
        else:
            player_turn_over = True
    while not cpu_turn_over:
        if cpu_hand.value > player_hand.value or cpu_hand.value == player_hand.value:
            game_over = True
            cpu_turn_over = True
        print(f"\nYour hand: {player_hand.cards}; Value: {player_hand.value}")
        print(f"CPU hand: {cpu_hand.cards}; {cpu_hand.value}")
        if cpu_hand.value <= 17 and cpu_hand.value < player_hand.value:
            cpu_hand.add_card()
            if cpu_hand.bust:
                game_over = True
                cpu_turn_over = True
                continue
        else:
            cpu_turn_over = True
print_results()
