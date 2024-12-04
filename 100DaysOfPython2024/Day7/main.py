import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"

game_over = False
correct_letters = []
guesses = []
lives = 6

while not game_over:
    print(f"\nWord: {placeholder}")
    print(f"Guesses: {' '.join(guesses)}")
    print(f"Lives left: {lives}")
    guess = input("Guess a letter: ").lower()
    display = ""

    if guess in guesses:
        print(f"Guess \"{guess}\" has already been guessed.")
        continue

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print(f"\n\nLives left: {lives}\nYou lose.")
            game_over = True
            continue

    guesses += guess
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if "_" not in display:
        print("You win!")
        game_over = True

    placeholder = display
