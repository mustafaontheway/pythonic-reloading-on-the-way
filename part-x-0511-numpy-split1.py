import numpy as np 

arr = np.array([100, 55, 96, 11, 7, 98, 14, 10, -15])

a, b, c = np.split(arr, [2, 4])

print(a)
print(b)
print(c)

# [100  55]
# [96 11]
# [  7  98  14  10 -15]
