import numpy as np
import numpy.random as nr

v = np.array([1, 0, -1])
M = np.array([[1, 2, 3], [4, 5, 6]])

print("BASIC STUFF")
print(M + M)
print(-1 * M)
print(M * M)
print()
print()

print("MATICE")
print(M)
print(M.transpose())
print(M @ M.transpose())
print()
print()

print("SHAPE")
print(M.shape)
print(v.shape)
print(M.size)
print()
print()

print("GENERATORY POLA")
# generatory pola
print(np.ones(5))
print(np.ones((3, 2), "bool"))
# print(np.zeros(50, "int"))
# print(np.zeros((5, 5)))
print(np.eye(7))  # jednotkova matica
print(np.eye(7, dtype="int", k=2))
print()
print(np.arange(7))
print(np.arange(1, 7).reshape((2, 3)))
print(np.reshape(np.arange(1, 25), (4, 6)))
print()
print(np.linspace(1, 10, 5))
print()
print(nr.rand(5))  # v intervale <0, 1);  normalne rozdelenie
print(nr.rand(3, 3))
print(nr.randint(5))
print(nr.randint(5, size=10))
print(nr.randint(1, 7, 100))  # 100 hodov kockou
print(nr.choice(np.arange(1, 7, dtype="int"), size=10, p=(0.1, 0.1, 0.1, 0.1, 0.5, 0.1)))  # falosna kocka
print()
a = np.arange(1, 7)
print(a)
nr.shuffle(a)  # nevracia hodnotu, iba premiesa
print(a)
print()
print()


print("NACITANIE + ZAPISANIE DO/ZO SUBORU")
# ciselko = np.loadtxt("cislo.txt").astype(np.int64)  # nejak to nefunguje
# print(ciselko)
np.savetxt("output.txt", M)
np.savetxt("output2.txt", M, fmt="%i")

