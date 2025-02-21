from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.teleport(x,y)
        self.color("white")
        self.turtlesize(7,1)
        self.x = self.xcor()
        self.y = self.ycor()

    def move_paddle_up(self):
        self.y += 35
        self.goto(self.x,self.y)

    def move_paddle_down(self):
        self.y -= 35
        self.goto(self.x,self.y)

