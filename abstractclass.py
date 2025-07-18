#interfaces and abstract class
from abc import ABC, abstractmethod

class Animal(ABC):  # Inherits from ABC

    @abstractmethod
    def speak(self):
        pass  # Must be implemented by any subclass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Works fine:

print(Dog().speak())

# ❌ Error if you try to instantiate abstract class directly
# a = Animal()  # TypeError: Can't instantiate abstract class Animal
