import pandas as pd
import numpy as np 

np.random.seed(2026)

names_df = pd.DataFrame(["ayhan", "bilge", "bengü", "kültigin", "turan"], columns=["names"])

df1 = pd.DataFrame(np.random.randint(50, 100, 20).reshape(5, 4), columns=["exam1", "exam2", "exam3", "exam4"])

df1 = pd.concat([df1, names_df], axis=1)

df2 = pd.DataFrame(np.random.randint(10, 30, 5).reshape(5, 1), columns=["ages"])

df2 = pd.concat([df2, names_df], axis=1)

print(df1)

print("------------------------")

print(df2)

print("------------------------")

new_df = pd.merge(df1, df2)

print(new_df)

"""
   exam1  exam2  exam3  exam4     names
0     51     56     76     63     ayhan
1     63     79     78     55     bilge
2     62     78     52     63     bengü
3     77     82     57     82  kültigin
4     57     97     70     83     turan
------------------------
   ages     names
0    26     ayhan
1    16     bilge
2    14     bengü
3    29  kültigin
4    26     turan
------------------------
   exam1  exam2  exam3  exam4     names  ages
0     51     56     76     63     ayhan    26
1     63     79     78     55     bilge    16
2     62     78     52     63     bengü    14
3     77     82     57     82  kültigin    29
4     57     97     70     83     turan    26
"""
