from random import randint
from vehicle import Vehicle
from time import localtime, strftime

class Game():

    def __init__(self):
        self.active_vehicles = []
        self.level = 1
        self.speed_options = [ 2, 4, 6, 8, 10 ]
        self.last_wave_second = None

    def generate_wave(self):
        current_second = strftime("%S", localtime())
        first_run = self.last_wave_second == None
        new_second = not self.last_wave_second == current_second
        if first_run or new_second:
            self.last_wave_second = current_second
            upper_limit = randint(0,6)
            for i in range(0,upper_limit):
                if i % 2 == 0:
                    self.add_car(direction="left", speeds=self.speed_options)
                elif i == 1 or i == 5:
                    self.add_car(direction="right", speeds=self.speed_options)

    def add_car(self, direction, speeds):
        self.active_vehicles.append(Vehicle(direction, speeds))

    def level_up(self):
        self.level += 1
        new_speeds = [] 
        for speed in self.speed_options:
            new_speeds.append(speed + 2)
        self.speed_options = new_speeds.copy()
