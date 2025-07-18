import numpy as np

a = np.array([1, 2, 3])              # 1D array
b = np.array([[1, 2], [3, 4]])       # 2D array
c = np.zeros((2, 3))                 # 2x3 array filled with 0
d = np.ones((3, 3), dtype=np.int32)  # 3x3 array filled with 1
e = np.arange(0, 10, 2)              # [0, 2, 4, 6, 8]
f = np.linspace(0, 1, 5)             # [0. , 0.25, 0.5, 0.75, 1. ]
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x + y)       # [5 7 9]
print(x * y)       # [ 4 10 18]
print(x ** 2)      # [1 4 9]
print(np.sqrt(x))  # [1. 1.4142 1.732]
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([10, 20, 30])

print(A + B)
# Output:
# [[11 22 33]
#  [14 25 36]]
a = np.array([[10, 20, 30], [40, 50, 60]])

print(a[1, 2])      # 60
print(a[:, 1])      # [20 50]
print(a[0:2, 1:])   # [[20 30]
                   #  [50 60]]
a = np.array([[1, 2, 3], [4, 5, 6]])

reshaped = a.reshape((3, 2))
flattened = a.flatten()

print(reshaped)
# [[1 2]
#  [3 4]
#  [5 6]]

print(flattened)  # [1 2 3 4 5 6]
np.random.seed(0)           # For reproducibility
print(np.random.rand(2, 3)) # Uniform [0,1) in 2x3
print(np.random.randint(1, 10, size=(3,)))  # [1, 10)
