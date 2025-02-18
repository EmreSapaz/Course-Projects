import turtle
from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
turtle.bgpic("Race.png")
screen.colormode(255)
screen.setup(width=1040,height=400)
user_bet = screen.textinput("Race","Who will win the race?\nPick a Color:")
colors = ["red","orange","pink","green","blue","purple"]
y = 175
racers = []

for i in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-500,y)
    racers.append(new_turtle)
    i += 1
    y -= 70

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in racers:
        move = random.randint(0,10)
        turtle.forward(move)
        if turtle.pos()[0] >= 500:
            is_race_on = False
            winner_color = turtle.color()[0]
            if user_bet == winner_color:
                turtle.write(f"You Win !!! The winner is {turtle.color()[0]}", font=("Verdana", 15, "normal"), align="right")
            else:
                turtle.write(f"You Lose. Your Bet was {user_bet}. The winner is {turtle.color()[0]}", font=("Verdana", 15, "normal"), align="right")




screen.exitonclick()