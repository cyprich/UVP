import scipy.interpolate as sipol
import numpy as np
import matplotlib.pyplot as plt

"""
najst Taylorov polynom stupna n so stredom v bode x0 pre funkciu f
taylorov polynom = aproximacia funkcie

f: y = cos(x^3)
"""

# taylorov polynom - numpy pole, indexy = koeficienty polynomu
f = lambda x: np.cos(x**3)
x0 = 0
n = 5
tp = sipol.approximate_taylor_polynomial(f, x0, n, 1)

# print(np.cos(x0**3))
# print(np.polyval(tp, x0))

x = np.linspace(-1, 1, 100)
g = lambda x: np.polyval(tp, x)

plt.plot(x, f(x), label="original")
plt.plot(x, g(x), label="taylor")
plt.legend()
plt.grid()
plt.savefig("5-1.svg")

plt.figure()
x = np.linspace(-0.1, 0.1, 100)
plt.plot(x, f(x), label="original")
plt.plot(x, g(x), label="taylor")
plt.legend()
plt.grid()
plt.savefig("5-1.svg")

# print(f"rozdiel medzi hodnotami: {np.cos(x0**3) - np.polyval(tp, x0)}")

plt.show()

