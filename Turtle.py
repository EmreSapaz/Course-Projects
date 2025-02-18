# import time
# from turtle import Turtle,Screen
# import random
#
# tim = Turtle()
# tim.shape("turtle")
# screen = Screen()
# screen.colormode(255)
#
#
#
# screen.exitonclick()

# colors = []
# for i in range(8):
#     color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
#     colors.append(color)

# for i in range(8):
#     angle = 360 / num
#     tim.color(colors[color_num])
#     for j in range(num):
#         tim.forward(100)
#         tim.right(angle)
#     num += 1
#     color_num += 1

# tim.color(colors[0])
# for i in range(3):
#     tim.forward(100)
#     tim.right(120)

# tim.color(colors[1])
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# tim.color(colors[2])
# for i in range(5):
#     tim.forward(100)
#     tim.right(72)

# tim.color(colors[3])
# for i in range(6):
#     tim.forward(100)
#     tim.right(60)

# tim.color(colors[4])
# for i in range(7):
#     tim.forward(100)
#     tim.right(360/7)

# tim.color(colors[5])
# for i in range(8):
#     tim.forward(100)
#     tim.right(45)

# tim.color(colors[6])
# for i in range(9):
#     tim.forward(100)
#     tim.right(40)

# tim.color(colors[7])
# for i in range(10):
#     tim.forward(100)
#     tim.right(36)

# for i in range(10):
#     tim.forward(5)
#     x = tim.position()[0]
#     y = tim.position()[1]
#     tim.teleport(x+10,y)

# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# for _ in range(100):
#     tim.pensize(width)
#     tim.color(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
#     tim.forward(50)
#     tim.setheading(random.randint(0,360))
#     width += .5
#     time.sleep(.1)

# heading = 0
# increase = 5
# tim.speed("fastest")
# times : int = int(360/increase) + 1
#
# for i in range(times):
#     tim.color(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
#     tim.circle(100)
#     tim.setheading(heading)
#     heading += increase