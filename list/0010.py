a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

N = 5 # number of elements

c = [0] * N # a list of N elements initialized to 0

for i in range(0, N):
    c[i] = a[i] + b[i]

print("c:" , c)

# c: [7, 9, 11, 13, 15]

