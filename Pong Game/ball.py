from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.move_x = 5
        self.move_y = 5
        self.move_speed = 1

    def move_ball(self):
        new_x = self.xcor() + (self.move_x * self.move_speed)
        new_y = self.ycor() + (self.move_y * self.move_speed)
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1
        self.move_speed *= 1.05

    def set_speed(self):
        self.move_speed = 1
