from turtle import Turtle

class Courtline(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(-5,-285)
        self.setheading(90)
        self.shape("square")
        self.pensize(5)
        for i in range(0,15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)