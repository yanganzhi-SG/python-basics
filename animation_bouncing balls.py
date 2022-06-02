
import turtle as t
import random as r
#
# ######################################
# # Initialization - screen creation
# ######################################

wn = t.Screen()
wn.setup(width=800, height=800)
wn.bgcolor('black')
wn.title('Bouncing Ball Simulator')
wn.tracer(0) # turns off screen update; screen update is done in the while loop

#
# ######################################
# # Initialization - ball creation
# ######################################
#
#
colors = ['red', 'green', 'orange', 'blue', 'yellow', 'white', 'purple']
shapes = ['circle', 'triangle', 'square', 'turtle']

all_balls = []

for i in range(20):

    ball = t.Turtle()

    # balls are of different shapes
    random_shape = r.choice(shapes)
    ball.shape(random_shape) #t.shape('circle')

    # balls are of different colors
    random_color = r.choice(colors)
    ball.color(random_color)

    # go to a random location
    ball.penup()
    x = r.randint(-300, 300)
    y = r.randint(200, 400)
    ball.goto(x,y)

    # each ball moves at different speed horizontally, rotates at different angles
    ball.dx = r.randint(-3,3) #delta x
    ball.dy = r.randint(-3,3)
    ball.da = r.randint(-5,5) #delta angle

    all_balls.append(ball)

# wn.update()
# t.done()

# # ######################################
# # # movement starts here
# # ######################################

while True:

    wn.update()

    for ball in all_balls:

        ball.setx(ball.xcor()-ball.dx)
        ball.sety(ball.ycor()-ball.dy)
        ball.right(ball.da)

        if ball.xcor() > 400:
            ball.dx = ball.dx * (-1)
            ball.da = ball.da * (-1)

        if ball.xcor() < -400:
            ball.dx = ball.dx * (-1)
            ball.da = ball.da * (-1)

        if ball.ycor() > 400:
            ball.dy = ball.dy * (-1)
            ball.da = ball.da * (-1)

        if ball.ycor() < -400:
            ball.dy = ball.dy * (-1)
            ball.da = ball.da * (-1)