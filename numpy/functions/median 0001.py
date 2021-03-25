#The numbers must be sorted before we can find the median.
import numpy

a = [1, 3, 2, 1, 1, 4, 6, 7, 5]
a = numpy.sort(a)
med = numpy.median(a) #median
print("a:", a)
print("med:", med)

"""
a: [1 1 1 2 3 4 5 6 7]
med: 3.0
"""
