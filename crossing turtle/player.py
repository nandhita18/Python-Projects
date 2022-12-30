# STARTING_POSITION = (0, -280)
# MOVE_DISTANCE = 10
# FINISH_LINE_Y = 280
from turtle import Turtle, Screen

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def starting_point(self):
        self.goto(0,-280)


    def is_on_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False