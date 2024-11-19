from random import randint

class Game:
    def __init__(self):
        self.number_to_guess = randint(1, 100)
        self.remaining_guesses = 0
        self.is_over = False
        self.player_won = False
        self.guess_too_high = "Incorrect. Our guess is lower."
        self.guess_too_low = "Incorrect. Our guess is higher."

    def select_difficulty(self, difficulty):
        difficulties = {
            "easy": 10,
            "hard": 5
        }
        self.remaining_guesses = difficulties[difficulty]

    def evaluate_guess(self, guess):
        if not guess == self.number_to_guess:
            self.remaining_guesses -= 1
            if self.remaining_guesses == 0:
                self.is_over = True
            if self.number_to_guess > guess:
                return self.guess_too_low
            else:
                return self.guess_too_high
        else:
            self.is_over = True
            self.player_won = True
            return None

