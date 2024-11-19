# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()
print("Successfully read invited_names.txt!")

with open(r"Input/Letters/starting_letter.txt", "r") as template_file:
    template = template_file.read()
print("Successfully read starting_letter.txt!")

for name in names:
    stripped_name = name.strip("\n")
    print(f"Creating {stripped_name.lower()}_letter.txt..")
    with open(fr"Output/ReadyToSend/{stripped_name.lower()}_invite.txt", "w") as output_file:
        output = template.replace("[name]", stripped_name.capitalize())
        output_file.write(output)

print("Work complete!")
input("Press <ENTER> to continue..")
