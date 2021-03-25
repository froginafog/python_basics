from sympy import Symbol, sin, pi
from sympy.plotting import plot3d

x = Symbol('x')
y = Symbol('y')

x_min = -3*pi
x_max = 3*pi

y_min = -4
y_max = 4

plot_1 = plot3d(sin(x)*y, (x, x_min, x_max), (y, y_min, y_max), show = False)

plot_2 = plot3d(x + y, (x, x_min, x_max), (y, y_min, y_max), show = False)

plot_1.extend(plot_2)

plot_1.show()

#how to save a plot:
#plot_1.save('plot.png')




