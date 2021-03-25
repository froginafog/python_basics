import matplotlib.pyplot as plt
import math

def f(x):
    return math.log(x)

def g(x):
    return math.exp(x)
        
xMin = 0.1
xMax = 3.0
dx = 0.1
numOfPoints = int((xMax - xMin)/dx)
xData = [0.0] * numOfPoints
yData1 = [0.0] * numOfPoints
yData2 = [0.0] * numOfPoints

x = xMin
for i in range(0, numOfPoints):
    xData[i] = x
    yData1[i] = f(x)
    yData2[i] = g(x)
    x = x + dx

plt.xlabel("x")
plt.ylabel("y")

for i in range(0, numOfPoints):
    plt.scatter(xData[i], yData1[i], color = 'blue')
    plt.scatter(xData[i], yData2[i], color = 'orange')
    plt.pause(0.001)

