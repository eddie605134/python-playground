from . import Person

class Employee(Person):  # Employee 是 Person 的子類
  def __init__(self, name, age, employee_id):
    super().__init__(name, age)  # 呼叫父類的 __init__ 方法
    self.employee_id = employee_id  # Employee 類的額外屬性

  def say_hello(self):  # 覆寫父類的方法
    super().say_hello()  # 呼叫父類的 say_hello 方法
    print(f"My employee ID is {self.employee_id}.")