import numpy as np
from scipy import stats
import random
import matplotlib.pyplot as plt
b=np.random.randint(1,100, size=(25,20))
flat=b.flatten()
above90=flat[flat>90]
count=np.sum(flat>90)
print(b)
print("mean marks=",np.mean(b))
print("median marks=",np.median(b))
print("mode result=",stats.mode(b))
print("number of students who scored above 90=",count)
print("marks of students who scores above 90=",above90)

plt.figure(figsize=(8,5))
plt.hist(flat, bins=10, color='pink', edgecolor='black')
plt.xlabel('value')
plt.ylabel('frequency')
plt.show()