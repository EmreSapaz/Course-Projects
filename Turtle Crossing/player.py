from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(-25,-280)
        self.setheading(90)


    def move(self):
        y = self.ycor() + 50
        self.goto(self.xcor(),y)


    def reset_position(self):
        self.goto(0,-280)