import os
import constants
import game


def current_game():
  title()
  progress(game.get_progress())
  stage(game.get_stage_index())
  mistakes(game.get_mistake_list())


def final():
  current_game()
  if game.player_loses():
    print(f"The word was: {game.selected_word}")


def title():
  os.system("cls||clear")
  print(f"{constants.title}\n")


def progress(progress):
  print(f"Word: {' '.join(progress)}")


def stage(stage_index):
  print(f"{constants.stages[stage_index]}")


def mistakes(mistake_list):
  print(f"Mistakes: {' '.join(mistake_list)}")