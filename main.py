from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("darkblue")
screen.title("Snake Game")
screen.tracer(0)



screen.update()
game_on = True
snake = Snake()
while game_on:
    time.sleep(.1)
    snake.move()

    screen.listen()
    screen.update()

screen.exitonclick()