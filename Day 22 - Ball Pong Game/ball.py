from turtle import Turtle

class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(new_x, new_y)
    

    def bounce_y(self):
        self.y_move *= -1
    
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    

    def new_game(self):
        self.setpos(0, 0)
        self.bounce_x()