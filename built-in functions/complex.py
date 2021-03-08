# The complex() function returns a complex number by specifying a real number and an imaginary number.
# z = x + jy

x1 = 2
y1 = 3
x2 = 4
y2 = 5
print("complex(x1, y1):", complex(x1, y1))
print("complex(x2, y2):", complex(x2, y2))
print("complex(x1, y1) + complex(x2, y2):", complex(x1, y1) + complex(x2, y2))

print("complex(\"2+3j\") + complex(\"2-3j\"):", complex("2+3j") + complex("2-3j"))

"""
complex(x1, y1): (2+3j)
complex(x2, y2): (4+5j)
complex(x1, y1) + complex(x2, y2): (6+8j)
complex("2+3j") + complex("2-3j"): (4+0j)
"""
