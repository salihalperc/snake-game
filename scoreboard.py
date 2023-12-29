from turtle import Turtle
FONT = ( "Arial", 16, "normal")
ALIGMENT = "center"


class ScoreBoard(Turtle):


    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
            # self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGMENT, font=FONT)
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGMENT, font=FONT)
        self.score = 0


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGMENT, font=FONT)




    def add_score(self):
        self.clear()
        self.score += 1
        # self.reset()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGMENT, font=FONT)


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGMENT, font=FONT)


