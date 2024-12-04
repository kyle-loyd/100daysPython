alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def shift_char(char, shift):
    base_index = alphabet.index(char)
    new_index = base_index + shift
    return alphabet[new_index]


def handle(message, shift):
    output = ""
    for char in message:
        if char in alphabet:
            if char.isupper():
                lower_char = char.lower()
                new_char = shift_char(lower_char, shift).upper()
                output += new_char
            else:
                new_char = shift_char(char, shift)
            output += new_char
        else:
            output += char
    return output


def encode(message, shift):
    return handle(message, shift)


def decode(message, shift):
    return handle(message, shift * -1)
