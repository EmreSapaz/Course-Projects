from turtle import Turtle,Screen

tim =Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backwards():
    tim.back(10)
def turn_right():
    tim.right(5)
def turn_left():
    tim.left(5)
def clear_screen():
    screen.reset()

screen.listen()
screen.onkeypress(move_forward,"w")
screen.onkeypress(move_backwards,"s")
screen.onkeypress(turn_right,"d")
screen.onkeypress(turn_left,"a")
screen.onkey(clear_screen,"c")

screen.exitonclick()