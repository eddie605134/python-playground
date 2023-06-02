# 基本數學運算：Python 支持加 (+)、減 (-)、乘 (*)、除 (/)、整數除法 (//)、取餘數 (%) 和取冪 (**) 等基本數學運算。
x = 10
y = 3

print(x + y)  # 13
print(x - y)  # 7
print(x * y)  # 30
print(x / y)  # 3.3333333333333335
print(x // y) # 3
print(x % y)  # 1
print(x ** y) # 1000
# 數學函數：Python 的內建 math 模塊提供了許多數學函數，如平方根 (sqrt())、對數 (log())、三角函數 (sin(), cos(), tan() 等)、冪函數 (pow()) 等。

# python
# Copy code
import math

print(math.sqrt(16))  # 4.0
print(math.log(100))  # 4.605170185988092
print(math.sin(math.pi / 2))  # 1.0
print(math.cos(math.pi))  # -1.0
print(math.tan(math.pi / 4))  # 1.0
print(math.pow(2, 3))  # 8.0
# 數字類型轉換：可以使用 int(), float(), complex() 等函數將數字從一種類型轉換為另一種類型。

# python
# Copy code
x = 10
y = 3.14
z = 2 + 3j

print(int(y))  # 3
print(float(x))  # 10.0
print(complex(x))  # (10+0j)
# 絕對值和取整：abs() 函數返回一個數的絕對值，round() 函數對一個數進行四捨五入。

# python
# Copy code
print(abs(-3.14))  # 3.14
print(round(3.14159, 2))  # 3.14
# 在 Python 的 math 模塊中還有許多其他的數學函數和常數，如 math.pi、math.e、math.factorial()、math.radians() 等，這些都是在進行複雜數學運算時非常有用的工具。

import math

# math.pi 表示數學常數 pi（π）
print(math.pi)  # 3.141592653589793

# math.e 表示數學常數 e
print(math.e)  # 2.718281828459045

# math.factorial(x) 可以計算 x 的階乘，即 x*(x-1)*(x-2)*...*3*2*1
print(math.factorial(5))  # 120

# math.radians(x) 將角度 x 轉換為弧度
print(math.radians(180))  # 3.141592653589793

# math.degrees(x) 將弧度 x 轉換為角度
print(math.degrees(math.pi))  # 180.0

# math.sin(x) 和 math.cos(x) 分別計算弧度 x 的正弦值和餘弦值
print(math.sin(math.pi/2))  # 1.0
print(math.cos(math.pi))  # -1.0

# math.exp(x) 計算 e 的 x 次冪
print(math.exp(1))  # 2.718281828459045

# math.log(x, base) 計算以 base 為底數的 x 的對數，如果省略 base，則計算自然對數
print(math.log(10))  # 2.302585092994046
print(math.log(100, 10))  # 2.0

# math.sqrt(x) 計算 x 的平方根
print(math.sqrt(16))  # 4.0

# math.pow(x, y) 計算 x 的 y 次冪
print(math.pow(2, 3))  # 8.0






