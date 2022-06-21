# change thickness
# increase speed of turtle

from turtle import Turtle, Screen
import random

tom = Turtle()
my_screen = Screen()

my_screen.colormode(255)

angles = [0, 90, 180, 270]

tom.pensize(15)
tom.speed(0) # '0' is the fastest and '10' is the slowest

for _ in range(50):
    tom.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    angle = random.choice(angles)
    tom.forward(20)
    tom.setheading(angle)
    
    



my_screen.exitonclick()