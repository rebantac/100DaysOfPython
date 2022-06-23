import time
from turtle import Screen
from snake import Snake

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("SNAKE GAME")
my_screen.tracer(0) # turns off all animation

snake = Snake()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    my_screen.update() # turns on the animation; placed here so that the snake is showed after all the segments have moved
    time.sleep(0.1) # so that the turtle can be tracked
    
    snake.move()


my_screen.exitonclick()