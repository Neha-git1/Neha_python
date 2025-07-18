choice=input("do you want to calculate?")
while choice =='yes':
    n=int(input("enter a number"))
    o=input("enter an operator ")
    n2=float(input("enter anothernumber"))
    if o=='+':
        print(n+n2)
    elif o=='-':
        print(n-n2)
    elif o=='/':
        print(n/n2)
    elif o=='*':
        print(n*n2)
    elif o=='%':
        print(n%n2)
    else:
        print("invalid operator")
print("thanks")
 