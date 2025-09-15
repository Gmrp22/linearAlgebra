from functools import reduce
from math import gcd
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


#Multiplication by scalar
v6 = v1 * 3
print('Multiplication by scalar:\n', v6)

v1 = np.array([1, 2, 3])
v2 = np.array([1, -2, 3])
v3 = 4*v1 + 2*v2
print('Linear combination of two vectors:\n', v3)

#FACTORING OUT simple
v = np.array([6, 9])

# Compute GCD of all elements
common_factor = reduce(gcd, v)

# Factor out the common factor
factored_vector = v // common_factor

print("Original vector:", v)
print("Common factor:", common_factor)
print("Factored vector:", factored_vector)

