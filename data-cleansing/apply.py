#  異常值處理

import pandas as pd
import numpy as np

# 建立一個有缺失值的 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [4, np.nan, np.nan],
    'C': [7, 8, 9]
})

# 假設我們認為 A 列大於 2 的為異常值
df['A'] = df['A'].apply(lambda x: x if x <= 2 else np.nan)
print(df)