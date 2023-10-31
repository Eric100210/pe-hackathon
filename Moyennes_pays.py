import pandas as pd
import numpy as np
from matplotlib import pyplot as plt 


df=pd.DataFrame(pd.read_excel('data2022.xls'))


group=df.groupby('Country name')
group.head()

country_name=df['Country name'].unique()
country_name
l=df['Country name'].value_counts()
l['Lebanon']


d={}
df=df.fillna(0)
df.dtypes


# +
for name in country_name:
    d[name]=df[df['Country name']==name].drop(columns='Country name').drop(columns='year').sum(axis=0)/l[name]

df2=pd.DataFrame(
