from turtle import Turtle

MOVEMENT_SPEED = 25

class Paddle(Turtle):

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.shape("square")
        self.shapesize(stretch_len=4, stretch_wid=1)
        self.color("white")
        self.penup()
        self.speed(0)
        self.set_position()
        self.setheading(90)
        
    def set_position(self):
        if self.player == 1:
            self.goto(-375, 0)
            return
        self.goto(365, 0)

    def move_up(self):
        if self.ycor() < 240:
            self.forward(MOVEMENT_SPEED)

    def move_down(self):
        if self.ycor() > -240:
            self.backward(MOVEMENT_SPEED)