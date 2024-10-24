"""
<p>Starting in the top left corner of a $2 \times 2$ grid, and only being able to move to the right and down, there are exactly $6$ routes to the bottom right corner.</p>
<div class="center">
<img src="resources/images/0015.png?1678992052" class="dark_img" alt=""></div>
<p>How many such routes are there through a $20 \times 20$ grid?</p>
"""

f = {}
def vypocet(n: int, k: int) -> int:
    if n < k or n < 0:
        return 0

    if k in (0, n):
        return 1

    if (n, k) not in f:
        f[(n, k)] = vypocet(n - 1, k - 1) + vypocet(n - 1, k)

    return f[(n, k)]


