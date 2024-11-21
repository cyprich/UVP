import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("psy.csv", delimiter=";")
psy = df[["Ulica", "OrientacneC", "Plemeno"]]
pocet = psy.groupby("Ulica").size()
print(f"PSY_CUT:\n{psy[642:]}\n\n\n")

print(psy[psy["Ulica"].isnull()])
