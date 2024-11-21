import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("psy.csv", delimiter=";")
# print(df[:5])

psy = df[["Ulica", "OrientacneC", "Plemeno"]].rename(columns={"OrientacneC": "Cislo"})
print(psy)

# kolko psov zije na jednotlivych uliciach
pocet = psy.groupby("Ulica").size()
print(pocet)
print()
print()

# kolko psov zije na ulici 11.Marca
print(pocet["11.Marca"])
print()
print()

# na ktorych uliciach zije najviac psov
pocet.sort_values(ascending=False, inplace=True)
print(pocet)
print()
print()

print(pocet.nlargest(3))
print()
print()

# na ktorych uliciach zije >30 psov
print(pocet[pocet>30])
print()
print()

# kolko psov nema uvedenu ulicu
# bezdomovci = pocet[]
# print(bezdomovci)

print(psy["Ulica"]=="Nan")
