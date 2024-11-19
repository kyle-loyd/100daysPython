from tkinter import CENTER
from turtle import Turtle

CONCRETE = "gray64"
ASPHALT = "gray10"
CENTERLINE = "gold"

class Artist(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setheading(180)
        self.draw_roads()

    def draw_roads(self):
        self.draw_solid_line(-165, CONCRETE)
        self.draw_solid_line(-160, ASPHALT)
        self.draw_dashed_line(-120, CENTERLINE)
        self.draw_dashed_line(-80, CENTERLINE)
        self.draw_solid_line(-40, ASPHALT)
        self.draw_solid_line(-35, CONCRETE)
        self.draw_solid_line(30, CONCRETE)
        self.draw_solid_line(35, ASPHALT)
        self.draw_dashed_line(75, CENTERLINE)
        self.draw_dashed_line(115, CENTERLINE)
        self.draw_solid_line(155, ASPHALT)
        self.draw_solid_line(160, CONCRETE)

    def draw_solid_line(self, ycor, color):
        self.penup()
        self.goto(305, ycor)
        self.pendown()
        self.pencolor(color)
        self.forward(550)

    def draw_dashed_line(self, ycor, color):
        self.penup()
        self.goto(305, ycor)
        self.pendown()
        self.pencolor(color)
        for i in range(0,50):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()


    