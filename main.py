import random
import turtle
from turtle import Turtle, Screen
is_race_on = False
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make you bet", prompt="which turtle will win the race? Enter a colir: ")
colors = ["red", "orange", "yellow", "blue", "purple", "green"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for i in range(0, 6):
    t0 = Turtle("turtle")
    t0.penup()
    t0.color(colors[i])
    t0.goto(x=-230, y=y_position[i])
    all_turtles.append(t0)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            if user_bet == turtle.color()[0]:
                print(f"You have won the game! \nThe {turtle.pencolor()} is the winner.")
            else:
                print(f"You have lost the game! \nThe {turtle.pencolor()} is the winner.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()