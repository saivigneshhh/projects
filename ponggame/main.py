from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen=Screen()
screen.title("pong game")
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball=Ball()
scoreboard=ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

#detects collison


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(r_paddle)<50 and ball.xcor()<320:
        ball.x_bounce()
        scoreboard.l_point()


    if ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.x_bounce()
        scoreboard.r_point()


    if ball.xcor()>380:
        ball.reset_ball()
        scoreboard.l_point()

    if ball.xcor()<-380:
        ball.reset_ball()
        scoreboard.r_point()


screen.exitonclick()