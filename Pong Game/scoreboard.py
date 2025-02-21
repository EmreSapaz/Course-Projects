from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_player = 0
        self.score_computer = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,380)
        self.write(f"{self.score_computer}            {self.score_player}",False,"center",("Arial",48,"normal"))

    def increase_score_player(self):
        self.clear()
        self.score_player += 1
        self.write(f"{self.score_computer}            {self.score_player}", False, "center", ("Arial", 48, "normal"))

    def increase_score_computer(self):
        self.clear()
        self.score_computer += 1
        self.write(f"{self.score_computer}            {self.score_player}", False, "center", ("Arial", 48, "normal"))


    def game_over(self):
        self.clear()
        self.color("white")
        self.goto(0,0)
        self.write(f"{self.score_computer} --- {self.score_player}", False, "center", ("Arial", 48, "normal"))