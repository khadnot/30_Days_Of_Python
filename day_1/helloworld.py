# Day 1 - 30_Days_Of_Python Challenge
import math
import numpy as np

print(2 + 3)
print(3 - 1)
print(2 * 3)
print(3 / 2)
print(3 ** 2)
print(3 % 2)
print(3 // 2)

# Checking data types
print(type(10))
print(type(3.14))
print(type(1+3j))
print(type('Kenn'))
print(type([1, 2, 3]))
print(type({'name': 'Kenn'}))
print(type({9.8, 3.14, 2.7}))
print(type((9.8, 3.14, 2.7)))

#Euclidean distance between (2, 3) and (10, 8)
point_1 = np.array([2, 3])
point_2 = np.array([10, 8])

print(np.linalg.norm(point_1 - point_2))
