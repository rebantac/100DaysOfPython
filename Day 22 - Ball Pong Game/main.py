import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG GAME")
screen.tracer(0)
player1, player2 = screen.textinput(title="Make your bet", prompt="Enter player namess").split()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

winner = ""
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # Detect if ball goes past right paddle
    if ball.xcor() > 380:
        ball.new_game()
        score.point("left")
        if score.l_score >= 10:
            winner = player1
            game_is_on = False
    
    # Detect if ball goes past left paddle
    if ball.xcor() < -380:
        ball.new_game()
        score.point("right")
        if score.r_score >= 10:
            winner = player2
            game_is_on = False
        
score.game_over(winner)

screen.exitonclick()