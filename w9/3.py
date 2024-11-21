import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
read dataframe from file

https://data.slovensko.sk/datasety/7bdacf06-355c-4ba0-bb09-181d587e83c3
"""

df = pd.read_csv("muzeum.csv", delimiter=";")

print(df[:10])

# celkova navstevnost po jednotlivych mesiacoch
navstevnost = df.groupby('Mesiac')["Návštevnosť"].sum()
print(navstevnost)

mesiace=["jan", "feb", "mar", "apr", "maj", "jun", "jul", "aug", "sep", "okt", "nov", "dec"]
plt.pie(navstevnost, labels=mesiace, explode=(0.1,)*12)
plt.title("Navstevnost banskych muzei v jednotlivych mesiacoch roku 2023")
plt.show()

