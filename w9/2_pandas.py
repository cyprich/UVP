import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

'''
pandas uses "dataframes"
'''

zviera = ["slimak", "prasa", "slon", "kralik", "zirafa", "kon"]
rychlost = [0.1, 17.5, 40, 48, 52, 88]
zivotnost = [2, 8, 70, 1.5, 25, 28]

df = pd.DataFrame({"rychlost": rychlost, "zivotnost": zivotnost}, index=zviera)
print(df)
print("\n-----\n")

"""
        rychlost  zivotnost
slimak       0.1        2.0
prasa       17.5        8.0
slon        40.0       70.0
kralik      48.0        1.5
zirafa      52.0       25.0
kon         88.0       28.0
"""

# mozeme narabat ako s np polom
print(df.shape)
print(df.columns)
print(df.values)
print(df['zivotnost'].min())
print("\nmaska")
print(df['zivotnost']>10)
print("filtrovanie pomocou masky")
print(df[df['zivotnost']>10])
print()

# vizualizacia
df.plot.bar(rot=0)

plt.figure()
df['zivotnost'].plot.bar(rot=0)
plt.show()
