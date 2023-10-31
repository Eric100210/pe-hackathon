import pandas as pd
import numpy as np
from matplotlib import pyplot as plt 

df = pd.DataFrame(pd.read_excel('data2022.xls'))
df=df.set_index('Country name')

group=df.groupby('Country name')
