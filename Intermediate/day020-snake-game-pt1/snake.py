from turtle import Turtle

class Snake:
    def __init__(self):
        self.body = []
        self.default_config = {
            "shape": "square",
            "color": "white",
            "size": 20
        }
        self.new_snake()

    def add_snake_segment(self, position):
        turtle = Turtle(shape=self.default_config["shape"])
        turtle.shape(self.default_config["shape"])
        turtle.color(self.default_config["color"])
        turtle.penup()
        turtle.goto(position)
        self.body.append(turtle)

    def new_snake(self):
        self.add_snake_segment((0, 0))
        self.add_snake_segment((-20, 0))
        self.add_snake_segment((-40, 0))

    def move(self):
        for segment in range(len(self.body) - 1, 0, -1):
            x = self.body[segment - 1].xcor()
            y = self.body[segment - 1].ycor()
            self.body[segment].goto((x, y))
        self.body[0].forward(20)

    def up(self):
        self.body[0].setheading(90)

    def right(self):
        self.body[0].setheading(0)

    def down(self):
        self.body[0].setheading(270)

    def left(self):
        self.body[0].setheading(180)