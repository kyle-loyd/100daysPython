from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def shift_letters(text, shift):
  new_string = ""
  for letter in text:
    if not letter.isalpha() or letter == " ":
      new_string += letter
      continue
    new_index = alphabet.index(letter) + shift
    new_string += alphabet[new_index if new_index < 26 else new_index % 26]
  return new_string

def encrypt(text, shift):
  print(f"The encrypted text is {shift_letters(text, shift)}")

def decrypt(text, shift):
  print(f"The decrypted text is {shift_letters(text, shift * -1)}")

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
  encrypt(text, shift)
elif direction == "decode":
  decrypt(text, shift)
else:
  print("Invalid input")
