import turtle

pen = turtle.Turtle()
pen.hideturtle()
pen.pensize(5)
pen.penup()
message = "To C or not to C. \nTo Python or not to Python."
pen.write(message, move = False, align = 'left', font = ('arial', 12, 'normal'))
