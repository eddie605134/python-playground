x = 10          # 一個整數
y = 3.14        # 一個浮點數
z = "Hello"     # 一個字串
b = True        # 一個布林值
f = False       # 一個布林值

if (b == True):
  print("b is True")
  
def my_function():
  print("Hello From My Function!")
  
my_function()

x = True
y = False
z = True

print((not x) or z)  # 這個會輸出 True

# F string
name = "John"
age = 36
txt = f"My name is {name}, and I am {age}"
print(txt) 
