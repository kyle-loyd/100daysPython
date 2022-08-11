from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.boundary_buffer = 180
        self.shape("turtle")
        self.color("LimeGreen")
        self.penup()
        self.setheading(90)
        self.start()
        

    def start(self):
        self.goto(0,-1 * self.boundary_buffer)

    def move_forward(self):
        self.setheading(90)
        self.forward(20)

    def move_left(self):
        if self.xcor() > -1 * self.boundary_buffer:
            self.setheading(180)
            self.forward(20)

    def move_right(self):
        if self.xcor() < self.boundary_buffer:
            self.setheading(0)
            self.forward(20)

    def move_backward(self):
        if self.ycor() > -1 * self.boundary_buffer:
            self.setheading(270)
            self.forward(20)