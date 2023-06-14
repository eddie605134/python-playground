import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

# 讀取 CSV 檔案
df = pd.read_csv('raw_data.csv', header=None)

# 將 DataFrame 的欄位名稱設定為 'Name', 'Gender', 'Age', 'Income'
df.columns = ['Name', 'Gender', 'Age', 'Income']

# 印出 DataFrame
# print(df)

# print('是否有缺失值', df.isna())

# df = df.dropna()
# df = df.fillna(0)

# print('fillna')
# print(df)
# df['date_string'] = ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06']
# df['Income'] = df['Income'].astype(float)
# df['Date'] = pd.to_datetime(df['date_string'])
# print('轉換資料型態')
# print(df)
# print(df.dtypes)

# 使用 pandas 的 get_dummies() 函數進行一位有效編碼
df_encoded = pd.get_dummies(df, columns=['Gender'])

# 使用 scikit-learn 的 OneHotEncoder 進行一位有效編碼
# encoder = OneHotEncoder(sparse=False)
# df_encoded = pd.DataFrame(encoder.fit_transform(df[['Gender']]))

print(df_encoded)