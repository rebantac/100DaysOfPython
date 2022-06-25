from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.setpos(position)
    

    def up(self):
        new_ycor = self.ycor() + 20
        self.setpos(self.xcor(), new_ycor)

    
    def down(self):
        new_ycor = self.ycor() - 20
        self.setpos(self.xcor(), new_ycor)
