import pandas
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (_, row) in alphabet.iterrows()}
name_input = input("Enter your name: ")
output = []
for letter in name_input:
    output.append(alphabet_dict[letter.capitalize()])
print(output)
