from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.setpos(-280, 250)
        self.update_level()
    

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=FONT)


    def game_over(self):
        self.setpos(0, 0)
        self.write("Game Over!", align="center", font=FONT)
