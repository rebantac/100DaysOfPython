from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
    

    def point(self, dir):
        if dir == "left":
            self.l_score += 1
        elif dir == "right":
            self.r_score += 1
        self.update_score()
    

    def update_score(self):
        self.clear()
        self.setpos(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.setpos(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
    

    def game_over(self, player):
        self.setpos(0, 0)
        self.write(f"{player} Wins!", align="center", font=("Courier", 20, "normal"))
