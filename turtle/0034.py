import turtle

pen = turtle.Turtle()
pen.speed(1)
pen.pensize(5)
pen.color("red") #color of the trace
pen.fillcolor("blue") #color of the filling

pen.begin_fill()
pen.circle(100)
pen.end_fill()
