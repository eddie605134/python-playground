# 索引和切片：你可以通過索引獲取元組中的值，或使用切片來獲取元組的一部分。例如：
t = ('Alice', 'Bob', 'Charlie')
print(t[0])  # Output: 'Alice'
print(t[1:3])  # Output: ('Bob', 'Charlie')

# count()：這個方法返回指定元素在元組中出現的次數。例如：
t = ('Alice', 'Bob', 'Charlie', 'Alice')
print(t.count('Alice'))  # Output: 2

# index()：這個方法返回指定元素在元組中的第一個匹配項的索引。例如：
t = ('Alice', 'Bob', 'Charlie', 'Alice')
print(t.index('Alice'))  # Output: 0