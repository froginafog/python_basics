import turtle

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.pensize(5)
message = "To C or not to C. \nTo Python or not to Python."
pen.write(message, move = False, align = 'left', font = ('arial', 12, 'normal'))
pen.goto(0, -20)
pen.pensize(10)
message = "To Javascript or not to Javascript."
pen.write(message, move = False, align = 'left', font = ('arial', 12, 'normal'))
