from turtle import Screen
from border_line import BorderLine
from paddle import Paddle
from ball import Ball
from score import Score
import time

INIT_LOC_RIGHT = (480, 0)
INIT_LOC_LEFT = (-480, 0)
WALL = 230
NWALL = -230
SCORE_LOC_R =(100,180)
SCORE_LOC_L = (-100,180)

# Screen Init
screen = Screen()
screen.tracer(0)
screen.setup(1000, 500)
screen.title("PONG")
border_line = BorderLine()

# Init
paddle_r = Paddle(INIT_LOC_RIGHT)
paddle_l = Paddle(INIT_LOC_LEFT)
boli = Ball()
score_r = Score(SCORE_LOC_R)
score_l = Score(SCORE_LOC_L)

# Screen Mod
screen.listen()


is_true =True

# PADDLE 1
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")
# PADDLE 2
screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")

while is_true:
    time.sleep(0.05)
    screen.update()
    boli.moving_ball()

# collision with wall
    if boli.ycor() > WALL or boli.ycor() < NWALL:
        boli.bounce_y()
# collision with paddle
    if boli.xcor() > 460 and boli.distance(paddle_r)< 50 or  boli.xcor() < -460 and boli.distance(paddle_l)<50  :
        boli.bounce_x()

    if boli.xcor() > 500 :
        score_l.update_score()
        boli.goto(0,0)
    if boli.xcor() < -500 :
        score_r.update_score()
        boli.goto(0, 0)



screen.exitonclick()
