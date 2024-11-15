import matplotlib.pyplot as plt
import numpy as np

# %matplotlib inline  # display plots inline in notebooks

plt.figure()
x = [2, 8, 13, 14, 17]
y = [11, -2, 4, 6, 5]
plt.plot(x, y)

plt.figure()
plt.plot(x, y, "r*")
plt.grid()

plt.figure()
x = np.linspace(-3, 5, 100)
y = x * np.exp(-x)
plt.xlabel("x")
plt.ylabel("y")
plt.title("$f: y = x\cdot$")
plt.plot(x, y)

plt.figure()
x = np.linspace(-3, 5, 100)
y = np.cos(x)
y2 = np.sin(x)
plt.plot(x, y, x, y2)


def nakresl(predpis, od: int, do: int):
    f = eval("lambda x:" + predpis)
    x = np.linspace(od, do, 1000)
    y = f(x)
    plt.plot(x, y)
    plt.grid()
    plt.title(f"y = {predpis}")


plt.show()
