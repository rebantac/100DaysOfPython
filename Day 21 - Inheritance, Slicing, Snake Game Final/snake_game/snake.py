from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        x = 0
        y = 0

        for _ in range(3):
            position = (x, y)
            self.add_segment(position)
            x -= 20

    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # the last segment moves to the postion of the 2nd last, the 2nd last -> 3rd last and so on
            # thus the snake moves
            # if the 1st segment takes a turn then all the segments will follow
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].setpos(new_x, new_y)
            
        self.head.forward(MOVE_DISTANCE) # so that the segments continue moving
    
    
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.setpos(position)
        self.segments.append(new_segment)

    
    def extend(self):
        self.add_segment(self.segments[-1].position())


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)