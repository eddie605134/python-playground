import pandas as pd
import numpy as np

# 建立一個有缺失值的 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [4, np.nan, np.nan],
    'C': [7, 8, 9]
})

print(df)

# 檢查是否有缺失值
print(df.isnull())

# 刪除有缺失值的列
df_dropped = df.dropna()
print(df_dropped)

# 填補缺失值
df_filled = df.fillna(value=0)
print(df_filled)