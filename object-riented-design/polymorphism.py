class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"

def make_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

make_sound(dog)  # 輸出："Woof!"
make_sound(cat)  # 輸出："Meow!"
