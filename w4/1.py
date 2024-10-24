"""
fibonnacho postupnost

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
"""


# vrati n-te fib. cislo
def fib_rekurzivne(n: int) -> int:
    if n < 1:
        return 0
    if n in (1, 2):
        return 1
    else:
        return fib_rekurzivne(n - 1) + fib_rekurzivne(n - 2)


print(fib_rekurzivne(-1))
print(fib_rekurzivne(0))
print(fib_rekurzivne(2))
print(fib_rekurzivne(11))
print(fib_rekurzivne(19))


def fib_sekvencne(n: int) -> int:
    if n < 1:
        return 0
    if n in (1, 2):
        return 1

    zoznam = [1, 1]

    for _ in range(n - 2):
        zoznam.append(zoznam[-1] + zoznam[-2])

    return zoznam[-1]


print()
print(fib_sekvencne(-1))
print(fib_sekvencne(0))
print(fib_sekvencne(2))
print(fib_sekvencne(11))
print(fib_sekvencne(19))

# MEMOIZACIA
f = {1: 1, 2: 1}


def fib_memo(n: int) -> int:
    if n < 1:
        return 0
    if n not in f:
        f[n] = fib_memo(n - 1) + fib_memo(n - 2)

    return f[n]


print()
print(fib_memo(-1))
print(fib_memo(0))
print(fib_memo(2))
print(fib_memo(11))
print(fib_memo(19))
print(fib_memo(100))




