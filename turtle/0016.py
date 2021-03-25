import turtle

pen = turtle.Turtle()

pen.penup() #lift up the pen to avoid drawing
x = 0
y = 0
pen.goto(x, y)
pen.pendown() #put down the pen on the screen to draw
x = 300
y = 0
pen.goto(x, y)

pen.penup()
x = 0
y = 100
pen.goto(x, y)
pen.pendown()
x = 300
y = 100
pen.goto(x, y)

pen.penup()
x = 0
y = 200
pen.goto(x, y)
pen.pendown()
x = 300
y = 200
pen.goto(x, y)
