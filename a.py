import pandas as pd 

df =pd.read_csv('data.csv')




df['RedRatio']=df['RedRatio']/1000
print(df)
