import pandas as pd 
df = pd.DataFrame(pd.read_excel('data2022.xls'))
df.head()

#Ensemble des données de 2022
df2=df[df["year"]==2022]
df2=df2.set_index("Country name")

df3=df2[["Life Ladder"]]
df3.head()