import turtle as t
from random import choice,randint


timmy = t.Turtle()
t.colormode(255)
def random_colour():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    return r,g,b
timmy.speed(70)
size=5
for i in range(int(360/size)):
    timmy.pencolor(random_colour())
    timmy.circle(100)
    timmy.setheading(timmy.heading() + size)





















screen = t.Screen()

screen.exitonclick()

