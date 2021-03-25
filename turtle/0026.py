import turtle

pen = turtle.Turtle()
pen.speed(1)
#pen.shapesize(stretch length, stretch width, outline width)
pen.shapesize(1, 1, 1) 
x = 0
y = 300
pen.goto(x, y)
pen.shapesize(10, 1, 1) 
x = 300
y = 300
pen.goto(x, y)
pen.shapesize(1, 10, 1)
x = 300
y = 0
pen.goto(x, y)
pen.shapesize(1, 1, 10)
x = 0
y = 0
pen.goto(x, y)
