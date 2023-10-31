import pandas as pd 
import seaborn as sns

df = pd.DataFrame(pd.read_excel('data2022.xls'))
df=df.fillna(0)
df.head()

#Ensemble des données de 2022
df2=df[df["year"]==2022]
df2=df2.set_index("Country name")

#Tableau avec simplement la colonne Life Ladder
df3=df2[["Life Ladder"]]
df3.head()

#liste_pays contient la liste séparée des tableaux de chaque pays
group=df.groupby("Country name")
liste_pays=[]
for i in df["Country name"].unique():
    liste_pays.append(group.get_group(i))

sns.pairplot(data=df2) #graphiques 