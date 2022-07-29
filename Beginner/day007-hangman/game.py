from random import randint

selected_word = ""
progress = []
mistake_list = []
word_bank = ["bulbasaur", "charmander", "squirtle"]


def start_game():
  select_word()
  build_mistake_list()


def player_wins():
  letters_needed = "_" not in progress
  return letters_needed


def player_loses():
  return get_stage_index() == 6


def is_complete():
  return player_wins() or player_loses()


def select_word():
  global selected_word
  global progress
  word_index = randint(0, len(word_bank) - 1)
  selected_word = word_bank[word_index]
  progress = ["_"] * len(selected_word)


def build_mistake_list():
  global mistake_list
  for i in range(0, 6):
    mistake_list.append("_")


def get_mistake_list():
  return mistake_list


def get_progress():
  return progress


def get_stage_index():
  return 6 - mistake_list.count("_")


def check_guess(guess):
  if guess not in selected_word:
    update_for_incorrect_guess(guess)
  else:
    update_for_correct_guess(guess)


def update_for_incorrect_guess(guess):
  global mistake_list
  mistake_list[get_stage_index()] = guess


def update_for_correct_guess(guess):
  global progress
  for i in range(0, len(selected_word)):
    if selected_word[i] == guess:
      progress[i] = guess
