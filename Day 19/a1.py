from turtle import Turtle, Screen

tom = Turtle()
my_screen = Screen()


def mv_fd():
    tom.forward(20)


my_screen.listen()
my_screen.onkey(key="space", fun=mv_fd)


my_screen.exitonclick()