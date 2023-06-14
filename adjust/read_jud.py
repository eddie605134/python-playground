import pandas as pd 
df=pd.read_csv("./107後_槍_test.csv")
jfull=df["JFULL"].values.tolist()
print(jfull[0:5])
print(df[0:5])