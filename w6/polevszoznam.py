from math import sin
import numpy as np

zoznam = [i/10 for i in range(1, 100, 10)]
print(zoznam)
# print(sin(zoznam))

pole = np.arange(1, 100, 10)/10
print(pole)
print(np.sin(pole))
print()


M = np.array([[1, 2, 3], [4, 5, 6]])
print(M)
print(M[0])
print(M[0, :])  # multy riadok, vsetky prvky stlpca
print(M[:, 0])  # vsetky prvky riadku, nulty stlpec
print()

print("maskovanie")
# poviem ze aku podmienku maju splnat hodnoty v danom poli
print(M>3)
# vsetky cisla >3 nastav na 0
M[M>3] = 0  
print(M)
