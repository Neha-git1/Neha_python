number=[]
print("enter the list of 10 numbers: ")
for i in range(10):
    number.append(int(input()))
target=int(input("enter target sum: "))
print("your list is:",number)
print("your target is:",target)
for n in number:
    for m in range(n+1,len(number)):
        if m+n==target:
            print(f"your numbers are-{m}+{n}={target}")
            print(f"the indices of the numbers are:{number.index(m)},{number.index(n)}")
    