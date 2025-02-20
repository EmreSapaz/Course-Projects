from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("pink")
        self.speed("fastest")
        self.reposition()

    def reposition(self):
        random_x = random.choice(range(-280,280,10))
        random_y = random.choice(range(-280,280,10))
        self.goto(random_x, random_y)