import pandas as pd
df = pd.DataFrame(pd.read_excel('data2022.xls'))
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
df.head()
df.columns

df

# +

mask=(df['year']==2022)
df1=df.copy()
df1=df1[mask]

# -

df1=df1.set_index('Country name')

# +
#df1.plot.scatter(x='Log GDP per capita',y='Life Ladder',title="argent=bonheur")
# -

df1.plot.scatter(x='Healthy life expectancy at birth',y='Life Ladder',title="plus on est vieux, plus on est heureux ?")



df2=df1.copy()
mask=df2['Log GDP per capita'].notna()
df2=df2[mask]
df2

pib=np.array(df2['Log GDP per capita'])
lifeladder=np.array(df2['Life Ladder'])
len(lifeladder)

pib=pib.reshape((-1,1))
lifeladder=lifeladder.reshape((-1,1))
model=LinearRegression()
model.fit(pib,lifeladder)
l=(model.coef_,model.intercept_)

plt.scatter(pib,lifeladder)
y=l[0]*pib+l[1]
plt.scatter(pib,y)








