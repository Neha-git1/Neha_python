#oop
#abstraction
#encapsulation
#inheritance
#polymorphism

class Fruit:
    def __init__(self,n,c,t,p):
        self.name = n
        self.colour=c
        self.taste=t
        self.price=p
    def showdata(self):
        print(f"fruit {self.name} colour is {self.colour} and taste is {self.taste} and cost is {self.price} rupees")

f1  = Fruit("Apple", "Red" , "Sweet",90.9)
f2  = Fruit("Orange", "Orange" , "Sweet",50)
f3  = Fruit("Kiwi", "Green" , "Sweet",70)
f1.showdata()
f2.showdata()
f3.showdata()



