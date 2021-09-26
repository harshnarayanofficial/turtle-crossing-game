from turtle import Turtle

FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-270, 260)
        self.write(arg=f"Level: {self.level}", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", font=FONT)