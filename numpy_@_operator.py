import numpy as np


a = np.array([[1, 2],
             [3, 4]])
b = np.array([[12, 10],
              [99, 24]])

print(a @ b)  # Matrix multiplication. Yani matris çarpımı
print(a.dot(b))  # Matrix multiplicaiton. Linear Algebra
