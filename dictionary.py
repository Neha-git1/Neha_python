d={}
d["roll"]=int(input("enter roll "))
d["name"]=input("name? ")
print(d)
print(d.keys())
print(d.items())
print(d.values())
print(d.get("name"))

#program to accept 10 numbers and display frequency of each

l={}
for i in range(10):
    n=int(input())
    if n in l:
        l[n]+= 1
    else:
        l[n]=1
print(l)