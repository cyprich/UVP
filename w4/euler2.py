"""
<p>Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with $1$ and $2$, the first $10$ terms will be:
$$1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...$$</p>
<p>By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.</p>
"""

f = {1: 1, 2: 1}


def fib_memo(n: int) -> int:
    if n < 1:
        return 0
    if n not in f:
        f[n] = fib_memo(n - 1) + fib_memo(n - 2)

    return f[n]


# zistovanie, ktore cislo prediahne 4 miliony
i = 0
while True:
    i += 1
    n = fib_memo(i)
    if n > 4_000_000:
        break

# scitovanie parnych cisel
vysledok = 0
for i in range(i):
    n = fib_memo(i)
    if n % 2 == 0:
        vysledok += n

print(vysledok)