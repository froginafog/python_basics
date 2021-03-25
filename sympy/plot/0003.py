from sympy import plot, Symbol, sin, cos, pi

x = Symbol('x')

x_min = -2*pi
x_max = 2*pi

plot_1 = plot(sin(x), (x, x_min, x_max), line_color = 'red', show = False)

plot_2 = plot(cos(x), (x, x_min, x_max), line_color = 'blue', show = False)

plot_1.extend(plot_2)

plot_1.show()

#how to save a plot:
#plot_1.save('plot.png')




