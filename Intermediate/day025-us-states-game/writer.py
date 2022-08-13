from turtle import Turtle


class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def state(self, x, y, state):
        self.goto(x, y)
        text = state
        move = False
        align = "left"
        font = ("System", 8, "bold")
        self.write(arg=text, move=move, align=align, font=font)
