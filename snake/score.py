from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("record.txt", "r") as record:
            self.highscore = int(record.read())
        self.write_score()

    def write_score(self):
        self.reset()
        self.color("green")
        self.penup()
        self.hideturtle()
        self.goto(-150, 300)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(150, 300)
        self.write(f"High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        if self.score > self.highscore:
            with open("record.txt", "w") as file:
                file.write(f"{self.score}")
