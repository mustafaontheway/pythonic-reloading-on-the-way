import numpy as np 

my_arr = np.array([3, 12, 13, 23])

my_arr2 = np.array([47, 22.34, 56.21, 12], dtype="float32")

my_arr3 = np.array([3, 12, 13, 23, 22.0/7.0], dtype="float64")

my_arr4 = np.array([47, 22.34, 56.21, 12], dtype="int")

print(my_arr)

print(my_arr2)

print(my_arr3)

print(my_arr4)

# [ 3 12 13 23]
# [47.   22.34 56.21 12.  ]
# [ 3.         12.         13.         23.          3.14285714]
# [47 22 56 12]
