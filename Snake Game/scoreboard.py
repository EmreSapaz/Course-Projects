from turtle import Turtle
ALIGN ="center"
FONT = ("Arial",24,"normal")
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.write(f"Score : {self.score}",align=ALIGN,font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.color("white")
        self.goto(0,0)
        self.write("!!!Game Over !!!", align=ALIGN, font=FONT)
        self.goto(0,-50)
        self.write(f"Your Score : {self.score}", align=ALIGN, font=FONT)