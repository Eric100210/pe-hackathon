import pandas as pd
import numpy as np
from matplotlib import pyplot as plt 


# +
df=pd.DataFrame(pd.read_excel('data2022.xls'))

df=df.set_index('Country name')
# -

group=df.groupby('Country name')
group.head()

country_name=df['Country name'].unique()
country_name
l=df['Country name'].value_counts()
l['Lebanon']


d={}
df=df.fillna(0)
df.dtypes


for i in country_name:
    d[name]=df[df['Country name']==name].sum(axis=1)/l[name]
