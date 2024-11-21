import random

title = "Welcome to Rock, Paper, Scissors!\n"
move_prompt = "Make your move: Rock (0), Paper (1), or Scissors (2)? "
cpu_move_text = "The computer chose:"
your_move_text = "You chose:"


def get_move_text(move_text, value):
    match int(value):
        case 0:
            return f"{move_text} ROCK"
        case 1:
            return f"{move_text} PAPER"
        case 2:
            return f"{move_text} SCISSORS"
        case _:
            raise IndexError("Only values 0, 1, and 2 are allowed")


def get_winner(cpu, player):
    win = ["21", "10", "02"]
    lose = ["01", "12", "20"]
    result = f"{player}{cpu}"

    if result in win:
        return "You win!"
    elif result in lose:
        return "You lose!"
    else:
        return "Game draw!"


cpu_move = random.randint(0, 2)
your_move = input(move_prompt)
print(get_move_text(cpu_move_text, cpu_move))
print(get_move_text(your_move_text, your_move))
print(get_winner(cpu_move, your_move))
