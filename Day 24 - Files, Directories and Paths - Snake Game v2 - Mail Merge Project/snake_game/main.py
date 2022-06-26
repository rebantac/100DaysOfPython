import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score


my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("SNAKE GAME")
my_screen.tracer(0) # turns off all animation

snake = Snake()
food = Food()
score = Score()

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

    # Detect collision of snake and food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    
    # Detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        score.reset_highscore()
        snake.reset_snake()
    
    # Detect collision with tail
    for segment in snake.segments[1:]: # the head segment is not considered
        if snake.head.distance(segment) < 10:
            score.reset_highscore()
            snake.reset_snake()



my_screen.exitonclick()