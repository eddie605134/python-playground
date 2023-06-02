# add()：添加元素到集合中。例如：
s = {1, 2, 3}
s.add(4)
print(s)  # Output: {1, 2, 3, 4}

# remove()：移除集合中的元素。如果該元素不存在，會引發KeyError。例如：
s = {1, 2, 3}
s.remove(2)
print(s)  # Output: {1, 3}

# discard()：移除集合中的元素，如果該元素不存在，不會引發錯誤。例如：
s = {1, 2, 3}
s.discard(2)
print(s)  # Output: {1, 3}
s.discard(4)
print(s)  # Output: {1, 3}

# pop()：移除並返回一個集合中的隨機元素。如果集合為空，則引發KeyError。例如：
s = {1, 2, 3}
print(s.pop())  # Output could be 1, 2, or 3
print(s)

# clear()：移除集合中的所有元素。例如：
s = {1, 2, 3}
s.clear()
print(s)  # Output: set()

# union()：返回兩個集合的聯集（包含在兩個集合中的所有元素）。例如：
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2))  # Output: {1, 2, 3, 4, 5}

# intersection()：返回兩個集合的交集（兩個集合中都有的元素）。例如：
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.intersection(s2))  # Output: {3}

# symmetric_difference()：返回兩個集合的對稱差集（只在其中一個集合中的元素）。例如：
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.symmetric_difference(s2))  # Output: {1, 2, 4, 5}

# issubset() 和 issuperset()：這兩個方法可以檢查一個集合是否是另一個集合的子集或超集。例如：
s1 = {1, 2, 3}
s2 = {1, 2}
print(s2.issubset(s1))  # Output: True
print(s1.issuperset(s2))  # Output: True