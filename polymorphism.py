class Animal:
    def make_sound(self):
        pass  # Abstract method

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class Cow(Animal):
    def make_sound(self):
        print("Moo!")

# Function demonstrating polymorphism
def animal_sound(animal):
    animal.make_sound()

# Creating different animal objects
dog = Dog()
cat = Cat()
cow = Cow()

#static polymorphism
dog.make_sound()
cat.make_sound()
cow.make_sound()


# Calling the same function with different objects
#dynamic polymorphism
animal_sound(dog)   # Woof!
animal_sound(cat)   # Meow!
animal_sound(cow)   # Moo!