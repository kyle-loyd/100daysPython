from turtle import Screen
from snake import Snake
import time

score = 0
game_is_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()

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
    

screen.exitonclick()