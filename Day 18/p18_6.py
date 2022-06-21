from turtle import Turtle, Screen
import random

tom = Turtle()
my_screen = Screen()

my_screen.colormode(255)

angle = 0


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b) # a tuple
    return color


tom.speed(0) # '0' is the fastest and '10' is the slowest

# while angle <= 360 :
#     tom.color(random_color())

#     tom.circle(100) # draws a circle with radius = 100 units
#     angle += 1
#     tom.right(angle)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tom.color(random_color())
        tom.circle(100)
        tom.setheading(tom.heading() + size_of_gap)

draw_spirograph(3)

my_screen.exitonclick()
