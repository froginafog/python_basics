import matplotlib.pyplot as plt

xMin = -5
xMax = 5
step = 1
x = list(range(xMin, xMax, step))

yMin = -5
yMax = 5
step = 1
y = list(range(yMin, yMax, step))

plt.plot(x, y)
plt.show()
