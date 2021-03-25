import turtle

pen = turtle.Turtle()
pen.speed(1)
pen.shapesize(5,5,5) #pen.shapesize(stretch length, stretch width, outline width)
pen.color("green") #change both the color of the outline of the pen and its fill color
x = 0
y = 300
pen.goto(x, y)
pen.color("gold")
x = 300
y = 300
pen.goto(x, y)
pen.color("red")
x = 300
y = 0
pen.goto(x, y)
pen.color("blue")
x = 0
y = 0
pen.goto(x, y)
