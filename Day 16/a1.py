from turtle import Turtle, Screen

tom = Turtle() # 'tom' is an object of Turtle class
tom.shape("turtle") # here, shape() is a method in the Turtle class
tom.color("green")

tom.forward(100) # 'moves' pointer forward by 100 units in the x-axis

my_screen = Screen() # similarly 'my_screen' is an object of Screen class
my_screen.exitonclick()
print(tom)
print(my_screen)