import matplotlib.pyplot as plt

def f(x):
    return x**2;

xMin = -5.0
xMax = 5.0
dx = 0.1
numOfPoints = int((xMax - xMin)/dx)
xData = [0.0] * numOfPoints
yData = [0.0] * numOfPoints

x = xMin
for i in range(0, numOfPoints):
    xData[i] = x
    yData[i] = f(x)
    x = x + dx

plt.plot(xData, yData)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
