from turtle import Turtle, Screen

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.draw_score()

    def draw_score(self):
        self.clear()
        text = f"Score : {self.score}"
        move_turtle = False
        alignment = "center"
        font_style = ("System", 20, "bold")
        self.write(text, move_turtle, alignment, font_style)

    def score_point(self):
        self.score += 1
        self.draw_score()

    def game_over(self):
        self.goto(0,0)
        text = "GAME OVER"
        move_turtle = False
        alignment = "center"
        font_style = ("System", 30, "bold")
        self.write(text, move_turtle, alignment, font_style)