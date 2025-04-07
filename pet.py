# pet.py
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} makes a sound."

    def info(self):
        return f"Name: {self.name}, Age: {self.age}"
