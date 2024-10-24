'''
<p>Work out the first ten digits of the sum of the following one-hundred $50$-digit numbers.</p>

*cislo v subore euler13_cislo.txt*

mame 100 cisel, kde kazde ma 50 cifier 
treba ich scitat
'''

with open("euler13_cislo.txt", "r") as file:
    print(str(sum([int(i) for i in file.read().split("\n") if i != '']))[0:10])

