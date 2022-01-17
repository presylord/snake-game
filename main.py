from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("darkblue")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
screen.update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True

while game_on:
    time.sleep(.1)
    snake.move()

    screen.update()

screen.exitonclick()