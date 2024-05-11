from turtle import Turtle
P_WID = 6
P_LEN = 0.75
DISTANCE = 20


class Paddle(Turtle):
    def __init__(self,loc):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(P_WID,P_LEN)
        self.goto(loc)


    def move_up(self):
        new_y = self.ycor() + DISTANCE
        self.goto(self.xcor(),new_y)

    def move_down(self):
        new_y = self.ycor() - DISTANCE
        self.goto(self.xcor(),new_y)





