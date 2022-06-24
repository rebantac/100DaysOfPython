from turtle import Turtle


class Score(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = -1
        self.penup()
        self.hideturtle()
        self.shapesize(stretch_len=10, stretch_wid=10)
        self.setpos(0, 260)
        self.color("white")
        self.update_score()

        
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align="center", font="24")

    def game_over(self):
        self.setpos(0, 0)
        self.write("Game Over!", align="center", font="24")
