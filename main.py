import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("My Turtle Crossing")

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.car_move()


    #Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 15:
            game_is_on = False
            scoreboard.game_over()


    if player.is_at_finish_line():
        scoreboard.get_level()
        player.go_starting_point()
        car_manager.level_up()

screen.exitonclick()