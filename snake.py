from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for _ in range(0, 3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(_*-20, 0)
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            cur_seg = self.segments[seg_num]
            cur_seg.goto(new_x, new_y)
        self.segments[0].forward(20)


