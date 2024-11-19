from random import randint

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def select_characters(count, character_set):
  output = []
  while count > 0:
    index = randint(0, len(character_set) - 1)
    output += character_set[index]
    count -= 1
  return output


def build_character_set(letter_count, number_count, symbol_count):
  character_set = select_characters(letter_count, letters)
  character_set += select_characters(number_count, numbers)
  character_set += select_characters(symbol_count, symbols)
  return character_set


def build_index_pool(count):
    output = []
    for i in range(0, count):
        output.append(i)
    return output


def build_password(letters, numbers, symbols):
  character_set = build_character_set(letters, numbers, symbols)
  output = ""
  index_pool = build_index_pool(len(character_set))
  while len(index_pool) > 0:
      random_index = randint(0, len(index_pool) - 1)
      output += character_set[index_pool[random_index]]
      index_pool.pop(random_index)
  return output