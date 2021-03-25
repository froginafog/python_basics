import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x1 = np.array([0, 1, 2, 3, 4])
y1 = np.array([10, 20, 30, 40, 50])

#plt.subplot(number of rows, number of columns, plot index)
plt.subplot(2, 1, 1)
plt.plot(x1,y1)
plt.title("increasing")

#plot 2:
x2 = np.array([0, 1, 2, 3, 4])
y2 = np.array([50, 40, 30, 20, 10])

plt.subplot(2, 1, 2)
plt.plot(x2,y2)
plt.title("decreasing")

plt.show()
