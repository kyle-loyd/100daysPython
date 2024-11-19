from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def write_level(self, level):
        self.clear()
        self.goto(-210, 170)
        text = f"LEVEL {level}"
        move = False
        align = "left"
        font = ("System", 16, "bold")
        self.write(arg=text, move=move, align=align, font=font)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        text = "GAME OVER"
        move = False
        align = "center"
        font = ("System", 24, "bold")
        self.write(arg=text, move=move, align=align, font=font)