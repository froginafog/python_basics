import turtle
import math
import time
#--------------------------------------------------
def draw_line(pen, x_start, y_start, x_end, y_end):
    pen.penup()
    pen.goto(x_start, y_start)
    pen.pendown()
    pen.goto(x_end, y_end)
    pen.penup()
#--------------------------------------------------

window = turtle.Screen()  
window.bgcolor("midnightblue")  
window.setup(width = 1.0, height = 1.0)
window.colormode(255)

pen = turtle.Turtle()  
pen.color("silver")
pen.pensize(2)
pen.speed(5)
pen.hideturtle()

draw_line(pen, -600, 0, 600, 0) 
draw_line(pen, 0, 500, 0, -500)

pen.goto(0, 0)
pen.color("lightgreen")

a_1 = 100
a_2 = -100
w = 1 #angular frequency
t = 0
dt = 0.1
x_min = -200
x_max = 200
x = x_min
y = a_1 * math.sin(w*t) + a_2 * math.cos(w*t)
dx = 1
pen.goto(x, y)
pen.pendown()

while(x <= x_max):
    y = a_1 * math.sin(w*t) + a_2 * math.cos(w*t)
    pen.goto(x, y)
    x = x + dx
    t = t + dt
    
    
