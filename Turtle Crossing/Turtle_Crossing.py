import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from cars import CarManager

screen = Screen()
screen.setup(1000,600)
screen.bgpic("road.gif")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(player.move,"w")

game_is_on = True

while game_is_on:

    time.sleep(0.03)
    screen.update()

    car_manager.create_cars()
    car_manager.move_car()

    if player.ycor() > 280 :
        player.reset_position()
        scoreboard.level_up()
        car_manager.increase_speed()

    for car in car_manager.all_cars:
        if car.xcor() < -580 or car.xcor() > 580:
            car.clear()

    for car in car_manager.all_cars:
        if player.distance(car) < 30:
            screen.update()
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()