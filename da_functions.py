import numpy as np
import pandas as pd
df=pd.read_csv("dataset.csv")
print("--------DATA----------")
print(df)
print("TOTAL UNITS SOLD",df['Units_Sold'].sum())
print('REGION WISE SALES',df.groupby('Region')['Units_Sold'].sum())
print('REGION WISE MEAN REVENUE',df.groupby('Region')['Revenue'].mean())
