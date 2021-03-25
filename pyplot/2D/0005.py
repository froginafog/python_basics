import matplotlib.pyplot as plt
import math

def f(x):
    return math.log(x)
        
xMin = 0.1
xMax = 3.0
dx = 0.01
numOfPoints = int((xMax - xMin)/dx)
xData = [0.0] * numOfPoints
yData = [0.0] * numOfPoints

x = xMin
for i in range(0, numOfPoints):
    xData[i] = x
    yData[i] = f(x)
    x = x + dx

plt.xlabel("x")
plt.ylabel("y")

for i in range(0, numOfPoints):
    plt.scatter(xData[i], yData[i], color = 'blue')
    plt.pause(0.0001)

plt.close('all')
