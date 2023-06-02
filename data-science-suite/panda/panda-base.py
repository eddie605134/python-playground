import numpy as np
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 32, 22],
    "City": ["New York", "Los Angeles", "San Francisco"]
}
df = pd.DataFrame(data)

# print(df)

s = pd.Series([1, 2, 3, 4, 5])
# print(s)

# 選擇數據
# names = df["Name"]
# print(names)

first_row = df.iloc[0]
# print(first_row)

# 按 Age 列排序
df_sorted = df.sort_values("Age")
# print(df_sorted)

# # 選擇 Age 大於 25 的行
df_filtered = df[df["Age"] > 25]
# print(df_filtered)

# ########################################################### 
# 處理缺失數據

df_missing = pd.DataFrame({
    "A": [1, 2, np.nan],
    "B": [4, np.nan, np.nan],
    "C": [7, 8, 9]
})

# 刪除包含缺失值的行
df_no_na = df_missing.dropna()
print(df_no_na)

# 用 0 填充缺失值
df_filled = df_missing.fillna(0)
print(df_filled)
