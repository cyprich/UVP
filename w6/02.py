import numpy as np
import numpy.random as nr
import time

A1000x1000 = nr.rand(1000, 1000) 
np.savetxt("velkamatica.txt", A1000x1000)
np.save("velkamatica", A1000x1000)

# porovnanie casu nacitania zo suboru
zaciatok = time.time()
nacitane_A = np.loadtxt("velkamatica.txt")
print(f"cas nacitania textoveho: {time.time() - zaciatok}")


zaciatok = time.time()
nacitane_A = np.load("velkamatica.npy")
print(f"cas nacitania binarneho: {time.time() - zaciatok}")

