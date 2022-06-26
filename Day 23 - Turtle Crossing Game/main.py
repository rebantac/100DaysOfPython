import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("TURTLE CROSSING")

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

i = 1
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_car()

    if i % 6 == 0: # new car is created every 6th time the loop runs
        car_manager.create_car()
    i += 1

    # Detects turtle's collision with cars
    for car in car_manager.cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    # Detect turtle's crossing to the other side
    if player.ycor() > 280:
        player.start_position()
        car_manager.increase_speed()
        score.update_level()
        

screen.exitonclick()