import pandas as pd
import numpy as np 

np.random.seed(2026)

df1 = pd.DataFrame(np.random.randint(50, 100, 20).reshape(5, 4), columns=["exam1", "exam2", "exam3", "exam4"])

df2 = pd.DataFrame(np.random.randint(10, 30, 5).reshape(5, 1), columns=["ages"])

new_df = pd.merge(df1, df2, left_index=True, right_index=True)

print(new_df)

"""
   exam1  exam2  exam3  exam4  ages
0     51     56     76     63    26
1     63     79     78     55    16
2     62     78     52     63    14
3     77     82     57     82    29
4     57     97     70     83    26
"""
