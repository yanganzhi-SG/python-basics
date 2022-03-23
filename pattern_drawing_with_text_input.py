import turtle as t

t.shape('turtle')
name = t.textinput("Name", "Please enter your name:")
screen = t.Screen()
screen.title(name+", have fun!")
screen.setup(800, 800)
color = t.textinput("color", '''Do you prefer black & white image or color image?

Please answer 1 for black and white, answer 2 for color''')
if(color=='1'):
    bgcolor = t.textinput('background color', '''Do you prefer 1. a white background or 2. a black background?''')
    if(bgcolor=='1'):
        screen.bgcolor('white')
        t.color('black')
    elif(bgcolor=='2'):
        screen.bgcolor('black')
        t.color('white')
else:
    bgcolor = t.textinput("Background color", "What color do you want for the background?")
    screen.bgcolor(bgcolor)
    turtle_color = t.textinput("Turtle color", "What color do you want to use for drawing?")
    t.color(turtle_color)

number = int(t.numinput("Lucky Number", "Please key in your lucky number (0-10)", 10, 0, 10))
t.penup()
t.goto(-200, 200)
t.write("Let's draw a polygon with "+str(number)+" equal sides", align='left', font=('Arial', 20, 'bold'))
t.goto(-50,-50)
t.pendown()
for i in range(number):
    t.forward(100)
    t.left(180 - 180*(number-2)/number)

t.done()