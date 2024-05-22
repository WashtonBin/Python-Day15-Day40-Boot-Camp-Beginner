from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score_board = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.get_score()
        snake.extend()

    #detect collision with wall
    if snake.head.xcor()> 280 or snake.head.xcor()< -280 or snake.head.ycor()> 280 or snake.head.ycor()< -280:
        score_board.reset()
        # game_is_on = False
        snake.reset_snakes()
        score_board.reset()
        snake.segments[0].goto(0, 0)

    #Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            # game_is_on = False
            snake.reset_snakes()
            score_board.reset()
            snake.segments[0].goto(0, 0)





screen.exitonclick()