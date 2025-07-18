class account:
    def __init__(self):
        self.name=" "
        self.balance=0
    def __innercircle(self):
        print("secret code is  55")
    def acceptdata(self):
        print("enter your name")
        self.name=input()
        print("enter your balance")
        self.balance=int(input())
    def showdata(self):
        print(f"your name is {self.name} and your balance is {self.balance}")
    def secret(self):
        code=input("enter code")
        if code=='1234':
            self.__innercircle()
        else:
            print("invalid code")
a1=account()
a1.acceptdata()
a1.showdata()
a1.secret()
