import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as scipol

'''
interpolacia a aproximacia dat
'''
"""
nieco s obrazkami

from scipy import ndimage, misc

namet na semestralku
"""


x = np.linspace(0, 9, 100)
y = np.sin(x)

# merania
n = np.linspace(0, 9, 20)
yn = np.sin(n) + 0.1 * np.random.randn(20)

plt.plot(x, y, "--", color="lightgray")
plt.plot(n, yn, "o")

li = scipol.interp1d(n, yn)  # linearna interpolacia
# plt.plot(x, li(x))

ki = scipol.interp1d(n, yn, "cubic")  # kubicka interpolacia
# plt.plot(x, ki(x))

si = scipol.UnivariateSpline(n, yn, k=5)  # interpolacia pomocou spline
plt.plot(x, si(x))




plt.show()

