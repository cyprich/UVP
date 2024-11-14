import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sopt

"""
najst priesecniky grafov dvoch funkcii

f: y = x
g: y = cos(x)

x = <0, pi/2>
"""

f = lambda x: x
g = lambda x: np.cos(x)

x = np.linspace(0, np.pi/2, 100)
y1 = f(x)
y2 = g(x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.grid()
plt.savefig("3-1.svg")

# vypocitat priesecnik
func = lambda x: f(x) - g(x)
vysledok = sopt.fsolve(func, 0.8)  # bod bude priblizne na 0.8 (z grafu)
print(f"priesecnik: {vysledok[0]}")

# priblizenie 1
plt.figure()
x = np.linspace(0.7, 0.8, 100)
y1 = f(x)
y2 = g(x)
plt.plot(x, y1)
plt.plot(x, y2)
plt.grid()
plt.savefig("3-2.svg")

# priblizenie 2
plt.figure()
x = np.linspace(0.73, 0.75, 100)
y1 = f(x)
y2 = g(x)
plt.plot(x, y1)
plt.plot(x, y2)
plt.grid()
plt.savefig("3-3.svg")

"""
vypocet funkcnej hodnoty
f(x)
g(x)
"""
print(f"funkcna hodnota\n\tpre f(x): {f(vysledok)[0]}\n\tpre g(x): {g(vysledok)[0]}")

plt.show()

