import pandas as pd
import numpy as np 

df1 = pd.DataFrame(np.random.randint(-10, 10, 20).reshape(5, 4), columns=["col1", "col2", "col3", "col4"])

df2 = pd.DataFrame(np.random.randint(-10, 10, 20).reshape(5, 4), columns=["col1", "col2", "col3", "col4"])

new_df = pd.concat([df1, df2])

print(new_df)

"""
   col1  col2  col3  col4
0     2    -6     4     7
1     5    -6   -10     3
2    -2    -4     4    -2
3     1    -2    -6    -1
4    -2    -4     2     5
0     1    -8    -8    -7
1     3    -8     5    -7
2     8    -1   -10     6
3    -2     1     3     5
4    -2    -4     2     5

"""
