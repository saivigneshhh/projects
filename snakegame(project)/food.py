from turtle import Turtle
import random

class Food(Turtle):
       def __init__(self):
           super().__init__()
           self.shape("square")
           self.penup()
           self.shapesize(0.5,0.5)
           self.color("white")
           self.speed("fastest")
           self.refresh()

       def refresh(self):
           coordinates_x = random.randint(-280, 280)
           coordinates_y = random.randint(-280, 280)
           food_coordinate = (coordinates_x, coordinates_y)
           self.goto(food_coordinate)
