# 7.1 打開和關閉檔案：open() 和 close()
# 在 Python 中，可以使用內置的 open() 函數來打開一個檔案。此函數接受兩個參數：檔案名稱和模式。模式可以是讀模式（'r'）、寫模式（'w'）、添加模式（'a'）或讀寫模式（'r+'）。使用完畢後，應該用 close() 方法關閉檔案。

# 打開一個檔案進行讀取
# f = open('myfile.txt', 'r')
# # 進行操作...
# f.close()  # 別忘了關閉檔案！

# === 例子 ===

# f = open('myfile.txt', 'r', encoding='utf-8')
# content = f.read()  # 讀取整個檔案的內容
# print(content)
# f.close()

# f = open('myfile.txt', 'r', encoding='utf-8')
# line = f.readline()  # 讀取一行
# print(line)
# f.close()

# f = open('myfile.txt', 'r')
# lines = f.readlines()  # 讀取所有行，並返回一個列表
# f.close()

# f = open('myfile.txt', 'w', encoding='utf-8')
# f.write('Hello, world!')  # 寫入一個字符串
# f.close()

# f = open('myfile.txt', 'w', encoding='utf-8')
# f.writelines(['Hello, world!', 'Goodbye, world!'])  # 寫入一個字符串列表
# f.close()

with open('myfile.txt', 'a', encoding='utf-8') as f:
  f.write("\n新添加的內容")