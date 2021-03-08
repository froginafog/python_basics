a = [3, 2, 1, 5, 4]

minimum = a[0]
for i in range(0, len(a)):
    minimum = a[i] if a[i] < minimum else minimum

print("minimum:", minimum)

"""
minimum: 1
"""
