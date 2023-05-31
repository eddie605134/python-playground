# 解包元組
t = ('Alice', 25)
name, age = t
print(name)  # 輸出：Alice
print(age)  # 輸出：25

# 解包列表
lst = ['Alice', 25]
name, age = lst
print(name)  # 輸出：Alice
print(age)  # 輸出：25

# 解包字串
str = 'AI'
first_char, second_char = str
print(first_char)  # 輸出：A
print(second_char)  # 輸出：I

# 在迴圈中解包
pairs = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
for name, age in pairs:
    print(f'{name} is {age} years old.')
    

# 解包字典
d = {'name': 'Alice', 'age': 25}

name, age = d.values()  # 解構字典的值

print(name)  # 輸出：Alice
print(age)  # 輸出：25

d = {'age': 18, 'name': 'eddie'}

if (name := d.get('name')) is not None:
  print(name)  # 輸出：eddie