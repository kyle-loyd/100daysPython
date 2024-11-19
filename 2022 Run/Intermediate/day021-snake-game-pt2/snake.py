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
        self.head = self.body[0]

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
    
    def extend(self):
        self.add_snake_segment(self.body[-1].position())

    def move(self):
        for segment in range(len(self.body) - 1, 0, -1):
            x = self.body[segment - 1].xcor()
            y = self.body[segment - 1].ycor()
            self.body[segment].goto((x, y))
        self.body[0].forward(20)

    def up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)

    def right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)

    def down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)

    def left(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)