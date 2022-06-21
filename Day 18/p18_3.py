from turtle import Turtle, Screen
from random import randint

tom = Turtle()
my_screen = Screen()

my_screen.colormode(255)

total_angle = 360
side = 3

while side <= 10:
    tom.color(randint(0, 255), randint(0, 255), randint(0, 255))

    angle = total_angle / side
    for _ in range(side):
        tom.forward(100)
        tom.right(angle)
    
    side += 1

my_screen.exitonclick()