from sympy import plot, Symbol, sin, cos, pi

def f(x):
    return (sin(x) + cos(x))/2;

x = Symbol('x')

x_min = -2*pi
x_max = 2*pi

plot_1 = plot((sin(x), (x, x_min, x_max)),
              (cos(x), (x, x_min, x_max)),
              (f(x), (x, x_min, x_max)),
              show = False
             )

plot_1[0].line_color = 'red'
plot_1[1].line_color = 'blue'
plot_1[2].line_color = 'green'
plot_1.xlabel = 'x'
plot_1.ylabel = 'y'
plot_1.title = 'sin(x), cos(x), (sin(x) + cos(x))/2'

plot_1.show()

#how to save a plot:
#plot_1.save('plot.png')

