import turtle

pen = turtle.Turtle()
pen.speed(2)
pen.pensize(5)

stamp_1 = pen.stamp()
x = 200
y = 0
pen.goto(x, y)
stamp_2 = pen.stamp()
x = 200
y = -200
pen.goto(x, y)
stamp_3 = pen.stamp()
x = 0
y = -200
pen.goto(x, y)
stamp_4 = pen.stamp()
x = 0
y = 0
pen.goto(x, y)

pen.clearstamp(stamp_2) #remove the stamp with the id stamp_2
pen.clearstamp(stamp_4) #remove the stamp with the id stamp_4
