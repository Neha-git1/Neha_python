class Emp:  # base class
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.father = ""

    def acceptData(self):
        self.name = input("Enter name: ")
        self.phone = input("Enter phone number: ")
        self.father = input("Enter father's name: ")

    def showData(self):
        print("Name:", self.name)
        print("Phone:", self.phone)
        print("Father's Name:", self.father)

class Mgr(Emp):
    def __init__(self):
        super().__init__()  # call Emp constructor
        self.department = ""

    def acceptData(self):
        super().acceptData()
        self.department = input("Enter department: ")

    def showData(self):
        super().showData()
        print("Department:", self.department)

class Acc(Emp):
    def __init__(self):
        super().__init__()
        self.accounting_tool = ""

    def acceptData(self):
        super().acceptData()
        self.accounting_tool = input("Enter accounting tool used: ")

    def showData(self):
        super().showData()
        print("Accounting Tool:", self.accounting_tool)

class VP(Emp):
    def __init__(self):
        super().__init__()
        self.region = ""

    def acceptData(self):
        super().acceptData()
        self.region = input("Enter region of responsibility: ")

    def showData(self):
        super().showData()
        print("Region:", self.region)

# Example usage
if __name__ == "__main__":
    print("Enter Manager Details:")
    mgr = Mgr()
    mgr.acceptData()
    print("\nManager Info:")
    mgr.showData()

    print("\nEnter Accountant Details:")
    acc = Acc()
    acc.acceptData()
    print("\nAccountant Info:")
    acc.showData()

    print("\nEnter VP Details:")
    vp = VP()
    vp.acceptData()
    print("\nVP Info:")
    vp.showData()