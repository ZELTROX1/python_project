# import colorgram

# c= colorgram.extract('51MOIhs2JoL._AC_UF1000,1000_QL80_.jpg',20)
# colors=[]
# for i in c:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_colour = (r,g,b)
#     colors.append(new_colour)
import turtle as t
import random
timmy=t.Turtle()
t.colormode(255)

def formating():
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)

timmy.speed(90)
timmy.penup()
colors=[ (236, 35, 108), (221, 231, 238), (145, 28, 66), (239, 75, 36), (7, 148, 95), (183, 158, 47), (44, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 92), (244, 219, 53), (178, 40, 98), (40, 168, 117)]
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

for i in range(0,90):
    timmy.dot(20,random.choice(colors))
    timmy.forward(50)
    if (i+1)%10==0:
        formating()




timmy.hideturtle()
screen = t.Screen()
screen.exitonclick()