from turtle import Turtle, Screen

tom = Turtle()
my_screen = Screen()


def mv_fd():
    tom.forward(20)


def mv_bd():
    tom.backward(20)


def mv_lt():
    tom.left(10)


def mv_rt():
    tom.right(10)


def clear_sc():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


my_screen.listen()
my_screen.onkey(key="w", fun=mv_fd)
my_screen.onkey(key="s", fun=mv_bd)
my_screen.onkey(key="a", fun=mv_lt)
my_screen.onkey(key="d", fun=mv_rt)
my_screen.onkey(key="c", fun=clear_sc)


my_screen.exitonclick()