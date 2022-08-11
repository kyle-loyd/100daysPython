from turtle import Screen
from player import Player
from artist import Artist
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()

screen.onkeypress(player.move_forward, "w")
screen.onkeypress(player.move_forward, "Up")
screen.onkeypress(player.move_left, "a")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "d")
screen.onkeypress(player.move_right, "Right")
screen.onkeypress(player.move_backward, "s")
screen.onkeypress(player.move_backward, "Down")

game_is_on = True
active_vehicles = []
previous_second = None
scoreboard.write_level(game.level)
while game_is_on:
    screen.update()
    sleep(0.012)
    game.generate_wave()
    vehicles = game.active_vehicles.copy()
    for vehicle in vehicles:
        vehicle.move()
        if vehicle.xcor() > 300 or vehicle.xcor() < -300:
            game.active_vehicles.remove(vehicle)
        if vehicle.distance(player) < 20:
            for lane in vehicle.get_lanes():
                player_in_lane = player.ycor() < int(lane) + 20 and player.ycor() < int(lane) - 20
                if player_in_lane:
                    game_is_on = False

    if player.ycor() > 180:
        game.level_up()
        scoreboard.write_level(game.level)
        player.start()
scoreboard.game_over()

screen.exitonclick()