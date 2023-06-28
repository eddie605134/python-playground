import pandas as pd
import json



# 讀取 JSON 檔案
# data = pd.read_json('output.json', orient='records')
data = pd.read_json('outputTest.json', orient='records')

# 取出前 30 筆資料
data = data.head(30)

# 印出 DataFrame
print(data)


with open('output.json', 'r') as f:
  json_data = json.load(f)

sub_data = json_data[0:30]
print(json.dumps(sub_data, indent=2, ensure_ascii=False))
