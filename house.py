import turtle as t


# # remember the two points for roof
pen = t.Turtle()
pen.color('black')
pen.penup()
pen.goto(-160, -20)
pen.pendown()
pen.setheading(90)
pen.fillcolor("yellow")
pen.begin_fill()
pen.forward(150)
roof1 = pen.position() #### point 1
pen.right(90)
pen.forward(300)
roof2 = pen.position() #### point 2
pen.right(90)
pen.forward(150)
pen.right(90)
pen.forward(300)
pen.right(90)
pen.end_fill()
# #
# #
# # # roof
pen.penup()
pen.goto(roof1)
pen.fillcolor('orange')
pen.begin_fill()
pen.pendown()
pen.goto(-10, 200)
pen.goto(roof2)
pen.goto(roof1)
pen.end_fill()
pen.setheading(90)

pen.penup()
pen.goto(-95,50)
pen.pendown()
pen.fillcolor('light blue')
pen.begin_fill()
pen.forward(50)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(50)
pen.end_fill()
pen.hideturtle()


t.done()