import pandas as pd

# 閱讀 csv 檔案
# df = pd.read_csv('0625去尾.csv')
df = pd.read_csv('test.csv')

# 轉換 DataFrame 至 json 格式，使每一行為一個字典
json_data = df.to_json(orient='records')

# 寫入 json_data 到檔案
with open('outputTest.json', 'w', encoding='utf-8') as f:
  f.write(json_data)