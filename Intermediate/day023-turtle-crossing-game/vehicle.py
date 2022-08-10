from turtle import Turtle
from random import randint

DIRECTION_CONFIG = {
    "left": { 
        "heading": 180,
        "lanes": [55, 95, 135],
        "starting_x": 250
    },
    "right": {
        "heading": 0,
        "lanes": [-140, -100, -60],
        "starting_x": -250
    }
}
COLOR_OPTIONS = [
    "SteelBlue1",
    "Red3",
    "DarkOrchid3",
    "Gray10",
    "Orange3"
]
SPEED_OPTIONS = [ 10, 20, 30, 40, 50 ]

class Vehicle(Turtle):

    def __init__(self, direction):
        super().__init__()
        self.color(COLOR_OPTIONS[randint(0, len(COLOR_OPTIONS) - 1)])
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.movement_speed = SPEED_OPTIONS[randint(0,len(SPEED_OPTIONS) - 1)]
        self.pick_lane(direction)

    def pick_lane(self, direction):
        lane_options = DIRECTION_CONFIG[direction]["lanes"]
        starting_y = lane_options[randint(0,len(lane_options)-1)]
        starting_x = DIRECTION_CONFIG[direction]["starting_x"]
        self.goto(starting_x, starting_y)

    def move(self):
        self.forward(self.movement_speed)
        