from turtle import Turtle, Screen
from random import randint

color_list = ["medium orchid", "dark sea green", "steel blue", "goldenrod", "crimson", "coral" ]

turtle = Turtle()
turtle.speed(0)
turtle.pensize(10)
turtle.penup()
turtle.setposition(-200, -200)
for row in range(10):
    for column in range(10):
        turtle.pencolor(color_list[randint(0,5)])
        turtle.pendown()
        turtle.dot()
        turtle.penup()
        if column == 9:
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(450)
            turtle.left(180)
        else:
            turtle.forward(50)
screen = Screen()
screen.exitonclick()
