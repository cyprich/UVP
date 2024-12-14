# zoznam cisel od 1 po 10
z = [i for i in range(1, 11)]
print(z)

# zoznam cisel <100, ktore su delitelne 3 a 5
z = [i for i in range(100) if i%3 == 0 and i%5 == 0]
print(z)

# zoznam druhych mocnin cisel <1, 20>
z = [i**2 for i in range(1, 21)]
print(z)

# zoznam vsetkych hran kompletneho grafu s mnozinou vrcholov v
# basically vsetky usecky medzi 2 bodmi
v = [1, 2, 3]
i = [(i, j) for i in v for j in v if i != j and i < j]
print(i)


print()
# if we list all the natural numbers below 10 that are multiplies of 3 or 5, we gen 3, 5, 6 and 9. The sum of these multiples is 23
# find the sum of all the multiples of 3 or 5 below 1000
z = [i for i in range(10) if i % 3 == 0 or i % 5 == 0]
print(z)
print(sum(z))

z = [i for i in range(1000) if i % 3 == 0 or i % 5 == 0]
print(sum(z))

