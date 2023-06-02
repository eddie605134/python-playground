# # 創建一個空列表
# empty_list = []

# # 創建一個含有數字的列表
# numbers = [1, 2, 3, 4, 5]

# # 創建一個含有不同類型元素的列表
# mixed = [1, "Hello", 3.14, ["a", "b", "c"]]

# print(empty_list)  # 輸出：[]
# print(numbers)     # 輸出：[1, 2, 3, 4, 5]
# print(mixed)       # 輸出：[1, 'Hello', 3.14, ['a', 'b', 'c']]



# # 索引與切片
# # 列表支持索引操作，以獲得某個位置的元素。索引從 0 開始。如果索引為負數，則從列表的末尾開始倒數。

# my_list = ['a', 'b', 'c', 'd', 'e']

# print(my_list[0])  # 輸出：'a'
# print(my_list[3])  # 輸出：'d'
# print(my_list[-1])  # 輸出：'e'

# #同樣地，列表也支持切片操作，以獲得列表的一個子集。切片的基本語法是 list[start:stop:step]，其中 start 為起始索引，stop 為結束索引（不包括），step 為步長（默認為 1）。如果省略 start，則默認為 0；如果省略 stop，則默認為列表的長度；如果省略 step，則默認為 1。

# my_list = ['a', 'b', 'c', 'd', 'e']

# print(my_list[1:4])  # 輸出：['b', 'c', 'd']
# print(my_list[2:])   # 輸出：['c', 'd', 'e']
# print(my_list[:3])   # 輸出：['a', 'b', 'c']
# print(my_list[::2])  # 輸出：['a', 'c', 'e'] (每隔一個元素)

# # 修改列表
# # 列表是可變的，這意味著我們可以更改列表的元素值。

# my_list = ['a', 'b', 'c']
# my_list[1] = 'z'
# print(my_list)  # 輸出：['a', 'z', 'c']

# # 添加和刪除元素
# # 我們可以使用 append 方法在列表末尾添加元素，使用 insert 方法在指定位置
# # 插入元素，或者使用 remove 方法刪除第一個匹配的元素，使用 pop 方法刪除指定位置的元素。

# # 添加元素
# my_list = ['a', 'b', 'c']
# my_list.append('d')
# print(my_list)  # 輸出：['a', 'b', 'c', 'd']

# # 在指定位置插入元素
# my_list.insert(2, 'z')
# print(my_list)  # 輸出：['a', 'b', 'z', 'c', 'd']

# # 刪除第一個匹配的元素
# my_list.remove('b')
# print(my_list)  # 輸出：['a', 'z', 'c', 'd']

# # 刪除指定位置的元素
# popped = my_list.pop(1)
# print(my_list)  # 輸出：['a', 'c', 'd']
# print(popped)  # 輸出：'z'，表示被刪除的元素

# # 其他常用方法
# # 列表有許多其他的方法，例如 sort 方法可以對列表進行排序，reverse 方法可以反轉列表，index 方法可以返回某元素的索引值，count 方法可以計算某元素在列表中出現的次數等。
# my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# # 排序
# my_list.sort()
# print(my_list)  # 輸出：[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# # 反轉
# my_list.reverse()
# print(my_list)  # 輸出：[9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]

# # 索引
# print(my_list.index(4))  # 輸出：5

# # 計數
# print(my_list.count(5))  # 輸出：3

# # 方便的迭代語法

# # 在函數調用時傳遞可迭代物件的元素
# def print_nums(a, b, c):
#   print(a, b, c)

# nums = [1, 2, 3]
# print_nums(*nums)  # 輸出：1 2 3

# # 在創建新的列表時包含已有的可迭代物件的元素
# more_nums = [*nums, 4, 5, 6]
# print(more_nums)  # 輸出：[1, 2, 3, 4, 5, 6]


lst = [
    {"name": "cccc", "age": 18},
    {"name": "ll", "age": 19}
]

filtered_lst = [d for d in lst if d["name"] == "cccc"]
print(filtered_lst)  
# 輸出：[{'name': 'cccc', 'age': 18}]

# 列表理解（List Comprehension）

# 生成數值序列：你可以用列表理解來生成一個特定範圍內的數值序列，例如：
nums = [i for i in range(10)]
print(nums)  # 輸出：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 進行轉換：列表理解可以用來對每個元素進行一些轉換或操作，例如：
squares = [x**2 for x in range(10)]
print(squares)  # 輸出：[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 過濾元素：如你所見，你可以在列表理解中加入 if 條件語句來過濾元素，例如：
odd_squares = [
  x**2 
  for x in range(10) 
  if x % 2 == 1
]
print(odd_squares)  # 輸出：[1, 9, 25, 49, 81]

# 平攤嵌套的列表：如果你有一個嵌套的列表（列表中的元素也是列表），你可以使用列表理解來平攤它，例如：
nested_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_lst = [num for sublist in nested_lst for num in sublist]
print(flat_lst)  # 輸出：[1, 2, 3, 4, 5, 6, 7, 8, 9]

