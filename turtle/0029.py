import turtle

pen = turtle.Turtle()
pen.speed(1)
pen.shapesize(5,5,5) #pen.shapesize(stretch length, stretch width, outline width)
pen.pencolor("green") #change the color of the outline of the pen
x = 0
y = 300
pen.goto(x, y)
pen.pencolor("gold")
x = 300
y = 300
pen.goto(x, y)
pen.pencolor("red")
x = 300
y = 0
pen.goto(x, y)
pen.pencolor("blue")
x = 0
y = 0
pen.goto(x, y)
