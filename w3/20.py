'''
<p>$n!$ means $n \times (n - 1) \times x \times 3 \times 2 \times 1$.</p>
<p>For example, $10! = 10 \times 9 \times x \times 3 \times 2 \times 1 = 3628800$,<br>and the sum of the digits in the number $10!$ is $3 + 6 + 2 + 8 + 8 + 0 + 0 = 27$.</p>
<p>Find the sum of the digits in the number $100!$.</p>
'''

def faktorial_rekurzivne(n):
    if n < 0:
        return None

    if n in (0, 1):
        return 1

    return n * faktorial_rekurzivne(n - 1)

# n = str(faktorial_rekurzivne(10))
n = sum([int(i) for i in str(faktorial_rekurzivne(100))])
print(n)
