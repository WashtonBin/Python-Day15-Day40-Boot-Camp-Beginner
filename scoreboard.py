FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)
        self.hideturtle()
        self.color("black")
        self.update_level()

    def update_level(self):
        self.write(f"Level {self.level}", False, "left", FONT)

    def get_level(self):
        self.clear()
        self.level += 1
        self.update_level()

    def game_over(self):
        self.hideturtle()
        self.goto(0,0)
        self.write("GAME OVER", False, "center", FONT)