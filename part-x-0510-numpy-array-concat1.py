import numpy as np 

x = np.array([3, 4, 5])

y = np.array([13, 24, 35])

z = np.array([113, 224, 335])

t = np.array([113.33, 224.45, 335.22])

con_arr1 = np.concatenate([x, y, z])

print(con_arr1)

con_arr2 = np.concatenate([x, y, z, t], dtype="float16")

print(con_arr2)

# [  3   4   5  13  24  35 113 224 335]

# [  3.    4.    5.   13.   24.   35.  113.  224.  335.  113.3 224.5 335.2]
