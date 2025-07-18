# Parent class
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

# Child class does not override make_sound()
class Dog(Animal):
    pass

# Another child class overrides make_sound()
class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Demo
animal = Animal()
dog = Dog()
cat = Cat()

animal.make_sound()  # Output: Some generic animal sound
dog.make_sound()     # Output: Woof!
cat.make_sound()     # Output: Meow!
