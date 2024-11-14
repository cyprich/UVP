import scipy
import scipy.integrate as sint
import numpy as np
import matplotlib.pyplot as plt

'''
vypocitat obsah plochy ohranicenej funkciou f a osou x

f: y = e^(-x^2) * sin(x)
$f: y = \mathrm{e}^{-x^2}\sin{x}$

x = <1, 5>
'''

x = np.linspace(1, 5, 1000)
y = np.e**(-x**2) * np.sin(x)
plt.plot(x, y)
plt.fill_between(x, y)
plt.savefig("2-1.svg")

# vypocet obsahu pomocou urciteho integralu 
f = lambda x: np.e**(-x**2) * np.sin(x)
vysledok,chyba = sint.quad(f, 1, 5)

print(f"vysledok:\t{vysledok}\nchyba:\t\t{chyba}")

plt.show()


