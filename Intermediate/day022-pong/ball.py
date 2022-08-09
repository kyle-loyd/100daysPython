from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.reset()

    def move(self):
        self.forward(5)

    def bounce_vertical(self):
        new_headings = {
            45: 315,
            315: 45,
            135: 225,
            225: 135
        }
        self.setheading(new_headings[self.heading()])

    def bounce_horizontal(self):
        new_headings = {
            45: 135,
            135: 45,
            315: 225,
            225: 315
        }
        self.setheading(new_headings[self.heading()])

    def reset(self):
        self.goto(0,0)
        self.setheading(45)