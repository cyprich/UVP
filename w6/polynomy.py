import numpy as np

"""
p1 = x^5 - 3x^3 + 4x - 11
p2 = x^2 - 3x + 2
"""

p1 = np.array([1, 0, -3, 0, 4, -11])
# p2 = np.array([0, 0, 0, 1, 3, 2])
p2 = np.array([1, -3, 2])
print(p1)
print(p2)

# hodnoty p2 pre x=10
print(np.polyval(p2, 10))
print(np.polyadd(p1, p2))
print(np.polymul(p1, p2))
print(np.polydiv(p2, np.array([1, -2])))  # p2:(x-2); vrati vysledok a zvysok
print(np.polydiv(p1, p2))
print()


print("derivovanie polynomu")
print("\'exponent napisem pred x ako jeho nasobok (pripadne vynasobim s momentalnym nasobkom x) a exponent zmensim o 1\'")
print(np.polyder(p1))
print(np.polyder(np.polyder(p1)))
print(np.polyder(np.polyder(np.polyder(p1))))

