import random
n=random.randint(0,100)
score=0
x=int(input("enter a random number "))
while x != n:
    if x>n:
        print("try a lower number ")
        score+=1
    else:
        print("try a higher number ")
        score+=1
    x= int(input("enter a number "))
print("you guessed the number ")
print(f"your score is {score}")
