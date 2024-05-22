COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random
class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        randon_chance = random.randint(1,6)
        if randon_chance == 2:
            t0 = Turtle("square")
            t0.shapesize(stretch_wid=1, stretch_len=2)
            t0.color(random.choice(COLORS))
            t0.penup()
            random_y = random.randint(-250, 250)
            t0.goto(280, random_y)
            self.all_cars.append(t0)

    def car_move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT