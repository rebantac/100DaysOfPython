from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start_position()
    

    def move_up(self):
        self.forward(MOVE_DISTANCE)
    

    def start_position(self):
        self.setpos(STARTING_POSITION)
        self.setheading(90)

