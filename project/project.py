from typing import List
import pandas as pd
import csv

df = pd.read_csv("C:\\Users\\Dhairya\\Desktop\\python\\c 130\\final.csv")
print(df.shape)

del df["hyperlink"]
del df["orbital_radius"]
del df["planet_radius"]

print(list(df))
df.to_csv("project/main.csv")