# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

color_list = [ (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# 10x10 spot painting
# easch spot=20 and spaced by 50

import random
from turtle import Turtle, Screen

tom = Turtle()
tom.speed(0)
tom.hideturtle()

my_screen = Screen()
my_screen.colormode(255)

x = -300
y = -300

for _ in range(10):
    tom.penup()
    tom.setposition(x, y)
    for _ in range(10):
        # tom.color(random.choice(color_list))
        tom.pendown()
        tom.dot(20, random.choice(color_list))
        tom.penup()
        tom.forward(50)
    y += 50

my_screen.exitonclick()
