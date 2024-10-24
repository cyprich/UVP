import numpy as np

# nrozmerne pole
u = np.array([1, 0, -1])
v = np.array([2, 1, 0], dtype="float")

print(u)
print(v)
print()

print(u + v)
print(3 * u)
print(u * v)  # nasobenie po zlozkach
print(u @ v)  # skalarny sucin
print()

M = np.array([[1, 2, 3], [4, 5, 6]])
print(M)

