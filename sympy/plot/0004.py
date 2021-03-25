from sympy import Symbol, sin, cos, pi, plot_parametric

x = Symbol('x')

x_min = -3*pi
x_max = 3*pi

plot_1 = plot_parametric(sin(x), x, (x, x_min, x_max), line_color = 'red', show = False)

plot_2 = plot_parametric(cos(x), x, (x, x_min, x_max), line_color = 'blue', show = False)

plot_1.extend(plot_2)

plot_1.show()

#how to save a plot:
#plot_1.save('plot.png')




