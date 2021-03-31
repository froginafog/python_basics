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

r = 100
theta_min = 0
theta_max = 2 * math.pi
theta = theta_min
dtheta = 0.01 * math.pi
x_min = -200
x_max = 200
x = x_min
y = r * math.sin(theta)
dx = 1
pen.goto(x, y)
pen.pendown()

while(x <= x_max):
    y = r * math.sin(theta) 
    pen.goto(x, y)
    x = x + dx
    theta = theta + dtheta
    
    
