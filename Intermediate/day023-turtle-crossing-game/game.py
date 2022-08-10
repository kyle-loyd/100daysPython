from random import randint
from vehicle import Vehicle

class Game():

    def __init__(self):
        self.active_vehicles = []

    def generate_wave(self):
        upper_limit = randint(0,6)
        for i in range(0,upper_limit):
            if i % 2 == 0:
                self.add_car("left")
            elif i % 3 == 0 or i == 1:
                self.add_car("right")

    def add_car(self, direction):
        self.active_vehicles.append(Vehicle(direction))