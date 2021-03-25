import numpy as np
import matplotlib.pyplot as plt
import math

#"np" is the name of the object to access "numpy"
#"plt" is the name of the object to access "matplotlib.pyplot"

def f(x):
    return np.sin(x)

#create 100 points between -2pi and 2pi
xMin = -2*math.pi
xMax = 2*math.pi
numPoints = 100
xData = np.linspace(xMin,xMax,numPoints)
yData = f(xData)

plt.plot(xData, yData, color = 'green', linestyle = 'solid')  
plt.legend('sin(x)')
plt.show()


