import pandas as pd
import numpy as np 

df1 = pd.DataFrame(np.random.randint(-10, 10, 20).reshape(5, 4), columns=["col1", "col2", "col3", "col4"])

df2 = pd.DataFrame(np.random.randint(-10, 10, 20).reshape(5, 4), columns=["col1", "col2", "col3", "col4"])

new_df = pd.concat([df1, df2], ignore_index=True)

print(new_df)

"""
    col1  col2  col3  col4
0    -4     7    -5     0
1    -8     4   -10    -9
2   -10     6    -8    -7
3     6    -3    -1     2
4     5     7     2    -7
5    -4     8     1     4
6    -4    -5     5    -5
7     2     5   -10    -3
8    -8    -4    -7     1
9    -2    -1    -4     3

"""
