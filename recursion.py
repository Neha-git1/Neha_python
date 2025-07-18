def factorial(n):
    if n==1 or n==0:
        return n
    else:
        return n * factorial(n-1)
print(factorial(3))

def fibonacci(x):
    if x<=1:
        return x
    else:
        return fibonacci(x-1) + fibonacci(x-2)
for i in range(6):
    print(fibonacci(i), end=" ")

def sumofdigits(x):
    if x==0:
        return 0
    else:
        return x%10 + sumofdigits(x//10)  #// divides without decimal
    
print("\n",sumofdigits(345))
    