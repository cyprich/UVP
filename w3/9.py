'''
<p>A Pythagorean triplet is a set of three natural numbers, $a < b < c$, for which,
$$a^2 + b^2 = c^2.$$</p>
<p>For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.</p>
<p>There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.<br>Find the product $abc$.</p>
'''

import math
zoznam = [(a, b, 1000 - a - b) for a in range(1, 1000) for b in range(a + 1, 1000) if a ** 2 + b ** 2 == (1000 - a - b)**2]
n = math.prod(zoznam[0])

print(zoznam)
print(n)
