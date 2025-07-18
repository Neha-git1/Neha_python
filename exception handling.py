age = 0
print("Enter your age")
while True:
    try:
        age = int(input())
        break
    except: 
        print("Hey please enter numbers only, please try again")
print("Age = " , age)

# A simple list
fruits = ["apple", "banana", "cherry"]

# Print the list
print("Fruits list:", fruits)

# Try to access an element at an invalid index
try:
    print("Accessing 5th element:", fruits[5])  # Index out of range!
except IndexError as e:
    print("Caught an IndexError:", e)
