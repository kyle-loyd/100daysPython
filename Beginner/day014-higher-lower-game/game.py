import game_data
import random

class Game:
    def __init__(self):
        self.remaining_options = [i for i in range(0,len(game_data.data) - 1)]
        self.option_one = None
        self.option_two = None
        self.correct_answer = None
        self.number_correct = 0
        self.is_over = False
        self.total_options = len(game_data.data)
        self.new_round()

    def select_option(self):
        while True:
            remaining_options_index = random.randint(0, len(self.remaining_options) - 1)
            selected_option = self.remaining_options[remaining_options_index]
            self.remaining_options.pop(remaining_options_index)
            selected_data = game_data.data[selected_option]
            is_option_one = self.option_one == None
            if is_option_one:
                return game_data.data[selected_option]
            else: 
                equal_to_option_one = selected_data["follower_count"] == self.option_one["follower_count"]
                if not equal_to_option_one:
                    return game_data.data[selected_option]

    def get_correct_answer(self):
        if self.option_one["follower_count"] > self.option_two["follower_count"]:
            return self.option_one
        elif self.option_two["follower_count"] > self.option_one["follower_count"]:
            return self.option_two
        else:
            raise Exception("option_one and option_two are equal; Internal error")

    def answer_is_correct(self, answer):
        options = [self.option_one, self.option_two]
        answer_option = options[answer - 1]
        if answer_option['name'] == self.correct_answer['name']:
            return True
        else:
            self.is_over = True
            return False

    def new_round(self):
        if not self.correct_answer == None:
            self.number_correct += 1
            self.option_one = self.option_two.copy()
        else:
            self.option_one = self.select_option()
        self.option_two = self.select_option()
        self.correct_answer = self.get_correct_answer()