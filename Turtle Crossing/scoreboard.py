from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-485,250)
        self.write(f"Level {self.level}",font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level {self.level}",font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("You Lose!!!",align="center",font=FONT)
        self.goto(0,-50)
        self.write(f"Level {self.level}", align="center",font=FONT)
