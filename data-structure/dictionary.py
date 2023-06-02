d = {'name': 'Alice', 'age': 25}
d.clear()
print(d)  # 輸出：{}

d = {'name': 'Alice', 'age': 25}
print(d.get('name'))  # 輸出：Alice
print(d.get('address'))  # 輸出：None
print(d.get('address', 'N/A'))  # 輸出：N/A

d = {'name': 'Alice', 'age': 25}
print(d.keys())  # 輸出：dict_keys(['name', 'age'])

d = {'name': 'Alice', 'age': 25}
print(d.values())  # 輸出：dict_values(['Alice', 25])

d = {'name': 'Alice', 'age': 25}
print(d.items())  # 輸出：dict_items([('name', 'Alice'), ('age', 25)])

d = {'name': 'Alice', 'age': 25}
print(d.pop('age'))  # 輸出：25
print(d)  # 輸出：{'name': 'Alice'}

d = {'name': 'Alice', 'age': 25}
d.update({'age': 26, 'city': 'New York'})
print(d)  # 輸出：{'name': 'Alice', 'age': 26, 'city': 'New York'}

d = {'name': 'Alice', 'age': 25}
items_list = list(d.items())

new_dict = {}
for item in items_list:
    key, value = item
    if key == 'age':
        value += 1
    new_dict[key] = value

print(new_dict)  # 輸出：{'name': 'Alice', 'age': 26}

d = {'age': 18, 'name': 'eddie', 'country': 'USA'}

name = d.get('name')
age = d.get('age')
country = d.get('country')

print(name, age, country)  # 輸出：eddie 18 USA

# 字典
dict1 = {'A': 1, 'B': 2}
dict2 = {'C': 3, 'D': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)  # 輸出：{'A': 1, 'B': 2, 'C': 3, 'D': 4}