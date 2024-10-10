import sys, time
from functools import reduce

sys.setrecursionlimit(1_000_000)


def faktorial_sekvencne(n):
    if n < 0:
        return None

    vysledok = 1

    for i in range(1, n + 1):
        vysledok *= i

    return vysledok


def faktorial_rekurzivne(n):
    if n < 0:
        return None

    if n in (0, 1):
        return 1

    return n * faktorial_rekurzivne(n - 1)


def faktorial_lambda(n):
    if n < 0:
        return None

    if n in (0, 1):
        return 1

    return reduce(lambda x, y: x*y, [i for i in range(1, n+1)])


for i in (5, 0, 1, -2, 999):
    print(faktorial_sekvencne(i))
    print(faktorial_rekurzivne(i))
    print(faktorial_lambda(i))
    print()


# porovnanie casu vypoctu
# %time faktorial_rekurzivne(100)
test = 999
start = time.time()
faktorial_sekvencne(test)
print(f"sekvencne: {time.time() - start}")

start = time.time()
faktorial_rekurzivne(test)
print(f"rekurzivne: {time.time() - start}")

start = time.time()
faktorial_lambda(test)
print(f"lambda: {time.time() - start}")
