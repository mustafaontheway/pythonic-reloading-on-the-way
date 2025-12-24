import numpy as np 

arr = np.random.randint(-12, 26, 11)

print(arr)

arr_sub1 = arr[1::2]

arr_sub2 = arr[0::3]

print(arr_sub1)

print(arr_sub2)

# [-8 13 -4 -8 -3 -2 -6 -9 -3 -7  8]
# [13 -8 -2 -9 -7]
# [-8 -8 -6 -7]
