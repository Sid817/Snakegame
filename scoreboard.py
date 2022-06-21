from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as score_file:
            self.highscore=int(score_file.read())
        # self.highscore=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
        self.score=0
        with open("data.txt",mode="w") as score_file:
            score_file.write(f"{self.highscore}")

        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        # self.clear()
        # since we are doing it in the update_score() method, no need to call clear() twice
        self.update_scoreboard()

