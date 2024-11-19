import handsigns
import random


# Write your code below this line 👇
def determine_outcome(player, computer):
    if [player, computer] in [[0, 0], [1, 1], [2, 2]]:
        return "The game is a draw!"
    else:
        outcome_code = str(player) + str(computer)
        return handsigns.outcomes[outcome_code]


def print_move(player_name, choice):
    handsign_images = [handsigns.rock, handsigns.paper, handsigns.scissors]
    handsign_names = ["rock", "paper", "scissors"]
    print(handsign_images[choice])
    print(f"{player_name} has chosen: {handsign_names[choice]}\n")


player_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
player_input_int = int(player_input)
computer_input = random.randint(0, 2)

print_move("Player", player_input_int)
print_move("Computer", computer_input)
print(determine_outcome(player_input_int, computer_input))
