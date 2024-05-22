from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.goto(0, 270)
        self.penup()
        self.hideturtle()
        self.color('white')
        self.update_score()
        file.close()



    def update_score(self):
        self.clear()
        self.write(f"Score:  {self.score}   High Score:  {self.high_score}", False, ALIGNMENT, FONT)
    def get_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file1:
                file1.write(f"{self.high_score}")
                file1.close()
        self.score = 0
        self.update_score()
