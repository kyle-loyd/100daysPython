import pandas


def print_out():
    name_input = input("Enter your name: ")
    output = []
    try:
        for letter in name_input:
            output.append(alphabet_dict[letter.capitalize()])
        print(output)
    except KeyError:
        print("Sorry, only letters are allowed.")
        print_out()


alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (_, row) in alphabet.iterrows()}
print_out()

