#calculate total marks given in a list
marks=[]
s=0
for i in range(4):
    n=int(input("enter your marks  "))
    marks.append(n) #append within the loop
for j in marks:
    s=s+j
print(s)
print(marks)

#take a list from the user and pick the largest number
n=[]
largest=0
for i in range(4):
    l=int(input("enter your numbers  "))
    n.append(l)
for i in n:
    if i>s:
        s=i
print(s)

#sorting
numbers=[]
for i in range(5):
    numbers.append(int(input()))
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
