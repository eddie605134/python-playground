try:
  x = 10 / 0  # 這將產生一個除以零的錯誤
except ZeroDivisionError:
  print("Attempted to divide by zero.")
    
try:
  '2' + 2  # 字串與整數不能相加
except TypeError:
  print("TypeError: unsupported operand type(s) for +: 'str' and 'int'")
    
try:
  int("abc")  # "abc"不能轉換成整數
except ValueError:
  print("ValueError: invalid literal for int() with base 10: 'abc'")

try:
  print(unknown_var)  # unknown_var變數未定義
except NameError:
  print("NameError: name 'unknown_var' is not defined")
    
try:
  my_list = [1, 2, 3]
  print(my_list[3])  # my_list中沒有索引3
except IndexError:
  print("IndexError: list index out of range")

name = "test"
try:
  my_dict = {name: "Alice", "age": 25}
  print(my_dict)
  print(my_dict["gender"])  # "gender"不是my_dict的一個鍵
except KeyError:
  print("KeyError: 'gender'")