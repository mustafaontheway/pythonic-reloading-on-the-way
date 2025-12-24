import numpy as np 

arr = np.random.randint(-12, 26, size=(6, 6))

print(arr)

print("------------------------------------------")

arr_logical_condition = arr > 3

print(arr_logical_condition)

print("------------------------------------------")

print(arr[arr_logical_condition])

"""
[[  7 -12  -3  20 -12 -10]
 [  5  21  19  -3  -6  -5]
 [ 17  22  -7  25  17   4]
 [  4   0  -5 -11  24   2]
 [-11  23  -2  16  11   5]
 [ 11  25  13   4   4   0]]
------------------------------------------
[[ True False False  True False False]
 [ True  True  True False False False]
 [ True  True False  True  True  True]
 [ True False False False  True False]
 [False  True False  True  True  True]
 [ True  True  True  True  True False]]
------------------------------------------
[ 7 20  5 21 19 17 22 25 17  4  4 24 23 16 11  5 11 25 13  4  4]

"""
