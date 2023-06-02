class Person:
  # 初始化方法，當建立這個類的實例時會被呼叫
  def __init__(self, name, age):
    self.name = name  # 實例變數
    self.age = age  # 實例變數

    # 方法
  def say_hello(self):
    print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p = Person("Alice", 25)  # 建立一個 Person 的實例
p.say_hello()  # 輸出：Hello, my name is Alice and I am 25 years old.

# Dog 為例
class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking.")

    def run(self):
        print(f"{self.name} is running.")

# 創建一個對象
my_dog = Dog("Fido", 2, "Labrador")

# 存取屬性
print(my_dog.name)  # 輸出：Fido
print(my_dog.age)  # 輸出：2
print(my_dog.breed)  # 輸出：Labrador

# 執行方法
my_dog.bark()  # 輸出：Fido is barking.
my_dog.run()  # 輸出：Fido is running.