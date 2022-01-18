from turtle import Turtle




class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.SCORE = 0
        self.score()

    def score(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.write("SCORE: " + str(self.SCORE), move=False, align="center", font=("Courier", 20, "normal"))

