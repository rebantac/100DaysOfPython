import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self) -> None:
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    
    def create_car(self):
        new_car = Turtle() 
        new_car.shape("square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.setpos(300, random.randint(-250, 250))
        new_car.setheading(180)
        self.cars.append(new_car)


    def move_car(self):
        for car in self.cars:
            car.forward(self.car_speed)
    

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
