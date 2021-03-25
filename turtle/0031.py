import turtle

pen = turtle.Turtle()
pen.speed(1)
pen.shapesize(5,5,5) #pen.shapesize(stretch length, stretch width, outline width)

pen.shape("turtle")
x = 0
y = 300
pen.goto(x, y)
pen.shape("arrow")
x = 300
y = 300
pen.goto(x, y)
pen.shape("circle")
x = 300
y = 0
pen.goto(x, y)
pen.shape("triangle")
x = 0
y = 0
pen.goto(x, y)


#shape options: arrow, trutle, square, circle, triangle, classic
