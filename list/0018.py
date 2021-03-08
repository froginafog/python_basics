a = [1, 2, 2, 3, 3, 3, 4, 4, 5]
frequencies = [0] * 5
#frequencies is expected to hold the frequency of each value in list a

for i in range(0, len(frequencies)):
    frequencies[i] = a.count(i + 1)

for i in range(0, len(frequencies)):
    s = "frequency of " + str(i + 1) + " is " + str(frequencies[i])
    print(s)

"""
frequency of 1 is 1
frequency of 2 is 2
frequency of 3 is 3
frequency of 4 is 2
frequency of 5 is 1
"""
