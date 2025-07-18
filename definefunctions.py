def greet(x):
    print("hello this is",x)
greet("neha")

d=[1,2,3,4,5,6,89,12,45]
def greater(a):
    if a>10:
        return a
def double(a):
    return a*2
e=filter(greater,d)
print(list(e))
f=map(double,d)
print(list(f))