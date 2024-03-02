from turtle import Turtle, Screen
import random
race=False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? ENter the color:")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
screen.addshape("f.gif")
f=Turtle()
f.shape("f.gif")
f.goto(x=230,y=0)
y=-50
all_turtle=[]
for i in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(color[i])
    tim.penup()
    tim.goto(x=-230,y=y)
    y += 25
    all_turtle.append(tim)

if user_bet:
    race=True
while race:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winning_color= turtle.pencolor()
            race=False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        distance = random.randint(0,6)
        turtle.forward(distance)




screen.exitonclick()
