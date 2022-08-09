from turtle import Screen
from scoreboard import Scoreboard
from courtline import Courtline
from paddle import Paddle
from ball import Ball
from time import sleep

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)
scoreboard = Scoreboard()
courtline = Courtline()

player_one = Paddle(player=1)
player_two = Paddle(player=2)
ball = Ball()

screen.onkeypress(player_one.move_up, "w")
screen.onkeypress(player_one.move_down, "s")
screen.onkeypress(player_two.move_up, "Up")
screen.onkeypress(player_two.move_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.012)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_vertical()
        continue

    hit_p1_paddle = ball.xcor() < -360 and ball.distance(player_one) < 50
    hit_p2_paddle = ball.xcor() > 350 and ball.distance(player_two) < 50
    if hit_p1_paddle or hit_p2_paddle:
        ball.bounce_horizontal()
        continue

    elif ball.xcor() > 390:
        scoreboard.player_one_score()
        sleep(2)
        ball.reset()

    elif ball.xcor() < -390:
        scoreboard.player_two_score()
        sleep(2)
        ball.reset()

screen.exitonclick()