from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

x_line = np.linspace(-10, 10, 100)
y_line = np.linspace(-10, 10, 100)

x_mesh, y_mesh = np.meshgrid(x_line, y_line)
z_mesh = x_mesh**2 + y_mesh**2

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(x_mesh, y_mesh, z_mesh, 50)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(45, 20) #set the initial elevation and azimuthal angles for the view
plt.show()
