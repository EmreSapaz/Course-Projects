import time
import random
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(1200,900)
screen.bgcolor("black")
screen.title("Pong")

screen.listen()
screen.tracer(0)

r_paddle = Paddle(570,0)
l_paddle = Paddle(-570,0)
ball = Ball()
scoreboard = Scoreboard()
change_direction = ["Up","Down","Right","Left"]
change_speed = ["True","False"]

screen.onkey(l_paddle.move_paddle_up,"w")
screen.onkey(r_paddle.move_paddle_up,"Up")
screen.onkey(l_paddle.move_paddle_down,"s")
screen.onkey(r_paddle.move_paddle_down,"Down")

game_is_on = True

screen.update()
time.sleep(1)

while game_is_on:
    time.sleep(.015)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 430 or ball.ycor() < -430:
        ball.bounce_y()

    if ball.xcor() > 650 :
        scoreboard.increase_score_computer()
        ball.teleport(0,0)
        screen.update()
        time.sleep(1)
        if random.choice(change_direction) == "Left" or random.choice(change_direction) == "Right" :
            ball.bounce_x()

        if random.choice(change_direction) == "Up" or random.choice(change_direction) == "Down":
            ball.bounce_y()

        if random.choice(change_speed) == "True":
            ball.increase_speed()

    if ball.xcor() < -650 :
        scoreboard.increase_score_player()
        ball.teleport(0, 0)
        screen.update()
        time.sleep(1)

        if random.choice(change_direction) == "Left" or random.choice(change_direction) == "Right":
            ball.bounce_x()

        if random.choice(change_direction) == "Up" or random.choice(change_direction) == "Down":
            ball.bounce_y()

        if random.choice(change_speed) == "True":
            ball.increase_speed()

    if ball.distance(r_paddle) < 60 and ball.xcor() > 550 :
        ball.bounce_x()

    if  ball.distance(l_paddle) < 60 and ball.xcor() < -550:
        ball.bounce_x()

    if scoreboard.score_player == 5 or scoreboard.score_computer == 5:
        ball.hideturtle()
        r_paddle.hideturtle()
        l_paddle.hideturtle()
        screen.update()
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()