"""
<p>The four adjacent digits in the $1000$-digit number that have the greatest product are $9 \times 9 \times 8 \times 9 = 5832$.</p>
<p class="monospace center">

*cislo je v subore euler8_thousanddigitnumber.txt*

<p>Find the thirteen adjacent digits in the $1000$-digit number that have the greatest product. What is the value of this product?</p>
"""

with open("euler8_thousanddigitnumber.txt", "r") as file:
    cislo = file.read().replace("\n", "")


def sucin(vstup: int | str) -> int:
    n = str(vstup)
    vysledok = 1

    for i in n:
        vysledok *= int(i)

    return vysledok

# from functools import reduce
# max([reduce(lambda x,y: x*y, [int(i) for i in stvorica]) for stvorica in beznuly])


dlzka_ntice = 13

ntice = [cislo[i:i+dlzka_ntice] for i in range(len(cislo) - dlzka_ntice + 1)]
beznuly = [i for i in ntice if not '0' in i]
suciny = [sucin(int(i)) for i in beznuly]
print(list(reversed(sorted(suciny)))[0])

