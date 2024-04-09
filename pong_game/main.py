from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title(" PING PONG BALL")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        r_paddle.y+= 2

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        l_paddle.y += 2

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        score.update()
        l_paddle.y = 20
        r_paddle.y = 20

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
        score.update()

    if score.l_score == 10:
        game_on = False
        print("left player wins")
    if score.r_score == 10:
        game_on = False
        print("Right player wins")

screen.exitonclick()
