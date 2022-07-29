print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
prompt_one = "You're at a crossroad.  Where do you want to go?  Type \"left\" or \"right\"\n"
prompt_one_wrong_choice = "You fell into a hole. Game Over."
prompt_two = "You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n"
prompt_two_wrong_choice = "You get attacked by an angry trout. Game Over."
prompt_three = "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n"
prompt_three_options = [ "red", "blue", "yellow" ]
prompt_three_outputs = {
  "red": "It's a room full of fire. Game Over.",
  "blue": "You enter a room of beasts. Game Over.",
  "yellow": "You found the treasure! You Win!"
}
prompt_three_invalid_choice = "You chose a door that doesn't exist. Game Over."

prompt_one_response = input(prompt_one)
if prompt_one_response != "left":
  print(prompt_one_wrong_choice)
  exit()
prompt_two_response = input(prompt_two)
if prompt_two_response != "wait":
  print(prompt_two_wrong_choice)
  exit()
prompt_three_response = input(prompt_three)
print(prompt_three_outputs.get(prompt_three_response, prompt_three_invalid_choice))