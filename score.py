from turtle import Turtle
FONT = ("Arial", 50, "normal")
class Score(Turtle):
    def __init__(self,loc):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(loc)
        self.write_score()

    def write_score(self):
        self.write(self.score, False, "center",FONT )

    def update_score(self):
        self.clear()
        self.score +=1
        self.write_score()


