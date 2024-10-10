# scitovanie 2 cisel
sucet = lambda x, y: x + y
print(sucet(2, 3))

# reduce
# aplikuje funkciu na zoznam cisel
from functools import reduce
print(reduce(sucet, [i for i in range(1, 6)]))

