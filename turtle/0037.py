import turtle

pen = turtle.Turtle()
pen.speed(2)
pen.pensize(5)

pen.stamp() #stamp the turtle (arrow) on the screen
x = 200
y = 0
pen.goto(x, y)
pen.stamp()
x = 200
y = -200
pen.goto(x, y)
pen.stamp()
x = 0
y = -200
pen.goto(x, y)
pen.stamp()
x = 0
y = 0
pen.goto(x, y)
