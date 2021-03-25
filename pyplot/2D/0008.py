# plot for sine, cosine, and the average of sine plus cosine
import matplotlib.pyplot as plt
import math

def f(x):
    return math.exp(x)

def g(x):
    return math.log(x)
        
xMin = 0.1
xMax = 5
dx = 0.1
numOfPoints = int((xMax - xMin)/dx)
xData = [0.0] * numOfPoints
yData1 = [0.0] * numOfPoints
yData2 = [0.0] * numOfPoints
averageData = [0.0] * numOfPoints

x = xMin
for i in range(0, numOfPoints):
    xData[i] = x
    yData1[i] = f(x)
    yData2[i] = g(x)
    averageData[i] = (yData2[i] + yData1[i])/2.0
    x = x + dx

plt.xlabel("x")
plt.ylabel("y")

for i in range(0, numOfPoints):
    plt.scatter(xData[i], yData1[i], color = 'green')
    plt.scatter(xData[i], yData2[i], color = 'red')
    plt.scatter(xData[i], averageData[i], color = 'orange')
    plt.pause(0.001)
