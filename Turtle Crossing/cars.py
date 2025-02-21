import random
from turtle import Turtle


Colors = ["red","orange","yellow","green","blue","purple"]


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = 10

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 6:
            new_car = Turtle("square")
            new_car.shapesize(1,3)
            new_car.penup()
            new_car.color(random.choice(Colors))
            random_y = random.choice(range(-230, 270, 50))
            new_car.goto(480,random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed *= 1.2
