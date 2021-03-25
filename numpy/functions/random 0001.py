from numpy import random

x = []

for i in range(0, 5):
    x.append(random.rand())

#random.rand() returns a floating point number between 0.0 and 1.0

print("x:", x)

"""
x: [0.467727969912455, 0.4636688766573437, 0.6584595158653471, 0.474601264882916, 0.12382803819266508]
"""
