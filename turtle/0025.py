import turtle

pen = turtle.Turtle()

r = 15
x = 200
y = 200
pen.goto(x, y)
pen.dot(r)
x = 200
y = 0
pen.goto(x, y)
pen.dot(r)
pen.home() #pen.goto(0, 0)
pen.dot(r)
