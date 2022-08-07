from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

score = 0
game_is_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "d")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "s")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "a")
screen.onkey(snake.left, "Left")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.score_point()
        food.refresh()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        game_is_on = False

    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
scoreboard.game_over()

screen.exitonclick()