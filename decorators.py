def decogreet(func):
    def wrapper():
        print("welcome")
        func()
    return wrapper
@decogreet
def greet():
    print("hello")
greet()

def decodiv(func):
    def wrapper(a,b):
        if b==0:
            print("zero error, changing denominator to 1")
            b=1
        func(a,b)
    return wrapper
@decodiv
def div(a,b):
    print(a/b)

div(9,0)
