from turtle import Turtle,Screen

color_list = [(1, 9, 30), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21),
 (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73),(205, 63, 91), (168, 129, 78),
 (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135),
 (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209),(229, 173, 165),
 (70, 70, 45), (185, 190, 201), (126, 225, 231), (88, 49, 45), (61, 65, 66)]

tim = Turtle()

tim.pensize(20)
num = 0
tim.hideturtle()
tim.speed("fastest")
tim.teleport(-200,-200)
x = tim.pos()[0]
y = tim.pos()[1]

screen = Screen()
screen.colormode(255)

for j in range(10):
    for i in range(10):
        tim.color(color_list[num])
        tim.forward(0)
        tim.penup()
        tim.forward(50)
        tim.pendown()
        if len(color_list)>num + 1:
            num += 1
        else:
            num = 0
    tim.teleport(x,y+50)
    y += 50

screen.exitonclick()