d=[]
for i in range(3):
    d.append(int(input()))
e=[x for x in d if x%5==0]
print(e)
e.insert(1,'k')
print(e)

#tuples

l=(1,2,3,4,1)
m=l.count(5)
print(m)
print(l.index(3))
