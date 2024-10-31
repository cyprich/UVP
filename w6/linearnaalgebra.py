import numpy as np
import numpy.linalg as na

"""
riesenie sustavy lin rovnic

x + y + z = 4
x + 2y + 4z = 12
2x - 3y - z = 4
"""

A = np.array([[1, 1, 1], [1, 2, 4], [2, -3, -1]])
b = np.array([4, 12, 4])
x = na.solve(A, b)
print(x)

# skuska spravnosti
print(A@x == b)
# ako velmi sa vysledok odlisuje
print(A@x - b)  # vysledok sa odlisuje o cca 1e-16, teda cca 0 :)
