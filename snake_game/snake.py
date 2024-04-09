from turtle import Turtle
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
Move_distance = 20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.segments = []
        self.creat_snake()
        self.head = self.segments[0]
    def creat_snake(self):
        for positions in starting_positions:
            self.add_segment(positions)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(Move_distance)

    def add_segment(self,positions):
        tim = Turtle("square")
        tim.shapesize(stretch_wid=0.75, stretch_len=0.75)
        tim.penup()
        tim.color("white")
        tim.goto(positions)
        self.segments.append(tim)

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
