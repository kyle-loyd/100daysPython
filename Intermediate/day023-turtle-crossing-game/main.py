from turtle import Screen
from player import Player
from artist import Artist
from game import Game
from time import sleep
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
screen.tracer(0)
screen.listen()

artist = Artist()
player = Player()
game = Game()


screen.onkeypress(player.move, "w")
screen.onkeypress(player.move, "Up")

game_is_on = True
active_vehicles = []
while game_is_on:
    screen.update()
    sleep(0.012)
    game.generate_wave()
    for vehicle in game.active_vehicles:
        vehicle.move()

    if player.ycor() > 180:
        player.start()

    for i in range(0,randint(0, 4)):
        pass

screen.exitonclick()