from sympy import plot, Symbol

def f(x):
    return x**2 - 3*x + 10;

x = Symbol('x')

plot(f(x), line_color = 'blue', xlabel = 'x', ylabel = 'y', title = 'f(x) = x**2 - 3*x + 10')

#how to save a plot:
#plot_1.save('plot.png')
