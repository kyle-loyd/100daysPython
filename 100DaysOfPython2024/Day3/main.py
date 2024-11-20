title = "~ ~ Welcome to Treasure Island ~ ~\nYour mission is to find the treasure hidden deep in the temple."
lever_prompt = "Two switches are on the wall ahead of you.  Which will you flip?\nleft or right? "
death_lever = "A trap door opens beneath you and you fall to your death.  Game Over."
lever_transition = "The switch activates a secret passage through the wall.  You enter the room within."
water_prompt = "The room contains a large, dark pit full of water.  You see a door across the pool.\nswim or wait? "
death_swim = "A giant trouts mouth snaps around you.  You have been eaten.  Game over."
water_transition = "Upon further inspection, you find a vine and swing over the pool.  You enter the door."
door_prompt = "Through the door, you see three buttons, each with a corresponding door.\nblue yellow or red? "
death_red = "Through the red door, you slide down a long chute into a raging inferno.  Game over."
death_blue = "Through the blue door, you are mauled by a tiger.  Game over."
victory = "Through the yellow door sits an overflowing chest full of gold.  You win!"
death_invalid = "A spider bites your big toe and you explode.  Game over."

print(title)
choice = input(lever_prompt)
if not choice == "left":
    print(death_lever)
    quit()
print(lever_transition)
choice = input(water_prompt)
if not choice == "wait":
    print(death_swim)
    quit()
print(water_transition)
choice = input(door_prompt)
if choice == "red":
    print(death_red)
    quit()
elif choice == "blue":
    print(death_blue)
    quit()
elif choice == "yellow":
    print(victory)
    quit()
else:
    print(death_invalid)

