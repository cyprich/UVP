"""
rekurzivne kombinacne cislo s vyuzitim memoizacie
(n nad k)

pascalov trojuholnik
(5 nad 3) = (4 nad 2) + (4 nad 3)

(n nad k)
    = 1 ak (k = 0) alebo (k = n)
    - inak = (n-1 nad k-1) + (n-1 nad k)
"""

import sys

sys.setrecursionlimit(10_000)


def kombi(n: int, k: int) -> int:
    if n < k or n < 0:
return 0

    if k in (0, n):
        return 1

    return kombi(n - 1, k - 1) + kombi(n - 1, k)


# print(kombi(5, 3))
# print(kombi(10, 4))


f = {}


def kombi_memo(n: int, k: int) -> int:
    if n < k or n < 0:
        return 0

    if k in (0, n):
        return 1

    if (n, k) not in f:
        f[(n, k)] = kombi_memo(n - 1, k - 1) + kombi_memo(n - 1, k)

    return f[(n, k)]


print(kombi_memo(5, 3))
print(kombi_memo(100, 4))
print(f)
