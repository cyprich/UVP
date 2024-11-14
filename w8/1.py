import numpy as np
import matplotlib.pyplot as plt

"""
z = f(x, y) = (x^2 + y^2) * sin(1/xy)

$\displaystyle z = f(x,y) = (x^2 + y^2) \sin{\frac{1}{xy}}$

pre x = <-2, 2>
pre y = <-2.5, 2.5>
"""

# karteziansky sucin a.k.a. ✨mriezka✨
x = np.linspace(-2, 2, 100)
y = np.linspace(-2.5, 2.5, 100)
X, Y = np.meshgrid(x, y)
Z = (X**2 + Y**2) * np.sin(1 / (X * Y))
plt.contour(X, Y, Z)
plt.colorbar()
plt.savefig("1-1.svg")

plt.figure()
plt.contourf(X, Y, Z)
plt.colorbar()
plt.savefig("1-2.svg")

plt.show()
