from turtle import Screen
import random
import time
from snake import Snake
from food import Food
from scoreboard  import Score_Board


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Score_Board()

screen.listen()
screen.onkey(snake.Up,"Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Left,"Left")
screen.onkey(snake.Right,"Right")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    #food detection
    if snake.head.distance(food)<15:
         food.refresh()
         snake.extend()
         scoreboard.increase_score()


    ''' detects  the wall collison'''


    if snake.head.xcor()>280 or snake.head.ycor()<-280 or snake.head.ycor()>280 or  snake.head.xcor()<-280:
        game_is_on=False
        scoreboard.game_over()

    '''detects the collison with the tail'''


    for segment in snake.segment[1:]:
         if  snake.head.distance(segment)<10:
             game_is_on=False
             scoreboard.game_over()


screen.exitonclick()