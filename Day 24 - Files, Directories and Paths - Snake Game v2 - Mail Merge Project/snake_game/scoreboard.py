from turtle import Turtle


class Score(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("data.txt", mode='r') as file1:
            self.high_score = int(file1.read())
        self.penup()
        self.hideturtle()
        self.shapesize(stretch_len=10, stretch_wid=10)
        self.setpos(0, 260)
        self.color("white")
        self.update_score()

        
    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}    High Score: {self.high_score}", align="center", font="24")


    def increase_score(self):
        self.score += 1
        self.update_score()
    

    def reset_highscore(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("data.txt", mode='w') as file1:
                file1.write(str(self.high_score))

        self.score = 0
        self.update_score()
