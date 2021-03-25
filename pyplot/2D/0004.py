import matplotlib.pyplot as plt
import math

def f(x):
    return math.log(x);

def g(x):
    return math.exp(x);

xMin = 0.1
xMax = 15.0
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

xMin = -5.0
xMax = 3.0
dx = 0.1
numOfPoints = int((xMax - xMin)/dx)
xData = [0.0] * numOfPoints
yData = [0.0] * numOfPoints

x = xMin
for i in range(0, numOfPoints):
    xData[i] = x
    yData[i] = g(x)
    x = x + dx

plt.plot(xData, yData)
plt.legend(['log(x)','exp(x)']) 
plt.show()
