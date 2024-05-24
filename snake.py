from turtle import Turtle, Screen
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_snake(position)


    def add_snake(self, position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)

    def extend(self):
        self.add_snake(self.segments[-1].position())
    def move(self):
        for snake_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snake_number - 1].xcor()
            new_y = self.segments[snake_number - 1].ycor()
            self.segments[snake_number].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset_snakes(self):
        for seg in self.segments:
            seg.goto(1000, 900)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]