import pandas as pd
import numpy as np

fake_date = pd.DataFrame(np.random.randint(0, 100, 20).reshape(5, 4), columns=["c1", "c2", "c3", "c4"])

fake_date.index = ["row1", "row2", "row3", "row4", "row5"]

print(fake_date)

"""
      c1  c2  c3  c4
row1   1  51  77  34
row2  51  91   0  77
row3  39  61   1  92
row4   0  77  73  90
row5  57  62  98  64
"""

cond_data1 = fake_date[fake_date.c1 < 50]

print(cond_data1)

"""
      c1  c2  c3  c4
row1   1  51  77  34
row3  39  61   1  92
row4   0  77  73  90

"""
