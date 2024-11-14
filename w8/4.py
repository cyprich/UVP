import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as sopt
import scipy.integrate as sint

"""
vypocitat obsah plochy ohranicenej grafmi funkcii
f: y = (x-0.5)^2
g: y = x * e^(-x ^ 2) 
"""

f = lambda x: (x - 0.5) ** 2
g = lambda x: x * np.e ** (-x ** 2)

x = np.linspace(0, 2, 100)
y1 = f(x)
y2 = g(x)
plt.plot(x, y1, x, y2)
plt.grid()
plt.savefig("4-1.svg")

# toto mi nejak nevychadza
func = lambda x: f(x) - g(x)
x1 = sopt.fsolve(func, 0.1)[0]  # priesecniky
x2 = sopt.fsolve(func, 1.1)[0]

X = np.linspace(x1, x2, 100)

# plt.fill_between(x, f(X), g(X), color="yellow")

# vypocet plochy pomocou urciteho integralu
plocha1 = sint.quad(f, x1, x2)[0]
plocha2 = sint.quad(g, x1, x2)[0]

vysledok = abs(plocha1 - plocha2)
print(f"obsah plochy je: {vysledok}")

plt.show()
