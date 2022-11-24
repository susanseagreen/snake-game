from turtle import Turtle

TEXT_ALIGN = "center"
FONT = ("Arial", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.get_high_score()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()

        self.update_scoreboard()

    def get_high_score(self):
        with open("high_score.txt") as file:
            # check that file has valid data
            try:
                contents = file.read()
                if contents:
                    self.high_score = int(contents)
            except ValueError:
                self.high_score = 0

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score}        High Score: {self.high_score}",
            align=TEXT_ALIGN,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
