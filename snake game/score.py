from turtle import Turtle
font = ("Arial", 20, "normal")
align = 'center'

# data = open("data.txt", mode='r+')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode='r') as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.write(f"score = {self.score} high score = {self.high_score}", True, align=align,
                   font=font)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_Score()
    # def game_over(self):
    #     self.color('white')
    #     self.goto(0, 0)
    #     self.write("game over", align='center', font=("Arial", 20, "normal"))

    def update_Score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"score = {self.score} high score = {self.high_score}", True, align=align,
                   font=font)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_Score()
