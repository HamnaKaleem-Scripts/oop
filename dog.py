# dog.py
from pet import Pet

class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

    def info(self):
        return f"{super().info()}, Breed: {self.breed}"
