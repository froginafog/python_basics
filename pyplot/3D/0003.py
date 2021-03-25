from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

z_line = np.linspace(0, 20, 1000)
#np.linspace(start, stop, num, endpoint, retstep, dtype, axis)
#returns evenly spaced numbers over a specified interval.

#start: starting value of the interval
#stop: ending value of the interval
#num: number of points (default value os 50)
#the rest are optional

x_line = np.sin(z_line)
y_line = np.cos(z_line)
ax.plot3D(x_line, y_line, z_line, 'blue')

plt.show()
