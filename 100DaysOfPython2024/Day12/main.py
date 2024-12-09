import random


def get_difficulty_input():
    valid_input = ["easy", "hard"]
    while True:
        response = input("Choose a difficulty (easy, hard): ")
        if response.lower() in valid_input:
            return 10 if response.lower() == "easy" else 5
        print("Please enter \"easy\" or \"hard\".")


def get_guess_input():
    while True:
        response = input("Guess the number: ")
        if response.isnumeric():
            return int(response)
        print("Please guess a number.")


random_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")
guesses_left = get_difficulty_input()
while guesses_left > 0:
    guess = get_guess_input()
    guesses_left -= 1
    if guess == random_number:
        print("You guessed my number!")
        exit()
    if guess > random_number:
        print("My number is lower.")
    else:
        print("My number is higher.")
print(f"You lose!  My number was {random_number}.")
