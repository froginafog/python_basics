from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

x_line = np.linspace(0, 20, 1000)
y_line = np.linspace(0, 20, 1000)
z_line = x_line**2 + y_line**2
ax.plot3D(x_line, y_line, z_line, 'blue')

#np.linspace(start, stop, num, endpoint, retstep, dtype, axis)
#returns evenly spaced numbers over a specified interval.

#start: starting value of the interval
#stop: ending value of the interval
#num: number of points (default value os 50)
#the rest are optional

x_data = x_line + 5
y_data = y_line + 5
z_data = z_line + 5
ax.scatter3D(x_data, y_data, z_data, c = z_data, cmap = 'Greens')

plt.show()
