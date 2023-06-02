s1 = "Hello"
s2 = "World"
s = s1 + " " + s2  # "Hello World"

s = "Hello World"
print(s[0:5])  # 輸出 "Hello"

s = "Hello World"
print(len(s))  # 輸出 11

s = "Hello World"
words = s.split(" ")  # ["Hello", "World"]

s = "Hello World"
s = s.replace("World", "Python")  # "Hello Python"

name = "Alice"
age = 25

# 使用 % 格式化
s = "Hello, my name is %s and I'm %d years old." % (name, age)

# 使用 str.format()
s = "Hello, my name is {} and I'm {} years old.".format(name, age)

# 使用 f-string
s = f"Hello, my name is {name} and I'm {age} years old."