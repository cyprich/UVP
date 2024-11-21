import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("muzeum.csv", delimiter=";")
# navstevnost v jednotlivych expziciach po mesiacoch
x = df.groupby(["Expozícia", "Mesiac"])["Návštevnosť"].sum()
# print(x)

# radsej spravit ✨kontingencnu tabulku✨  (pivot table)
navstevnost = df[["Expozícia", "Mesiac", "Návštevnosť"]]
pt = pd.pivot_table(navstevnost, values="Návštevnosť", index="Expozícia", columns="Mesiac", aggfunc="sum")
print(pt)
pt.plot.barh(title="Navstevnost jednolivych expozicii v mesiacoch roku 2023")

print()
print()
print(pt["Handlova":])

plt.show()

