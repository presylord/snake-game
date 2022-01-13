from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("darkblue")
screen.title("Snake Game")
screen.tracer(0)

segments = []

for _ in range(0, 3):
    segment = Turtle(shape="square")
    segment.color("white")
    segment.penup()
    segment.goto(_*-20, 0)
    segments.append(segment)

screen.update()

game_on = True
while game_on:
    for segment in segments:
        segment.forward(20)
        time.sleep(.1)
    screen.update()

screen.exitonclick()