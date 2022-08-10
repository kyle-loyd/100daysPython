from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("LimeGreen")
        self.penup()
        self.setheading(90)
        self.start()

    def start(self):
        self.goto(0,-185)

    def move(self):
        self.forward(20)