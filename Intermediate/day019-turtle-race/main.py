from turtle import Turtle, Screen
from random import randint

class TurtleConfig:
    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.position = position

def set_up_turtle(config):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(config.color)
    turtle.goto(x=-230, y=config.position)
    return turtle

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

turtle_configs = [
    TurtleConfig("red", "IndianRed", 75), 
    TurtleConfig("orange", "DarkOrange", 45), 
    TurtleConfig("yellow", "Gold", 15), 
    TurtleConfig("green", "Olive", -15), 
    TurtleConfig("blue", "CornflowerBlue", -45), 
    TurtleConfig("purple", "MediumOrchid", -75)
]
turtles = []
for config in turtle_configs:
    turtles.append({"instance": set_up_turtle(config), "config": config})

if user_bet:
    is_race_on = True

win_loss_message = None
winning_turtle = None
while is_race_on:
    for turtle in turtles:
        random_distance = randint(0, 10)
        turtle["instance"].forward(random_distance)
        if turtle["instance"].xcor() > 230:
            is_race_on = False
            if turtle["config"].name == user_bet:
                print(f"You win!  The {turtle['config'].name} came in first!")
            else:
                print(f"You lose!  The {turtle['config'].name} came in first!")


screen.exitonclick()