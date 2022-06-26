import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5) # half the original size
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randint(-280, 280) 
        random_y = random.randint(-280, 280)
        # as size of screen is 300 x 300
        self.setpos(random_x, random_y)
