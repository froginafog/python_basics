import turtle

pen = turtle.Turtle()
pen.speed(1)
pen.fillcolor("blue")

#draw a square and fill the square with the blue color
pen.begin_fill()
x = 0
y = 300
pen.goto(x, y)
x = 300
y = 300
pen.goto(x, y)
x = 300
y = 0
pen.goto(x, y)
x = 0
y = 0
pen.goto(x, y)
pen.end_fill()
