from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed(0)
        self.draw_score()

    def draw_score(self):
        self.clear()
        self.goto(-5, 250)
        text = f"{self.p1_score}\t{self.p2_score}"
        move_turtle = False
        alignment = "center"
        font_style = ("System", 30, "bold")
        self.write(text, move_turtle, alignment, font_style)

    def player_one_score(self):
        self.p1_score += 1
        self.draw_score()

    def player_two_score(self):
        self.p2_score += 1
        self.draw_score()

    def game_over(self):
        self.goto(0,0)
        text = "GAME OVER"
        move_turtle = False
        alignment = "center"
        font_style = ("System", 30, "bold")
        self.write(text, move_turtle, alignment, font_style)