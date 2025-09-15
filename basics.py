import numpy as np


list = [1, 2, 3, 4, 5]
#array no orientation
v1 = np.array([1, 2, 3, 4, 5])
#column vector
v2 = np.array([[1], [2], [3], [4], [5]])
#row vector
v3 = np.array([[1, 2, 3, 4, 5]])
v4 = np.array([1, -2, 3, 4, 5])
print(list)
print(v1)
print(v2)
print(v3)
print(v1.shape)
print(v2.shape)
print(v3.shape)



transpose = v3.T
print('row to column vector transpose:\n', transpose)


#Addition
v5 = v1 - v4
print('Addition of two row vectors:\n', v5) 