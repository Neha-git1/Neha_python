class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")

# Dog IS-A Animal
class Dog(Animal):
    def __init__(self, name, breed, color, mat):
        super().__init__("Dog")  # Call parent constructor
        self.name = name
        self.breed = breed
        self.collar = Collar(color, mat)  # HAS-A relationship

    def make_sound(self):
        print("Woof! Woof!")

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Collar Color: {self.collar.color}")
        print(f"Collar Material: {self.collar.material}")


# HAS-A relationship: Composition
class Collar:
    def __init__(self, color, material):
        self.color = color
        self.material = material


# Demo
dog1 = Dog("Buddy", "Labrador", "Red" , "Furr")
dog1.make_sound()         # Overridden method
dog1.show_details()