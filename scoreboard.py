from turtle import Turtle

TEXT_ALIGN = "center"
FONT = ("Arial", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=TEXT_ALIGN, font=FONT)
        self.score += 1

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align=TEXT_ALIGN, font=FONT)

