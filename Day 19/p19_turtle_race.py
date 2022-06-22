from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(width=500, height=400)
user_guess = my_screen.textinput(title="Make your bet", prompt="Choose your color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

x = -230
y = -100

flag = False

if user_guess: # so that it doesn't start before the user enters its guess
    flag = True

for color in colors:
    tom = Turtle(shape="turtle")
    turtles.append(tom)
    tom.penup()
    tom.color(color)
    tom.setposition(x = x, y = y)
    y += 30


while flag:
    for turtle in turtles:
        if turtle.xcor() > 230: # final dist = +250 and width of turtle is 20
            flag = False
            winning_color = turtle.pencolor()
            if user_guess == winning_color:
                print("You've won!")
            else:
                print(f"You've lost! The {winning_color} turtle has won.")
            break

        turtle.forward(random.randint(0, 10))

my_screen.exitonclick()