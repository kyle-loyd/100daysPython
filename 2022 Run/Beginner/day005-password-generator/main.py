# Password Generator Project
from password_generator import build_password

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

print(f"Your new password is: {build_password(nr_letters, nr_numbers, nr_symbols)}")
