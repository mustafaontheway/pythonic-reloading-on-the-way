import numpy as np 

arr = np.random.randint(-12, 26, size=(6, 6))

print(arr)

print("------------------------------------------")

sub_arr_row_indexes = np.array([0])

sub_arr_column_indexes = np.array([3])

sub_arr = arr[np.ix_(sub_arr_row_indexes, sub_arr_column_indexes)]

print(sub_arr)

"""
[[ -9  -1   0   8  -9  10] 
 [ 18  -1   6 -11  -6  18] 
 [ 22  25   2  16  14  -7] 
 [-11   6  -9  -8  15  -6] 
 [ 18  -6   0  17  23   9] 
 [-11  20   8  -4  10  11]]
------------------------------------------
[[8]]

"""
