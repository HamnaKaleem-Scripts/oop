# cat.py
from pet import Pet

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return f"{self.name} says Meow!"

    def info(self):
        return f"{super().info()}, Color: {self.color}"
