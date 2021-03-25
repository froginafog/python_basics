import turtle

pen = turtle.Turtle()
pen.speed(1)
pen.shapesize(5,5,5) #pen.shapesize(stretch length, stretch width, outline width)
pen.fillcolor("green") #change the filling color of the pen
x = 0
y = 300
pen.goto(x, y)
pen.fillcolor("gold")
x = 300
y = 300
pen.goto(x, y)
pen.fillcolor("red")
x = 300
y = 0
pen.goto(x, y)
pen.fillcolor("blue")
x = 0
y = 0
pen.goto(x, y)
