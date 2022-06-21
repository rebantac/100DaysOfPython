from turtle import Turtle, Screen
import random

tom = Turtle()
my_screen = Screen()

my_screen.colormode(255)

angles = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b) # a tuple
    return color


tom.pensize(15)
tom.speed(0) # '0' is the fastest and '10' is the slowest

for _ in range(50):
    tom.color(random_color())
    angle = random.choice(angles)
    tom.forward(20)
    tom.setheading(angle)
    
    



my_screen.exitonclick()